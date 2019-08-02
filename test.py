# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/PYUIC-GUI-Converter-PyQt/test.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(544, 293)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.FileNameLabel = QtGui.QLabel(self.centralwidget)
        self.FileNameLabel.setGeometry(QtCore.QRect(10, 50, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FileNameLabel.setFont(font)
        self.FileNameLabel.setIndent(30)
        self.FileNameLabel.setObjectName(_fromUtf8("FileNameLabel"))
        self.DestinationFileLabel = QtGui.QLabel(self.centralwidget)
        self.DestinationFileLabel.setGeometry(QtCore.QRect(10, 110, 101, 21))
        self.DestinationFileLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DestinationFileLabel.setIndent(5)
        self.DestinationFileLabel.setObjectName(_fromUtf8("DestinationFileLabel"))
        self.DestinationFileEntry = QtGui.QLineEdit(self.centralwidget)
        self.DestinationFileEntry.setGeometry(QtCore.QRect(120, 110, 341, 21))
        self.DestinationFileEntry.setObjectName(_fromUtf8("DestinationFileEntry"))
        self.SearchSourceFileButton = QtGui.QPushButton(self.centralwidget)
        self.SearchSourceFileButton.setGeometry(QtCore.QRect(470, 50, 51, 23))
        self.SearchSourceFileButton.setObjectName(_fromUtf8("SearchSourceFileButton"))
        self.SearchDestinationButton = QtGui.QPushButton(self.centralwidget)
        self.SearchDestinationButton.setGeometry(QtCore.QRect(470, 110, 51, 23))
        self.SearchDestinationButton.setObjectName(_fromUtf8("SearchDestinationButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 451, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 160, 416, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ExecutableCheck = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.ExecutableCheck.setObjectName(_fromUtf8("ExecutableCheck"))
        self.verticalLayout.addWidget(self.ExecutableCheck)
        self.AutoFillCkeck = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.AutoFillCkeck.setStatusTip(_fromUtf8(""))
        self.AutoFillCkeck.setWhatsThis(_fromUtf8(""))
        self.AutoFillCkeck.setObjectName(_fromUtf8("AutoFillCkeck"))
        self.verticalLayout.addWidget(self.AutoFillCkeck)
        self.OpenAfterConvertionCheck = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.OpenAfterConvertionCheck.setToolTip(_fromUtf8(""))
        self.OpenAfterConvertionCheck.setObjectName(_fromUtf8("OpenAfterConvertionCheck"))
        self.verticalLayout.addWidget(self.OpenAfterConvertionCheck)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(173, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ConvertButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ConvertButton.setFont(font)
        self.ConvertButton.setObjectName(_fromUtf8("ConvertButton"))
        self.horizontalLayout.addWidget(self.ConvertButton)
        self.FileNameEntry = QtGui.QLineEdit(self.centralwidget)
        self.FileNameEntry.setGeometry(QtCore.QRect(120, 50, 341, 21))
        self.FileNameEntry.setObjectName(_fromUtf8("FileNameEntry"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 544, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Vrinda"))
        font.setPointSize(10)
        self.statusBar.setFont(font)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyuic GUI", None))
        self.FileNameLabel.setText(_translate("MainWindow", "Source File", None))
        self.DestinationFileLabel.setText(_translate("MainWindow", "Destination", None))
        self.DestinationFileEntry.setToolTip(_translate("MainWindow", "<html><head/><body><p>Full path to the destination</p></body></html>", None))
        self.DestinationFileEntry.setStatusTip(_translate("MainWindow", "Enter The full path to the destination of the converted python file", None))
        self.SearchSourceFileButton.setText(_translate("MainWindow", "Search", None))
        self.SearchDestinationButton.setText(_translate("MainWindow", "Search", None))
        self.label.setText(_translate("MainWindow", "Convert A Ui file to a Python File", None))
        self.ExecutableCheck.setStatusTip(_translate("MainWindow", "If Enabled Adds some Code to Make The Converted Ui File Executable", None))
        self.ExecutableCheck.setWhatsThis(_translate("MainWindow", "Adds lines of code to make the file executable", None))
        self.ExecutableCheck.setText(_translate("MainWindow", "Executable", None))
        self.AutoFillCkeck.setText(_translate("MainWindow", "Auto Fill Destination", None))
        self.OpenAfterConvertionCheck.setStatusTip(_translate("MainWindow", "Open The Python File In a Text Editor After Convertion Is complete", None))
        self.OpenAfterConvertionCheck.setWhatsThis(_translate("MainWindow", "Adds lines of code to make the file executable", None))
        self.OpenAfterConvertionCheck.setText(_translate("MainWindow", "Open After Convertion", None))
        self.ConvertButton.setText(_translate("MainWindow", "Convert", None))
        self.FileNameEntry.setToolTip(_translate("MainWindow", "Full path to the destination", None))
        self.FileNameEntry.setStatusTip(_translate("MainWindow", "Enter The full path to the destination of the converted python file", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

