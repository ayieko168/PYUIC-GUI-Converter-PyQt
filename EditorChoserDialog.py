# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/PYUIC-GUI-Converter-PyQt/EditorChoserDialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(365, 346)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 290, 331, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 160, 246))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.NotePadRadio = QtGui.QRadioButton(self.verticalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/notepad.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NotePadRadio.setIcon(icon)
        self.NotePadRadio.setIconSize(QtCore.QSize(24, 24))
        self.NotePadRadio.setChecked(True)
        self.NotePadRadio.setObjectName(_fromUtf8("NotePadRadio"))
        self.verticalLayout.addWidget(self.NotePadRadio)
        self.NotePadppCheck = QtGui.QRadioButton(self.verticalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/notepad++.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NotePadppCheck.setIcon(icon1)
        self.NotePadppCheck.setObjectName(_fromUtf8("NotePadppCheck"))
        self.verticalLayout.addWidget(self.NotePadppCheck)
        self.PythonIdleCheck = QtGui.QRadioButton(self.verticalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/idle.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PythonIdleCheck.setIcon(icon2)
        self.PythonIdleCheck.setObjectName(_fromUtf8("PythonIdleCheck"))
        self.verticalLayout.addWidget(self.PythonIdleCheck)
        self.VSCodeCheck = QtGui.QRadioButton(self.verticalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/vscode.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VSCodeCheck.setIcon(icon3)
        self.VSCodeCheck.setObjectName(_fromUtf8("VSCodeCheck"))
        self.verticalLayout.addWidget(self.VSCodeCheck)
        self.VimCheck = QtGui.QRadioButton(self.verticalLayoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/vim.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VimCheck.setIcon(icon4)
        self.VimCheck.setObjectName(_fromUtf8("VimCheck"))
        self.verticalLayout.addWidget(self.VimCheck)
        self.AtomCheck = QtGui.QRadioButton(self.verticalLayoutWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/atom.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AtomCheck.setIcon(icon5)
        self.AtomCheck.setObjectName(_fromUtf8("AtomCheck"))
        self.verticalLayout.addWidget(self.AtomCheck)
        self.MSWordCheck = QtGui.QRadioButton(self.verticalLayoutWidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/word.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MSWordCheck.setIcon(icon6)
        self.MSWordCheck.setObjectName(_fromUtf8("MSWordCheck"))
        self.verticalLayout.addWidget(self.MSWordCheck)
        self.NanoCheck = QtGui.QRadioButton(self.verticalLayoutWidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/nano.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NanoCheck.setIcon(icon7)
        self.NanoCheck.setObjectName(_fromUtf8("NanoCheck"))
        self.verticalLayout.addWidget(self.NanoCheck)
        self.GeditCheck = QtGui.QRadioButton(self.verticalLayoutWidget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/gedit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GeditCheck.setIcon(icon8)
        self.GeditCheck.setIconSize(QtCore.QSize(24, 24))
        self.GeditCheck.setObjectName(_fromUtf8("GeditCheck"))
        self.verticalLayout.addWidget(self.GeditCheck)
        self.SetButton = QtGui.QPushButton(Dialog)
        self.SetButton.setGeometry(QtCore.QRect(234, 210, 81, 41))
        self.SetButton.setObjectName(_fromUtf8("SetButton"))
        self.defaultButton = QtGui.QPushButton(Dialog)
        self.defaultButton.setGeometry(QtCore.QRect(220, 150, 111, 31))
        self.defaultButton.setObjectName(_fromUtf8("defaultButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Editor Chooser", None))
        self.NotePadRadio.setText(_translate("Dialog", "NotePad", None))
        self.NotePadppCheck.setText(_translate("Dialog", "NotePad++", None))
        self.PythonIdleCheck.setText(_translate("Dialog", "Python IDLE", None))
        self.VSCodeCheck.setText(_translate("Dialog", "Visual Studio Code", None))
        self.VimCheck.setText(_translate("Dialog", "Vim", None))
        self.AtomCheck.setText(_translate("Dialog", "Atom", None))
        self.MSWordCheck.setText(_translate("Dialog", "Ms Word", None))
        self.NanoCheck.setText(_translate("Dialog", "Nono", None))
        self.GeditCheck.setText(_translate("Dialog", "Gedit", None))
        self.SetButton.setText(_translate("Dialog", "Set", None))
        self.defaultButton.setText(_translate("Dialog", "Reset To Default", None))

