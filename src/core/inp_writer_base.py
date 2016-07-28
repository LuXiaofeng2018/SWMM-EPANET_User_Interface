import inspect
import traceback
from enum import Enum
from core.project import Project, Section, SectionAsListOf

try:
    basestring
except NameError:
    basestring = str


class InputFileWriter(object):
    """Input File Reader and Writer"""

    def as_text(self, project):
        section_text_list = []
        try:
            for section in project.sections:
                attr_name = "write_" + project.format_as_attribute_name(section.SECTION_NAME)
                if hasattr(self, attr_name):
                    writer = self.__getattribute__(attr_name)
                elif section.value is basestring:
                    writer = SectionWriter()
                else:
                    writer = SectionWriterAsListOf(section.SECTION_NAME, type(section), SectionWriter(), None)
                try:
                    section_text = writer.as_text(section).rstrip('\n')
                    if section_text:                               # Skip adding blank sections
                        section_text_list.append(section_text)
                except Exception as e1:
                    section_text_list.append(str(e1) + '\n' + str(traceback.print_exc()))
            return '\n\n'.join(section_text_list) + '\n'
        except Exception as e2:
            return str(e2) + '\n' + str(traceback.print_exc())

    def write_file(self, project, file_name):
        if file_name:
            with open(file_name, 'w') as writer:
                writer.writelines(self.as_text(project))
                project.file_name = file_name


class SectionWriter(object):
    """Base class for writing a section or sub-section or value to an input file"""

    field_format = " {:19}\t{}"

    @staticmethod
    def as_text(section):
        """ Format contents of this section for writing to inp file.
            Args:
                section (Section): section of input sequence
        """
        if isinstance(section, basestring):
            return section
        txt = SectionWriter._get_text_using_metadata(section)
        if txt or txt == '':
            return txt
        if isinstance(section.value, basestring) and len(section.value) > 0:
            return section.value
        elif isinstance(section.value, (list, tuple)):
            text_list = []
            if hasattr(section, "SECTION_NAME") and section.SECTION_NAME:
                text_list.append(section.SECTION_NAME)
            if section.comment:
                text_list.append(section.comment)
            for item in section.value:
                text_list.append(str(item))
            return '\n'.join(text_list)
        elif section.value is None:
            return ''
        else:
            return str(section.value)

    @staticmethod
    def _get_text_using_metadata(section):
        """ Get input file representation of section using attributes represented in metadata, if any.
            Private method intended for use by subclasses.
            Returns empty string if the attributes in metadata have no values.
            Returns None if there is no appropriate metadata."""
        if hasattr(section, "metadata") and section.metadata:
            found_any = False
            text_list = []
            if hasattr(section, "SECTION_NAME"):
                text_list.append(section.SECTION_NAME)
            if section.comment:
                text_list.append(section.comment)
                if section.comment != getattr(section, "DEFAULT_COMMENT", ''):
                    found_any = True
            for metadata_item in section.metadata:
                attr_line = SectionWriter._get_attr_line(section, metadata_item.input_name, metadata_item.attribute)
                if attr_line:
                    text_list.append(attr_line)
                    found_any = True
            if found_any:
                return '\n'.join(text_list)
            return ''
        return None

    @staticmethod
    def _get_attr_line(section, label, attr_name):
        if label and attr_name and hasattr(section, attr_name):
            attr_value = getattr(section, attr_name)
            if isinstance(attr_value, Enum):
                attr_value = attr_value.name.replace('_', '-')
            if isinstance(attr_value, bool):
                if attr_value:
                    attr_value = "YES"
                else:
                    attr_value = "NO"
            if isinstance(attr_value, list):
                attr_value = ' '.join(attr_value)
            if attr_value or attr_value == 0:
                return SectionWriter.field_format.format(label, attr_value)
        else:
            return None


class SectionWriterAsListOf(SectionWriter):
    def __init__(self, section_name, list_type, list_type_writer, section_comment):
        if not section_name.startswith("["):
            section_name = '[' + section_name + ']'
        self.SECTION_NAME = section_name.upper()
        SectionWriter.__init__(self)
        self.list_type = list_type
        if isinstance(list_type_writer, type):
            self.list_type_writer = list_type_writer()
        else:
            self.list_type_writer = list_type_writer

        if section_comment:
            self.DEFAULT_COMMENT = section_comment

    def as_text(self, section):
        """ Format contents of this section for writing to inp file.
            Args:
                section (Section): section of input sequence that contains a list of items in its value attribute
        """
        if section.value or \
            (section.comment and (not hasattr(section, "DEFAULT_COMMENT") or \
                                  section.comment != section.DEFAULT_COMMENT)):
            text_list = []
            if hasattr(section, "SECTION_NAME") and section.SECTION_NAME and section.SECTION_NAME != "Comment":
                text_list.append(section.SECTION_NAME)
            elif hasattr(self, "SECTION_NAME") and self.SECTION_NAME and self.SECTION_NAME != "Comment":
                text_list.append(section.SECTION_NAME)
            if section.comment:
                text_list.append(section.comment)
            if isinstance(section.value, basestring):
                text_list.append(section.value.rstrip('\n'))  # strip any newlines from end of each item
            else:
                for item in section.value:
                    if item is not None:
                        if isinstance(item, basestring):
                            item_str = item
                        else:
                            item_str = self.list_type_writer.as_text(item)
                        # Uncomment below to skip blank items unless they are a blank comment, those are purposely blank
                        # if item_str.strip() or isinstance(item, basestring) or
                        #  (isinstance(item, Section) and item.SECTION_NAME == "Comment"):
                        text_list.append(item_str.rstrip('\n'))  # strip any newlines from end of each item
            return '\n'.join(text_list)
        else:
            return ''
