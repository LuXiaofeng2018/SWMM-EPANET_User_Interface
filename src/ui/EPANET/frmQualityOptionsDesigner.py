# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\Python\dev-ui\src\ui\EPANET\frmQualityOptions.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmQualityOptions(object):
    def setupUi(self, frmQualityOptions):
        frmQualityOptions.setObjectName(_fromUtf8("frmQualityOptions"))
        frmQualityOptions.resize(283, 318)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmQualityOptions.setFont(font)
        self.centralWidget = QtGui.QWidget(frmQualityOptions)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.lblChemicalName = QtGui.QLabel(self.centralWidget)
        self.lblChemicalName.setGeometry(QtCore.QRect(20, 110, 101, 16))
        self.lblChemicalName.setObjectName(_fromUtf8("lblChemicalName"))
        self.lblMassUnits = QtGui.QLabel(self.centralWidget)
        self.lblMassUnits.setGeometry(QtCore.QRect(20, 140, 111, 16))
        self.lblMassUnits.setObjectName(_fromUtf8("lblMassUnits"))
        self.cmdOK = QtGui.QPushButton(self.centralWidget)
        self.cmdOK.setGeometry(QtCore.QRect(50, 260, 75, 23))
        self.cmdOK.setObjectName(_fromUtf8("cmdOK"))
        self.cmdCancel = QtGui.QPushButton(self.centralWidget)
        self.cmdCancel.setGeometry(QtCore.QRect(150, 260, 75, 23))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.txtMassUnits = QtGui.QLineEdit(self.centralWidget)
        self.txtMassUnits.setGeometry(QtCore.QRect(150, 140, 113, 20))
        self.txtMassUnits.setObjectName(_fromUtf8("txtMassUnits"))
        self.lblDiffusivity = QtGui.QLabel(self.centralWidget)
        self.lblDiffusivity.setGeometry(QtCore.QRect(20, 170, 111, 16))
        self.lblDiffusivity.setObjectName(_fromUtf8("lblDiffusivity"))
        self.txtDiffusivity = QtGui.QLineEdit(self.centralWidget)
        self.txtDiffusivity.setGeometry(QtCore.QRect(150, 170, 113, 20))
        self.txtDiffusivity.setObjectName(_fromUtf8("txtDiffusivity"))
        self.lblTraceNode = QtGui.QLabel(self.centralWidget)
        self.lblTraceNode.setGeometry(QtCore.QRect(20, 200, 111, 16))
        self.lblTraceNode.setObjectName(_fromUtf8("lblTraceNode"))
        self.txtTraceNode = QtGui.QLineEdit(self.centralWidget)
        self.txtTraceNode.setGeometry(QtCore.QRect(150, 200, 113, 20))
        self.txtTraceNode.setObjectName(_fromUtf8("txtTraceNode"))
        self.lblTolerance = QtGui.QLabel(self.centralWidget)
        self.lblTolerance.setGeometry(QtCore.QRect(20, 230, 111, 16))
        self.lblTolerance.setObjectName(_fromUtf8("lblTolerance"))
        self.txtTolerance = QtGui.QLineEdit(self.centralWidget)
        self.txtTolerance.setGeometry(QtCore.QRect(150, 230, 113, 20))
        self.txtTolerance.setObjectName(_fromUtf8("txtTolerance"))
        self.txtChemicalName = QtGui.QLineEdit(self.centralWidget)
        self.txtChemicalName.setGeometry(QtCore.QRect(150, 110, 113, 20))
        self.txtChemicalName.setObjectName(_fromUtf8("txtChemicalName"))
        self.gbxQuality = QtGui.QGroupBox(self.centralWidget)
        self.gbxQuality.setGeometry(QtCore.QRect(20, 10, 241, 91))
        self.gbxQuality.setObjectName(_fromUtf8("gbxQuality"))
        self.cbxNone = QtGui.QCheckBox(self.gbxQuality)
        self.cbxNone.setGeometry(QtCore.QRect(30, 30, 70, 17))
        self.cbxNone.setObjectName(_fromUtf8("cbxNone"))
        self.cbxChemical = QtGui.QCheckBox(self.gbxQuality)
        self.cbxChemical.setGeometry(QtCore.QRect(30, 60, 70, 17))
        self.cbxChemical.setObjectName(_fromUtf8("cbxChemical"))
        self.cbxAge = QtGui.QCheckBox(self.gbxQuality)
        self.cbxAge.setGeometry(QtCore.QRect(130, 30, 70, 17))
        self.cbxAge.setObjectName(_fromUtf8("cbxAge"))
        self.cbxTrace = QtGui.QCheckBox(self.gbxQuality)
        self.cbxTrace.setGeometry(QtCore.QRect(130, 60, 70, 17))
        self.cbxTrace.setObjectName(_fromUtf8("cbxTrace"))
        frmQualityOptions.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(frmQualityOptions)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        frmQualityOptions.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(frmQualityOptions)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        frmQualityOptions.setStatusBar(self.statusBar)

        self.retranslateUi(frmQualityOptions)
        QtCore.QMetaObject.connectSlotsByName(frmQualityOptions)

    def retranslateUi(self, frmQualityOptions):
        frmQualityOptions.setWindowTitle(_translate("frmQualityOptions", "EPANET Quality Options", None))
        self.lblChemicalName.setText(_translate("frmQualityOptions", "<html><head/><body><p>Chemical Name</p></body></html>", None))
        self.lblMassUnits.setText(_translate("frmQualityOptions", "Mass Units", None))
        self.cmdOK.setText(_translate("frmQualityOptions", "OK", None))
        self.cmdCancel.setText(_translate("frmQualityOptions", "Cancel", None))
        self.lblDiffusivity.setText(_translate("frmQualityOptions", "Relative Diffusivity", None))
        self.lblTraceNode.setText(_translate("frmQualityOptions", "Trace Node", None))
        self.lblTolerance.setText(_translate("frmQualityOptions", "Quality Tolerance", None))
        self.gbxQuality.setTitle(_translate("frmQualityOptions", "Analysis Type", None))
        self.cbxNone.setText(_translate("frmQualityOptions", "None", None))
        self.cbxChemical.setText(_translate("frmQualityOptions", "Chemical", None))
        self.cbxAge.setText(_translate("frmQualityOptions", "Age", None))
        self.cbxTrace.setText(_translate("frmQualityOptions", "Trace", None))

