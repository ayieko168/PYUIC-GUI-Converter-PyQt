# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/PYUIC-GUI-Converter-PyQt/FrontEnd.ui'
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
        MainWindow.resize(557, 375)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/mainIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 250, 416, 80))
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
        spacerItem = QtGui.QSpacerItem(70, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ConvertButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.ConvertButton.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ConvertButton.setFont(font)
        self.ConvertButton.setObjectName(_fromUtf8("ConvertButton"))
        self.horizontalLayout.addWidget(self.ConvertButton)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 541, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.recentCombo = QtGui.QComboBox(self.groupBox)
        self.recentCombo.setGeometry(QtCore.QRect(80, 50, 341, 22))
        self.recentCombo.setObjectName(_fromUtf8("recentCombo"))
        self.FileNameEntry = QtGui.QLineEdit(self.groupBox)
        self.FileNameEntry.setGeometry(QtCore.QRect(80, 20, 341, 21))
        self.FileNameEntry.setObjectName(_fromUtf8("FileNameEntry"))
        self.SearchSourceFileButton = QtGui.QPushButton(self.groupBox)
        self.SearchSourceFileButton.setGeometry(QtCore.QRect(460, 50, 71, 31))
        self.SearchSourceFileButton.setObjectName(_fromUtf8("SearchSourceFileButton"))
        self.DestinationFileLabel_2 = QtGui.QLabel(self.groupBox)
        self.DestinationFileLabel_2.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.DestinationFileLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DestinationFileLabel_2.setIndent(5)
        self.DestinationFileLabel_2.setObjectName(_fromUtf8("DestinationFileLabel_2"))
        self.DestinationFileLabel_3 = QtGui.QLabel(self.groupBox)
        self.DestinationFileLabel_3.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.DestinationFileLabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DestinationFileLabel_3.setIndent(5)
        self.DestinationFileLabel_3.setObjectName(_fromUtf8("DestinationFileLabel_3"))
        self.DestinationFileLabel_4 = QtGui.QLabel(self.groupBox)
        self.DestinationFileLabel_4.setGeometry(QtCore.QRect(10, 80, 61, 21))
        self.DestinationFileLabel_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DestinationFileLabel_4.setIndent(5)
        self.DestinationFileLabel_4.setObjectName(_fromUtf8("DestinationFileLabel_4"))
        self.freqCombo = QtGui.QComboBox(self.groupBox)
        self.freqCombo.setGeometry(QtCore.QRect(80, 80, 341, 22))
        self.freqCombo.setObjectName(_fromUtf8("freqCombo"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(430, 20, 20, 81))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 541, 71))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.SearchDestinationButton = QtGui.QPushButton(self.groupBox_2)
        self.SearchDestinationButton.setGeometry(QtCore.QRect(470, 22, 61, 31))
        self.SearchDestinationButton.setObjectName(_fromUtf8("SearchDestinationButton"))
        self.DestinationFileEntry = QtGui.QLineEdit(self.groupBox_2)
        self.DestinationFileEntry.setGeometry(QtCore.QRect(80, 20, 361, 21))
        self.DestinationFileEntry.setObjectName(_fromUtf8("DestinationFileEntry"))
        self.DestinationFileLabel_5 = QtGui.QLabel(self.groupBox_2)
        self.DestinationFileLabel_5.setGeometry(QtCore.QRect(0, 20, 71, 21))
        self.DestinationFileLabel_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DestinationFileLabel_5.setIndent(5)
        self.DestinationFileLabel_5.setObjectName(_fromUtf8("DestinationFileLabel_5"))
        self.line_2 = QtGui.QFrame(self.groupBox_2)
        self.line_2.setGeometry(QtCore.QRect(440, 20, 20, 31))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuFrequentFiles = QtGui.QMenu(self.menubar)
        self.menuFrequentFiles.setObjectName(_fromUtf8("menuFrequentFiles"))
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
        self.actionSetDefaultEditor = QtGui.QAction(MainWindow)
        self.actionSetDefaultEditor.setObjectName(_fromUtf8("actionSetDefaultEditor"))
        self.actionFrequentFiles = QtGui.QAction(MainWindow)
        self.actionFrequentFiles.setObjectName(_fromUtf8("actionFrequentFiles"))
        self.actionRecentFiles = QtGui.QAction(MainWindow)
        self.actionRecentFiles.setObjectName(_fromUtf8("actionRecentFiles"))
        self.actionResetSources = QtGui.QAction(MainWindow)
        self.actionResetSources.setObjectName(_fromUtf8("actionResetSources"))
        self.menuFile.addAction(self.actionSetDefaultEditor)
        self.menuFile.addAction(self.actionExit)
        self.menuFrequentFiles.addAction(self.actionFrequentFiles)
        self.menuFrequentFiles.addAction(self.actionRecentFiles)
        self.menuFrequentFiles.addSeparator()
        self.menuFrequentFiles.addAction(self.actionResetSources)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFrequentFiles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyuic GUI", None))
        self.label.setText(_translate("MainWindow", "Convert A Ui file to a Python File", None))
        self.ExecutableCheck.setStatusTip(_translate("MainWindow", "If Enabled Adds some Code to Make The Converted Ui File Executable", None))
        self.ExecutableCheck.setWhatsThis(_translate("MainWindow", "Adds lines of code to make the file executable", None))
        self.ExecutableCheck.setText(_translate("MainWindow", "Executable", None))
        self.AutoFillCkeck.setText(_translate("MainWindow", "Auto Fill Destination", None))
        self.OpenAfterConvertionCheck.setStatusTip(_translate("MainWindow", "Open The Python File In a Text Editor After Convertion Is complete", None))
        self.OpenAfterConvertionCheck.setWhatsThis(_translate("MainWindow", "Adds lines of code to make the file executable", None))
        self.OpenAfterConvertionCheck.setText(_translate("MainWindow", "Open After Convertion", None))
        self.ConvertButton.setText(_translate("MainWindow", "Convert", None))
        self.ConvertButton.setShortcut(_translate("MainWindow", "Return", None))
        self.groupBox.setTitle(_translate("MainWindow", "Source", None))
        self.FileNameEntry.setToolTip(_translate("MainWindow", "Full path to the destination", None))
        self.FileNameEntry.setStatusTip(_translate("MainWindow", "Enter The full path to the destination of the converted python file", None))
        self.SearchSourceFileButton.setText(_translate("MainWindow", "Search", None))
        self.DestinationFileLabel_2.setText(_translate("MainWindow", "Recent", None))
        self.DestinationFileLabel_3.setText(_translate("MainWindow", "File Path", None))
        self.DestinationFileLabel_4.setText(_translate("MainWindow", "Frequent", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Destination", None))
        self.SearchDestinationButton.setText(_translate("MainWindow", "Search", None))
        self.DestinationFileEntry.setToolTip(_translate("MainWindow", "<html><head/><body><p>Full path to the destination</p></body></html>", None))
        self.DestinationFileEntry.setStatusTip(_translate("MainWindow", "Enter The full path to the destination of the converted python file", None))
        self.DestinationFileLabel_5.setText(_translate("MainWindow", "File Path", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuFrequentFiles.setTitle(_translate("MainWindow", "Sources", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionSetDefaultEditor.setText(_translate("MainWindow", "Set Default Editor", None))
        self.actionSetDefaultEditor.setToolTip(_translate("MainWindow", "Set Default Editor That opens the converted file", None))
        self.actionFrequentFiles.setText(_translate("MainWindow", "Frequent Files", None))
        self.actionRecentFiles.setText(_translate("MainWindow", "Resent Files", None))
        self.actionResetSources.setText(_translate("MainWindow", "Reset Sources", None))

