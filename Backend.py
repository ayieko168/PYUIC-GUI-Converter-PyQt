from PyQt4.QtCore import *
from PyQt4.QtGui import *
from FrontEnd import *
import os
import subprocess


class App(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setup
        self.ui.ConvertButton.setEnabled(False)

        # Signal Connections
        self.ui.SearchSourceFileButton.clicked.connect(self.lookForSFile)
        self.ui.SearchDestinationButton.clicked.connect(self.lookForDFile)
        self.ui.DestinationFileEntry.textChanged.connect(self.updateButton)
        self.ui.FileNameEntry.textChanged.connect(self.updateButton)
        self.ui.ConvertButton.clicked.connect(self.convert)

    
    def updateButton(self):
        """Update the Convert Button To Disabled Or Enabled"""

        if (len(self.ui.FileNameEntry.text()) >= 2) and (len(self.ui.DestinationFileEntry.text()) >= 2):
            self.ui.ConvertButton.setEnabled(True)
        else:
            self.ui.ConvertButton.setEnabled(False)

    def lookForSFile(self):

        fileName = QFileDialog.getOpenFileNameAndFilter(filter="Design Files (*.ui)")[0]
        editedFileName = "{}/{}.py".format(os.path.dirname(fileName), os.path.basename(fileName).split(".")[0])

        if len(fileName) > 6:
            self.ui.FileNameEntry.setText(str(fileName))
            self.ui.DestinationFileEntry.setText(str(editedFileName))
            self.ui.DestinationFileEntry.setFocus()
            
            startPos = (len(editedFileName) - len(os.path.basename(fileName)))
            endPos = len(os.path.basename(fileName)) - 3
            self.ui.DestinationFileEntry.setSelection(startPos, endPos)
        
        self.updateButton()
        
    def lookForDFile(self):

        fileName = QFileDialog.getSaveFileName(filter="Python File (*.py)")
        if len(fileName) > 6:
            self.ui.DestinationFileEntry.setText(str(fileName))
        
        self.updateButton()
    
    def convert(self):

        login = os.getlogin()
        pythonPath = "C:\\Users\\{}\\AppData\\Local\\Programs\\Python\\Python37\\python.exe".format(login)
        pyuicPath = "C:\\Users\\{}\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\PyQt4\\uic\\pyuic.py".format(login)
        uiFilePath = self.ui.FileNameEntry.text()
        destPath = self.ui.DestinationFileEntry.text()
        args = ""

        if self.ui.ExecutableCheck.isChecked() == True:
            args = "-x"
        else:
            args = ""
        
        command = "\"{}\" \"{}\" {} \"{}\" -o \"{}\"".format(pythonPath, pyuicPath, args, uiFilePath, destPath)

        self.ui.statusBar.showMessage("Converting...", 1000)
        exitCode = subprocess.call(command)
        if exitCode == 0:
            self.ui.statusBar.showMessage("Successfily Converted the UI file", 1000)

        print(exitCode)