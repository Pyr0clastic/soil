import sys
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Physiogeo - Laborapp'
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 500
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        #self.ScreenCenter.center()
        self.show()



class ScreenCenter(QDesktopWidget):

    def __init__(self):
        super(QDesktopWidget, self).__init__(ScreenCenter)

    def center(self):
        qr = self.frameGeometry()
        cp = QWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft)


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,500)

        # Add tabs
        self.tabs.addTab(self.tab1,"Rohdichte")
        self.tabs.addTab(self.tab2,"Tab 2")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

		# Second tab (my try)
        self.tab2.layout = QVBoxLayout(self)
        self.pushButton2 = QPushButton("Exit")
        self.tab2.layout.addWidget(self.pushButton2)
        self.tab2.setLayout(self.tab2.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
