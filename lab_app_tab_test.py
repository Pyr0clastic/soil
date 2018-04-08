import sys
from PyQt5.QtCore import QFileInfo, QRect
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QDesktopWidget, QMessageBox, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

	def __init__(self):
		super().__init__()
		self.title = 'Terra Status'
		self.left = 0
		self.top = 0
		self.width = 500
		self.height = 500
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.setWindowIcon(QIcon('test_icon.png'))


		self.table_widget = MyTableWidget(self)
		self.setCentralWidget(self.table_widget)


		self.createActions()
		self.createMenus()
		self.center()
		self.show()

	def center(self):

		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def createActions(self):
		self.aboutAct = QAction("&About", self,
				statusTip="Show the application's About box",
				triggered=self.about)

		self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                statusTip="Exit the application", triggered=self.close)

		self.aboutQtAct = QAction("About &Qt", self)
		self.aboutQtAct.triggered.connect(QApplication.instance().aboutQt)


	def createMenus(self):
		self.helpMenu = self.menuBar().addMenu("&Help")
		self.helpMenu.addAction(self.aboutAct)
		self.helpMenu.addAction(self.aboutQtAct)
		self.fileMenu = self.menuBar().addMenu("&File")
		self.fileMenu.addAction(self.exitAct)

	def about(self):
		QMessageBox.about(self, "About Menu",
				"The <b>Menu</b> example shows how to create menu-bar menus "
				"and context menus.")


class MyTableWidget(QWidget):
	def __init__(self, parent):
		super(QWidget, self).__init__(parent)

		self.layout = QVBoxLayout(self)
		self.tabs = QTabWidget()
		self.tabs.setMovable(True)
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tab3 = QWidget()
		self.tab4 = QWidget()
		self.tabs.resize(300, 200)
		self.tabs.addTab(self.tab1, "Rohdichte")
		self.tabs.addTab(self.tab2, "Wkmax")
		self.tabs.addTab(self.tab3, "Feststoffdichte")
		self.tabs.addTab(self.tab4, "Organische Substanz")


		####################### Rohdichte TAB ################
		self.lbl_rd_1 = QLabel(self.tab1)
		self.lbl_rd_1.setGeometry(QRect(40, 45, 151, 17))
		self.lbl_rd_1.setText("Masse der Probe frisch:")

		self.lbl_rd_2 = QLabel(self.tab1)
		self.lbl_rd_2.setGeometry(QRect(40, 85, 161, 17))
		self.lbl_rd_2.setText("Masser der Probe trocken:")

		self.lbl_rd_3 = QLabel(self.tab1)
		self.lbl_rd_3.setGeometry(QRect(40, 125, 180, 17))
		self.lbl_rd_3.setText("Volumen des Stechzylinders:")

		self.txt_rd_fresh = QLineEdit(self.tab1)
		self.txt_rd_fresh.setGeometry(QRect(260, 40, 141, 27))
		#self.txt_rd_fresh.setText("")
		self.txt_rd_fresh.setToolTip("Angabe in g")

		self.txt_rd_dry = QLineEdit(self.tab1)
		self.txt_rd_dry.setGeometry(QRect(260, 80, 141, 27))
		#self.txt_rd_dry.setText("")
		self.txt_rd_dry.setToolTip("Angabe in g")

		self.txt_rd_vol = QLineEdit(self.tab1)
		self.txt_rd_vol.setGeometry(QRect(260, 120, 141, 27))
		self.txt_rd_vol.setToolTip("Angabe in g/cm\u00B3")

		self.lbl_rd_4 = QLabel(self.tab1)
		self.lbl_rd_4.setGeometry(QRect(40, 200, 120, 17))
		self.lbl_rd_4.setText("Blub")

		self.lbl_rd_dry2 = QLabel(self.tab1)
		self.lbl_rd_dry2.setGeometry(QRect(40, 240, 120, 17))
		self.lbl_rd_dry2.setText("HaHa")

		self.btn_rd_Calc = QPushButton(self.tab1)
		self.btn_rd_Calc.setGeometry(QRect(280, 270, 100, 30))
		self.btn_rd_Calc.setText("Berechnen")

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
