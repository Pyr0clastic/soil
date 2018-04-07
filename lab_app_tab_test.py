import sys
from PyQt5.QtCore import QFileInfo
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

		self.center()
		self.show()

	def center(self):

		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())


class MyTableWidget(QWidget):
	def __init__(self, parent):
		super(QWidget, self).__init__(parent)

		self.layout = QVBoxLayout(self)
		self.tabs = QTabWidget()
		self.tab1 = QWidget()
		self.tabs.resize(300, 200)
		self.tabs.addTab(self.tab1, "Test Tab")

		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)

# class MyTableWidget(QWidget):
#
# 	def __init__(self, parent):
# 		super(QWidget, self).__init__(parent)
# 		self.layout = QVBoxLayout(self)
#
# 		# Initialize tab screen
# 		self.tabs = QTabWidget()
# 		self.tab1 = QWidget()
# 		self.tab2 = QWidget()
# 		self.tabs.resize(300,500)
#
# 		# Add tabs
# 		self.tabs.addTab(self.tab1,"Rohdichte")
# 		self.tabs.addTab(self.tab2,"Tab 2")
#
#
# 		self.layout.addWidget(self.tabs)
# 		self.setLayout(self.layout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
