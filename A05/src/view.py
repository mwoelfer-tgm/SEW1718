# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created: Tue Oct 17 23:50:43 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(769, 339)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.output_ok = QtGui.QLabel(Form)
        self.output_ok.setText("")
        self.output_ok.setObjectName("output_ok")
        self.gridLayout.addWidget(self.output_ok, 5, 0, 1, 1)
        self.button_submit = QtGui.QPushButton(Form)
        self.button_submit.setObjectName("button_submit")
        self.gridLayout.addWidget(self.button_submit, 4, 0, 1, 2)
        self.button_reset = QtGui.QPushButton(Form)
        self.button_reset.setObjectName("button_reset")
        self.gridLayout.addWidget(self.button_reset, 4, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.input_ziel = QtGui.QLineEdit(Form)
        self.input_ziel.setObjectName("input_ziel")
        self.gridLayout.addWidget(self.input_ziel, 2, 1, 1, 3)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.button_close = QtGui.QPushButton(Form)
        self.button_close.setObjectName("button_close")
        self.gridLayout.addWidget(self.button_close, 4, 3, 1, 1)
        self.input_start = QtGui.QLineEdit(Form)
        self.input_start.setObjectName("input_start")
        self.gridLayout.addWidget(self.input_start, 1, 1, 1, 3)
        self.output = QtGui.QTextBrowser(Form)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 3, 0, 1, 4)
        self.mode = QtGui.QCheckBox(Form)
        self.mode.setObjectName("mode")
        self.gridLayout.addWidget(self.mode, 0, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.button_close, QtCore.SIGNAL("clicked()"), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.button_submit.setText(QtGui.QApplication.translate("Form", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.button_reset.setText(QtGui.QApplication.translate("Form", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Ziel:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Start:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Google Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.button_close.setText(QtGui.QApplication.translate("Form", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.mode.setText(QtGui.QApplication.translate("Form", "XML?", None, QtGui.QApplication.UnicodeUTF8))

