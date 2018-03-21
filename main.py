#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
#from PyQt5.QtGui import QKeySequence
from design import *
import sys




class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        #reg_ex = QRegExp("[0-9]+.?[0-9]{,2}")
        #input_validator = QRegExpValidator(reg_ex, self.lineEdit)
        #self.lineEdit.setValidator(input_validator)






def main():
    import sys
    app = QApplication(sys.argv)
    instance = Main()
    #instance.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
