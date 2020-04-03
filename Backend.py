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
        # exitCode = 0
        if exitCode == 0: # Run this code only if exit code is "successful"
            self.ui.statusBar.showMessage("Successfily Converted the UI file (exitCode: {})".format(exitCode), 1000)
            self.addDirectory(uiFilePath)

            # open the file if 'Open File' option is set
            if self.ui.OpenAfterConvertionCheck.isChecked() == True:
                openCommand = "\"{}\" \"{}\"".format(editor, destPath)
                subprocess.call(openCommand)
                print(openCommand)

        self.updatelists()

    def updatelists(self):
        
        with open("Recent_Freq.json", "r") as recents_FO:
            data = json.load(recents_FO)
        
        all_db = data["All"]
        freq_db = data["Frequently"]
        recent_db = data["Recently"]
        
        
        ## Reset The Combo Boxes
        for i in range(20):
            self.ui.freqCombo.removeItem(i)
        for j in range(20):
            self.ui.recentCombo.removeItem(j)

        ## Update ComboBoxes With current data
        self.ui.freqCombo.addItems(freq_db)
        self.ui.recentCombo.addItems(recent_db)

    def resetData(self):

        with open("Recent_Freq.json", "w") as resetFo:
            json.dump({"Frequently":[], "Recently":[], "All":{}}, resetFo, indent=2)
        
        self.updatelists()
        
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

    def addDirectory(self, path):
        
        with open("Recent_Freq.json", "r") as recents_db:
            data = json.load(recents_db)
    
        all_db = data["All"]

        if path not in all_db.keys():
            print(f"adding {path} to db not available")
            all_db[path] = [1, time()]
        else:
            print(f"updating count as {path} is already aval in db")
            all_db[path][0]+=1
            all_db[path][1] = time()
        

        
        with open("Recent_Freq.json", "w") as recents_db:
            data["Frequently"] = []
            data["Recently"] = []
            json.dump(data, recents_db, indent=2)

        freq_db = data["Frequently"]
        recent_db = data["Recently"]

        ## update freq and recent data from all db
        freq_check_val = 0
        recent_check_val = 0

        for k, v in all_db.items():
            # frequency
            if v[0] >= freq_check_val:
                freq_check_val = v[0]
                if k not in freq_db:
                    freq_db.insert(0, k)
            else:
                if k not in freq_db:
                    freq_db.insert(-1, k)

        for k2, v2 in all_db.items():
            # recent
            if v2[1] >= recent_check_val:
                recent_check_val = v2[1]
                if k2 not in recent_db:
                    recent_db.insert(0, k2)
            else:
                if k2 not in recent_db:
                    recent_db.insert(-1, k2)

        with open("Recent_Freq.json", "w") as recents_db:
            json.dump(data, recents_db, indent=2)







if __name__ == "__main__":
    
    w = QApplication([])
    app = App()
    app.show()
    w.exec_()

