from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Backend import *

if __name__ == "__main__":
    
    w = QApplication([])
    app = App()
    app.show()
    w.exec_()