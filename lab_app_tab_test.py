import sys
from PyQt5.QtCore import QFileInfo, QRect, QRegExp
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QDesktopWidget, QMessageBox, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):
	def __init__(self):
		super().__init__()
		self.title = 'Terra Status'
		self.left = 0
		self.top = 0
		self.width = 600
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

		self.table_widget.btn_rd_Calc.clicked.connect(self.Input_none)
		self.table_widget.btn_wkmax_calc.clicked.connect(self.Input_none2)

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

	def Input_none(self):
		try:
			self.rohdichte()
		except ValueError:
			return(QMessageBox.warning(None, 'Error', 'Fehlende Parameter zur Berechnung!'))

	def Input_none2(self):
		try:
			self.wkmax()
		except ValueError:
			return(QMessageBox.warning(None, 'Error', 'Fehlende Parameter zur Berechnung!'))

	def rohdichte(self):
		masse_frisch = float(self.table_widget.txt_rd_fresh.text())
		masse_trocken = float(self.table_widget.txt_rd_dry.text())
		stechzyl_Volumen = float(self.table_widget.txt_rd_vol.text())
		global rd_wet
		rd_wet = str(round((masse_frisch/stechzyl_Volumen),4))
		rd_dry = str(round((masse_trocken/stechzyl_Volumen),4))
		self.table_widget.lbl_rd_res_fresh.setText(rd_wet + g_cm3)
		self.table_widget.lbl_rd_res_dry.setText(rd_dry + g_cm3)
		#self.txt_festD_rohDry.setText(rd_dry)


	def wkmax(self):
		masse_atro = float(self.table_widget.txt_wkmax_atro.text())
		masse_wkmax = float(self.table_widget.txt_wkmax_wkmax.text())
		stechzyl_Volumen = float(self.table_widget.txt_wkmax_Zylinder.text())
		res_wkmax = round((((masse_wkmax - masse_atro)/stechzyl_Volumen)*100),2)
		global wkmax
		wkmax = str(res_wkmax)
		self.table_widget.lbl_wkmax_Result.setText(wkmax + vol)

	reg_ex = QRegExp("[0-9]+\.[0-9]+")
	input_validator = QRegExpValidator(reg_ex)




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


		global vol
		global g_cm3
		global rd_dry          # temporary test for feststoffdichte
		rd_dry = None           # temprory test for feststoffdichte
		vol = " % Vol."
		g_cm3 = " g/cm\u00B3"





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
		self.txt_rd_fresh.setToolTip("Angabe in g")

		self.txt_rd_dry = QLineEdit(self.tab1)
		self.txt_rd_dry.setGeometry(QRect(260, 80, 141, 27))
		self.txt_rd_dry.setToolTip("Angabe in g")

		self.txt_rd_vol = QLineEdit(self.tab1)
		self.txt_rd_vol.setGeometry(QRect(260, 120, 141, 27))
		self.txt_rd_vol.setToolTip("Angabe in g/cm\u00B3")

		self.lbl_rd_fresh = QLabel(self.tab1)
		self.lbl_rd_fresh.setGeometry(QRect(40, 200, 120, 17))
		self.lbl_rd_fresh.setText("Rohdichte frisch:")

		self.lbl_rd_dry2 = QLabel(self.tab1)
		self.lbl_rd_dry2.setGeometry(QRect(40, 240, 120, 17))
		self.lbl_rd_dry2.setText("Rohdichte trocken:")

		self.btn_rd_Calc = QPushButton(self.tab1)
		self.btn_rd_Calc.setGeometry(QRect(280, 270, 100, 30))
		self.btn_rd_Calc.setText("Berechnen")

		self.lbl_rd_res_fresh = QLabel(self.tab1)
		self.lbl_rd_res_fresh.setGeometry(QRect(290, 200, 120, 22))
		#self.lbl_rd_res_fresh.setText("")

		self.lbl_rd_res_dry = QLabel(self.tab1)
		self.lbl_rd_res_dry.setGeometry(QRect(290, 240, 120, 22))
		#self.lbl_rd_res_dry.setText("")


		#######################	Wkmax TAB ########################

		self.lbl_wkmax_atro = QLabel(self.tab2)
		self.lbl_wkmax_atro.setGeometry(QRect(40, 45, 200, 17))
		self.lbl_wkmax_atro.setText("Masse der Probe atro (105 °C):")

		self.lbl_wkmax_wkmax = QLabel(self.tab2)
		self.lbl_wkmax_wkmax.setGeometry(QRect(40, 85, 300, 17))
		self.lbl_wkmax_wkmax.setText("Masse bei maximaler H\u2082O Sättigung:")

		self.lbl_wkmax_Zylinder = QLabel(self.tab2)
		self.lbl_wkmax_Zylinder.setGeometry(QRect(40, 125, 300, 17))
		self.lbl_wkmax_Zylinder.setText("Volumen des Stechzylinders:")

		self.txt_wkmax_atro = QLineEdit(self.tab2)
		self.txt_wkmax_atro.setGeometry(QRect(350, 40, 141, 27))
		self.txt_wkmax_atro.setToolTip("Angabe in g")

		self.txt_wkmax_wkmax = QLineEdit(self.tab2)
		self.txt_wkmax_wkmax.setGeometry(QRect(350, 80, 141, 27))
		self.txt_wkmax_wkmax.setToolTip("Angabe in g")

		self.txt_wkmax_Zylinder = QLineEdit(self.tab2)
		self.txt_wkmax_Zylinder.setGeometry(QRect(350, 120, 141, 27))
		self.txt_wkmax_Zylinder.setToolTip("Angabe in cm\u00B3")

		self.lbl_wkmax_lblres = QLabel(self.tab2)
		self.lbl_wkmax_lblres.setGeometry(QRect(40, 200, 200, 17))
		self.lbl_wkmax_lblres.setText("Wassergehalt in % Volumen:")

		self.lbl_wkmax_Result = QLabel(self.tab2)
		self.lbl_wkmax_Result.setGeometry(QRect(400, 200, 120, 17))

		self.btn_wkmax_calc = QPushButton(self.tab2)
		self.btn_wkmax_calc.setGeometry(QRect(365, 270, 100, 30))
		self.btn_wkmax_calc.setText("Berechnen")




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
