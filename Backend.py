from PyQt5.QtWidgets import *
from FrontEnd import *
from EditorChoserDialog import *
import os
import subprocess
import json
from time import localtime, asctime, time

PathsDict = {}
editor= "C:\\Windows\\system32\\notepad.exe"

class EditorDialog(QDialog):

    def __init__(self):

        super().__init__()
        self.EditorUi = Ui_Dialog()
        self.EditorUi.setupUi(self)

        self.change = False

        self.EditorUi.restoreDefaultButton.clicked.connect(self.restoreToDefault)
        self.EditorUi.SetButton.clicked.connect(self.SetButtonCMD)
        self.EditorUi.NotePadRadio.clicked.connect(self.ChangeSelectedEditor)
        self.EditorUi.NotePadppCheck.clicked.connect(self.ChangeSelectedEditor)
        self.EditorUi.PythonIdleCheck.clicked.connect(self.ChangeSelectedEditor)
        self.EditorUi.VSCodeCheck.clicked.connect(self.ChangeSelectedEditor)
        self.EditorUi.VimCheck.clicked.connect(self.ChangeSelectedEditor)
        self.EditorUi.AtomCheck.clicked.connect(self.ChangeSelectedEditor)
        self.EditorUi.MSWordCheck.clicked.connect(self.ChangeSelectedEditor)
        self.EditorUi.NanoCheck.clicked.connect(self.ChangeSelectedEditor)
        self.EditorUi.GeditCheck.clicked.connect(self.ChangeSelectedEditor)

    
    def MessageBox(self, message="This is a message box", icon=QMessageBox.Information, addItionalInfo="This is additional information", windowTitle="MessageBox demo"):

        msg = QMessageBox()
        msg.setIcon()
        msg.setText(message)
        msg.setInformativeText(addItionalInfo)
        msg.setWindowTitle(windowTitle)
        msg.setDetailedText(addItionalInfo)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.msgBoxButtonCMD)
        retval = msg.exec_()

    def msgBoxButtonCMD(self, i):
            print ("Button pressed is:",i.text())
    
    def restoreToDefault(self):

        self.EditorUi.NotePadRadio.setChecked(True)
    
    def SetButtonCMD(self):

        print("set")
    
    def ChangeSelectedEditor(self):

        global editor
        login = os.getlogin()

        if self.EditorUi.NotePadRadio.isChecked() == True:
            editor= "C:\\Windows\\system32\\notepad.exe"
        elif self.EditorUi.NotePadppCheck.isChecked() == True:
            editor= "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
        elif self.EditorUi.PythonIdleCheck.isChecked() == True:
            editor= "C:\\Users\\{}\\AppData\\Local\\Programs\\Python\\Python37\\pythonw.exe".format(login)
        elif self.EditorUi.VSCodeCheck.isChecked() == True:
            editor= "VSCode"
        elif self.EditorUi.VimCheck.isChecked() == True:
            editor= "Vim"
        elif self.EditorUi.AtomCheck.isChecked() == True:
            editor= "Atom"
        elif self.EditorUi.MSWordCheck.isChecked() == True:
            editor= "MSWord"
        elif self.EditorUi.NanoCheck.isChecked() == True:
            editor= "Nano"
        elif self.EditorUi.GeditCheck.isChecked() == True:
            editor= "Gedit"
        
        
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

        fileName = QFileDialog.getOpenFileName(filter="Design Files (*.ui)")[0]
        self.SetEntriesWithSelection(fileName)
        
    def lookForDFile(self):

        fileName = QFileDialog.getSaveFileName(filter="Python File (*.py)")
        if len(fileName) > 6:
            self.ui.DestinationFileEntry.setText(str(fileName))
        
        self.updateButton()
    
    def addToDataBase(self, PathData):

        curentNormalTime = asctime(localtime(time()))
        currentUnixTime = time()
        freqCount = 1

        with open("Recent_Freq.json", "r") as addFoR:
            wholeDataBase = json.load(addFoR)
            freqDataDict = wholeDataBase["Frequently"]
            recentDataDict = wholeDataBase["Recently"]
        
        #### Frequently
        # if len(freqDataDict.items()) > 0: # if there are items in the freq dict...
        #     for key, value in freqDataDict.items():
        #         print(value)
        #         if PathData not in value: # if the item is NOT in the dictionary
        #             freqDataDict[freqCount] = [PathData, curentNormalTime, currentUnixTime]
        #             break
        #         else: # if the item is in one of the items
        #             del freqDataDict[key]
        #             freqDataDict[(int(key)+1)] = [PathData, curentNormalTime, currentUnixTime]
        #             break
        
        # else: # if the freq dict has NO items...
        #     print("empty")
        #     freqDataDict[freqCount] = [PathData, curentNormalTime, currentUnixTime]

        

        with open("Recent_Freq.json", "w") as addFoW:
            json.dump(wholeDataBase, addFoW, indent=2)

    def convert(self):

        global editor

        login = os.getlogin()
        uiFilePath = self.ui.FileNameEntry.text()
        destPath = self.ui.DestinationFileEntry.text()
        args = ""

        if self.ui.ExecutableCheck.isChecked() == True:
            args = "-x"
        else:
            args = ""
        
        command = "pyuic5 {} \"{}\" -o \"{}\"".format(args, uiFilePath, destPath)

        self.ui.statusBar.showMessage("Converting...", 1000)

        exitCode = subprocess.call(command)
        if exitCode == 0: # Run this code only if exit code is "successful"
            self.ui.statusBar.showMessage("Successfily Converted the UI file (exitCode: {})".format(exitCode), 1000)

            # open the file if 'Open File' option is set
            if self.ui.OpenAfterConvertionCheck.isChecked() == True:
                openCommand = "\"{}\" \"{}\"".format(editor, destPath)
                subprocess.call(openCommand)
                print(openCommand)

        self.addToDataBase(uiFilePath)
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


if __name__ == "__main__":
    
    w = QApplication([])
    app = App()
    app.show()
    w.exec_()

