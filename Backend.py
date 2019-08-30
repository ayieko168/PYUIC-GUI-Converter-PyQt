from PyQt4.QtCore import *
from PyQt4.QtGui import *
from FrontEnd import *
from EditorChoserDialog import *
import os
import subprocess
import json
from time import gmtime, strftime, localtime
import datetime

PathsDict = {}

class EditorDialog(QDialog):

    def __init__(self):

        super().__init__()
        self.EditorUi = Ui_Dialog()
        self.EditorUi.setupUi(self)



class App(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setup
        self.ui.ConvertButton.setEnabled(False)
        self.updatelists()

        # Signal Connections
        self.ui.SearchSourceFileButton.clicked.connect(self.lookForSFile)
        self.ui.SearchDestinationButton.clicked.connect(self.lookForDFile)
        self.ui.DestinationFileEntry.textChanged.connect(self.updateButton)
        self.ui.FileNameEntry.textChanged.connect(self.updateButton)
        self.ui.ConvertButton.clicked.connect(self.convert)
        self.ui.AutoFillCkeck.setChecked(True)
        self.ui.actionSetDefaultEditor.triggered.connect(self.setEditor)
        self.ui.actionResetSources.triggered.connect(self.resetData)
        self.ui.freqCombo.currentIndexChanged.connect(lambda: self.SetEntriesWithSelection(self.ui.freqCombo.currentText()))
        self.ui.recentCombo.currentIndexChanged.connect(lambda: self.SetEntriesWithSelection(self.ui.recentCombo.currentText()))
        


    def setEditor(self):

        dialog = EditorDialog()
        dialog.show()
        dialog.exec_()
    
    def updateButton(self):
        """Update the Convert Button To Disabled Or Enabled"""

        if (len(self.ui.FileNameEntry.text()) >= 2) and (len(self.ui.DestinationFileEntry.text()) >= 2):
            self.ui.ConvertButton.setEnabled(True)
        else:
            self.ui.ConvertButton.setEnabled(False)

    def lookForSFile(self):

        fileName = QFileDialog.getOpenFileNameAndFilter(filter="Design Files (*.ui)")[0]
        self.SetEntriesWithSelection(fileName)
        
    def lookForDFile(self):

        fileName = QFileDialog.getSaveFileName(filter="Python File (*.py)")
        if len(fileName) > 6:
            self.ui.DestinationFileEntry.setText(str(fileName))
        
        self.updateButton()
    
    def addToRecent(self, PathData):

        pass

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
        if exitCode == 0: # Run this code only if exit code is "successful"
            self.ui.statusBar.showMessage("Successfily Converted the UI file", 1000)

            # open the file if 'Open File' option is set
            if self.ui.OpenAfterConvertionCheck.isChecked() == True:
                openCommand = "\"{}\" \"{}\"".format("C:\\Windows\\system32\\notepad.exe", destPath)
                subprocess.call(openCommand)
                print(openCommand)

        print(exitCode)

        self.addToRecent(uiFilePath)
        self.updatelists()

    def updatelists(self):

       pass
   
    def resetData(self):

        with open("Recent_Freq.json", "w") as resetFo:
            json.dump({"Frequently":{}, "Recently":{}}, resetFo, indent=2)
        
    def SetEntriesWithSelection(self, filePath):

        fileName = filePath
        editedFileName = "{}/{}.py".format(os.path.dirname(fileName), os.path.basename(fileName).split(".")[0])

        if len(fileName) > 6:  # Check if the selected filename is valid
            self.ui.FileNameEntry.setText(str(fileName)) # Set Souce Entry Text to File Path
            
            if self.ui.AutoFillCkeck.isChecked() == True:
                self.ui.DestinationFileEntry.setText(str(editedFileName))  # set destination entry text to file path
                self.ui.DestinationFileEntry.setFocus()

                startPos = (len(editedFileName) - len(os.path.basename(fileName)))
                endPos = len(os.path.basename(fileName)) - 3
                self.ui.DestinationFileEntry.setSelection(startPos, endPos)  #  Select th file name for editing
            else:
                pass
            
        else:
            pass
            
        
        self.updateButton()



















from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Backend import *

if __name__ == "__main__":
    
    w = QApplication([])
    app = App()
    app.show()
    w.exec_()