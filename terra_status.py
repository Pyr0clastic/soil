import sys
from PyQt5.QtCore import QFileInfo, QRect, QRegExp, Qt
from PyQt5.QtWidgets import QMainWindow, QComboBox, QLineEdit, QLabel, QDesktopWidget, QMessageBox, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout, QGridLayout, QAbstractButton, QButtonGroup, QGroupBox, QRadioButton
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtCore import pyqtSlot

import sqlite3 as lite

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

		global vol
		vol = " % Vol."
		global g_cm3
		g_cm3 = " g/cm\u00B3"
		global rd_dry
		rd_dry = None
		global proz
		proz = " %"
		global bodenzustand
		bodenzustand = "humus_dry"
		global chroma
		chroma = None
		global bo_art
		bo_art = "S"
		global value
		value = None
		global active_tab
		active_tab = None




		self.table_widget = MyTableWidget(self)
		self.setCentralWidget(self.table_widget)

		self.createActions()
		self.createMenus()
		self.center()
		self.show()

		self.table_widget.btn_rd_Calc.clicked.connect(self.errorRohdichte)
		self.table_widget.btn_wkmax_calc.clicked.connect(self.errorRohdichte)
		self.table_widget.btn_festD_calc.clicked.connect(self.errorFeststoff)


		self.table_widget.comboBox_Chroma.currentIndexChanged.connect(self.chroma)
		self.table_widget.comboBox_Value.currentIndexChanged.connect(self.humus)
		self.table_widget.aBTN.buttonClicked.connect(self.wet_or_dry)
		self.table_widget.gBTN.buttonClicked.connect(self.bodenart)

		self.table_widget.tabs.currentChanged[int].connect(self.tabSelected)


		reg_ex = QRegExp("[0-9]+\.[0-9]{,4}")
		input_validator = QRegExpValidator(reg_ex)

		self.table_widget.txt_rd_fresh.setValidator(input_validator)
		self.table_widget.txt_rd_dry.setValidator(input_validator)
		self.table_widget.txt_rd_vol.setValidator(input_validator)

		self.table_widget.txt_wkmax_atro.setValidator(input_validator)
		self.table_widget.txt_wkmax_wkmax.setValidator(input_validator)
		self.table_widget.txt_wkmax_Zylinder.setValidator(input_validator)

		self.table_widget.txt_festD_mass.setValidator(input_validator)
		self.table_widget.txt_festD_xylol.setValidator(input_validator)
		self.table_widget.txt_festD_rohDry.setValidator(input_validator)

		self.table_widget.txt_caG_einwage.setValidator(input_validator)
		self.table_widget.txt_caG_co2.setValidator(input_validator)
		self.table_widget.txt_caG_temp.setValidator(input_validator)
		self.table_widget.txt_caG_preassure.setValidator(input_validator)

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
				"Dieses Programm dient zur Berechnung von Bodenparametern "
				"aus Messwerten nach ÖNORM")

	def errorRohdichte(self):
		try:
			self.rohdichte()
		except ValueError:
			return(QMessageBox.warning(None, 'Error', 'Fehlende Parameter zur Berechnung!'))

	def errorWkmax(self):
		try:
			self.wkmax()
		except ValueError:
			return(QMessageBox.warning(None, 'Error', 'Fehlende Parameter zur Berechnung!'))

	def errorFeststoff(self):
		try:
			self.feststoffdichte()
		except ValueError:
			return(QMessageBox.warning(None, "Error", "Fehlende Paramter zur Berechnung!"))

	def rohdichte(self):
		masse_frisch = float(self.table_widget.txt_rd_fresh.text())
		masse_trocken = float(self.table_widget.txt_rd_dry.text())
		stechzyl_Volumen = float(self.table_widget.txt_rd_vol.text())
		global rd_wet
		rd_wet = str(round((masse_frisch/stechzyl_Volumen),4))
		rd_dry = str(round((masse_trocken/stechzyl_Volumen),4))
		self.table_widget.lbl_rd_res_fresh.setText(rd_wet + g_cm3)
		self.table_widget.lbl_rd_res_dry.setText(rd_dry + g_cm3)
		self.table_widget.txt_festD_rohDry.setText(rd_dry)


	def wkmax(self):
		masse_atro = float(self.table_widget.txt_wkmax_atro.text())
		masse_wkmax = float(self.table_widget.txt_wkmax_wkmax.text())
		stechzyl_Volumen = float(self.table_widget.txt_wkmax_Zylinder.text())
		res_wkmax = round((((masse_wkmax - masse_atro)/stechzyl_Volumen)*100),2)
		global wkmax
		wkmax = str(res_wkmax)
		self.table_widget.lbl_wkmax_Result.setText(wkmax + vol)

	def feststoffdichte(self):
		rd_dry = float(self.table_widget.txt_festD_rohDry.text())
		masse = float(self.table_widget.txt_festD_mass.text())
		xylol = float(self.table_widget.txt_festD_xylol.text())
		res_feststoff = round((masse/(50-xylol)), 3)
		substanzV = round(((rd_dry/res_feststoff)*100), 2)
		#res_feststoff = str(res_feststoff)
		#substanzV=str(substanzV)
		gpv = round((1 - (rd_dry/res_feststoff))*100, 2)



		self.table_widget.lbl_festD_res_festD.setText(str(res_feststoff) + g_cm3)
		self.table_widget.lbl_festD_res_substanzV.setText(str(substanzV) + vol)
		self.table_widget.lbl_festD_res_gpv.setText(str(gpv) + vol)



	def wet_or_dry(self, source):
		global bodenzustand
		if isinstance(source, QAbstractButton):
			source = ("{}".format(source.text()))
		if source == "feucht":
			bodenzustand = "humus"
		elif source == "trocken":
			bodenzustand = "humus_dry"
		self.check_humus_db()

	def bodenart(self, id_or_btn):
		global bo_art
		if isinstance(id_or_btn, QAbstractButton):
			#print("{}" .format(id_or_btn.text()))
			id_or_btn = ("{}" .format(id_or_btn.text()))
		if id_or_btn == "Sand & Grus":
			bo_art = "S"
		elif id_or_btn == "lehmiger Sand - sandiger Lehm":
			bo_art = "G"
		elif id_or_btn == "Lehm, Schluff & Ton":
			bo_art = "U"
		self.check_humus_db()

	def chroma(self, chrom):
		global chroma
		if chrom ==1:
			chroma = 0
		elif chrom == 2:
			chroma = 0.5
		elif chrom == 3:
			chroma = 1.0
		self.check_humus_db()


	def humus(self, val):
		global value
		global chroma
		if val  == 1:
			value = 7.0
		elif val == 2:
			value = 6.5
		elif val == 3:
			value = 6.0
		elif val == 4:
			value = 5.5
		elif val == 5:
			value = 5.0
		elif val == 6:
			value = 4.5
		elif val == 7:
			value = 4.0
		elif val == 8:
			value = 3.5
		elif val == 9:
			value = 3.0
		elif val == 10:
			value = 2.5
		elif val == 11:
			value = 2.0
		self.check_humus_db()



	def check_humus_db(self):
		global hum_geh
		global bo_art, bodenzustand, chroma, value
		cr = chroma
		value_x = value
		list = [value_x, cr]
		if None not in list:
			if chroma == 0:
				value_x = value
			elif chroma == 0.5:
				value_x = value + chroma
			elif chroma == 1.0:
				value_x = value + chroma
			hum_geh = None
			con = lite.connect('humus.sqlite')
			cur = con.cursor()
			cur.execute(f"SELECT {bo_art} FROM {bodenzustand} WHERE db_value = {value_x}")
			rows = cur.fetchall()
			for row in rows:
				hum_geh = row[0]
			self.table_widget.lbl_humus_out.setText(str(hum_geh) + proz)



	def whatTab(self):
		currentIndex=self.table_widget.tabs.currentIndex()

	def tabSelected(self, arg=None):
		active_tab = arg
		print(arg)
		print ('\n\t tabSelected() current Tab index =', arg)


	def keyPressEvent(self, event):				# Code execution on Return key pressed
		tab_index = self.table_widget.tabs.currentIndex()
		if event.key() == Qt.Key_Return:
			if tab_index == 0:
				self.errorRohdichte()
			elif tab_index ==1:
				self.errorWkmax()
			elif tab_index ==2:
				self.errorFeststoff()










class MyTableWidget(QWidget):
	def __init__(self, parent):
		super(QWidget, self).__init__(parent)

		self.layout = QVBoxLayout(self)
		self.tabs = QTabWidget()
		#self.tabs.setMovable(True)			not working because of keyPress Return key
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tab3 = QWidget()
		self.tab4 = QWidget()
		self.tab5 = QWidget()
		self.tabs.resize(300, 200)
		self.tabs.addTab(self.tab1, "Rohdichte")
		self.tabs.addTab(self.tab2, "Wkmax")
		self.tabs.addTab(self.tab3, "Feststoffdichte")
		self.tabs.addTab(self.tab4, "Organische Substanz")
		self.tabs.addTab(self.tab5, "Carbonat Gehalt")








######################### Rohdichte TAB ##############################
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
		self.txt_rd_fresh.setGeometry(QRect(350, 40, 141, 27))
		self.txt_rd_fresh.setToolTip("Angabe in g")

		self.txt_rd_dry = QLineEdit(self.tab1)
		self.txt_rd_dry.setGeometry(QRect(350, 80, 141, 27))
		self.txt_rd_dry.setToolTip("Angabe in g")

		self.txt_rd_vol = QLineEdit(self.tab1)
		self.txt_rd_vol.setGeometry(QRect(350, 120, 141, 27))
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


##############################	Wkmax TAB ##############################

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


############################ Feststoffdichte Tab #######################

		self.lbl_festD_mass = QLabel(self.tab3)
		self.lbl_festD_mass.setGeometry(QRect(40, 45, 200, 17))
		self.lbl_festD_mass.setText("Masse der Probe (gemörsert):")

		self.lbl_festD_xylol = QLabel(self.tab3)
		self.lbl_festD_xylol.setGeometry(QRect(40, 85, 300, 17))
		self.lbl_festD_xylol.setText("Xylolverbrauch:")

		self.lbl_festD_rohDry = QLabel(self.tab3)
		self.lbl_festD_rohDry.setGeometry(QRect(40, 125, 300, 17))
		self.lbl_festD_rohDry.setText("Rohdichte trocken:")

		self.lbl_festD_FestD = QLabel(self.tab3)
		self.lbl_festD_FestD.setGeometry(QRect(40, 165, 300, 17))
		self.lbl_festD_FestD.setText("Feststoffdichte:")

		self.txt_festD_mass = QLineEdit(self.tab3)
		self.txt_festD_mass.setGeometry(QRect(350, 40, 141, 27))
		self.txt_festD_mass.setToolTip("Angabe in g")

		self.txt_festD_xylol = QLineEdit(self.tab3)
		self.txt_festD_xylol.setGeometry(QRect(350, 80, 141, 27))
		self.txt_festD_xylol.setToolTip("Angabe in ml")

		self.txt_festD_rohDry = QLineEdit(self.tab3)
		self.txt_festD_rohDry.setGeometry(QRect(350, 120, 141, 27))
		self.txt_festD_rohDry.setToolTip("Angabe in g/cm\u00B3")

		self.lbl_festD_res_festD = QLabel(self.tab3)
		self.lbl_festD_res_festD.setGeometry(QRect(350, 160, 300, 17))

		self.lbl_festD_substanzV = QLabel(self.tab3)
		self.lbl_festD_substanzV.setGeometry(QRect(40, 205, 300, 17))
		self.lbl_festD_substanzV.setText("Substanzvolumen:")

		self.lbl_festD_res_substanzV = QLabel(self.tab3)
		self.lbl_festD_res_substanzV.setGeometry(QRect(350, 205, 300, 17))

		self.lbl_festD_gpv = QLabel(self.tab3)
		self.lbl_festD_gpv.setGeometry(QRect(40, 245, 300, 17))
		self.lbl_festD_gpv.setText("Gesamtporenvolumen:")

		self.lbl_festD_res_gpv = QLabel(self.tab3)
		self.lbl_festD_res_gpv.setGeometry(QRect(350, 245, 300, 17))



		self.btn_festD_calc = QPushButton(self.tab3)
		self.btn_festD_calc.setGeometry(QRect(365, 270, 100, 30))
		self.btn_festD_calc.setText("Berechnen")

		#self.lbl_test = QLabel(self.tab1)
		#self.lbl_test.setGeometry(QRect(365, 365, 100, 17))

##################### Humusgehalt, Organische Substanz Tab ################

		self.grid = QGridLayout(self.tab4)

		self.comboBox_Chroma = QComboBox(self.tab4)
		self.comboBox_Chroma.setGeometry(QRect(250, 100, 190, 27))
		self.comboBox_Chroma.addItem("")
		self.comboBox_Chroma.setItemText(0, "----- Chroma -----")
		self.comboBox_Chroma.model().item(0).setEnabled(False)
		self.comboBox_Chroma.addItem("< 3.5")
		self.comboBox_Chroma.addItem("3.5 - 6")
		self.comboBox_Chroma.addItem("> 6")

		self.grid.addWidget(self.comboBox_Chroma, 0, 0)

		self.comboBox_Value = QComboBox(self.tab4)
		self.comboBox_Value.setGeometry(QRect(250, 150, 190, 27))
		self.comboBox_Value.addItem("")
		self.comboBox_Value.setItemText(0, "---- Value ----")
		self.comboBox_Value.model().item(0).setEnabled(False)
		self.comboBox_Value.addItem("7.0")
		self.comboBox_Value.addItem("6.5")
		self.comboBox_Value.addItem("6.0")
		self.comboBox_Value.addItem("5.5")
		self.comboBox_Value.addItem("5.0")
		self.comboBox_Value.addItem("4.5")
		self.comboBox_Value.addItem("4.0")
		self.comboBox_Value.addItem("3.5")
		self.comboBox_Value.addItem("3.0")
		self.comboBox_Value.addItem("2.5")
		self.comboBox_Value.addItem("2.0")

		self.grid.addWidget(self.comboBox_Value, 1, 0)

		self.lbl_humus_1 = QLabel(self.tab4)
		self.lbl_humus_1.setGeometry(QRect(40, 240, 171, 17))
		self.lbl_humus_1.setText("Humusgehalt: ")

		self.lbl_humus_out = QLabel(self.tab4)
		self.lbl_humus_out.setGeometry(QRect(150, 240, 171, 17))

		#self.grid.addWidget(self.lbl_humus_1, 2, 0)
		#self.grid.addWidget(self.lbl_humus_out, 2, 1)


		############# QGroupBox with Radiobuttons 	#################

		self.gBox_wd = QGroupBox(self.tab4)
		self.vbox = QVBoxLayout(self.gBox_wd)
		self.rdb_wet = QRadioButton("feucht")
		self.rdb_dry = QRadioButton("trocken")
		self.rdb_dry.setChecked(True)
		self.vbox.addWidget(self.rdb_dry)
		self.vbox.addWidget(self.rdb_wet)



		#self.gBox_wd.setVisible(False)

		self.grid.addWidget(self.gBox_wd, 0, 1)

		self.gBox = QGroupBox("Bodenart", self.tab4)
		self.vbox = QVBoxLayout(self.gBox)
		self.rdb_1 = QRadioButton("Sand & Grus")

		self.rdb_2 = QRadioButton("lehmiger Sand - sandiger Lehm")
		self.rdb_3 = QRadioButton("Lehm, Schluff & Ton")
		self.vbox.addWidget(self.rdb_1)
		self.vbox.addWidget(self.rdb_2)
		self.vbox.addWidget(self.rdb_3)

		self.rdb_1.setChecked(True)


		self.gBTN = QButtonGroup(self.gBox)
		self.gBTN.addButton(self.rdb_1)
		self.gBTN.addButton(self.rdb_2)
		self.gBTN.addButton(self.rdb_3)

		self.aBTN = QButtonGroup(self.gBox_wd)
		self.aBTN.addButton(self.rdb_wet)
		self.aBTN.addButton(self.rdb_dry)



		self.grid.addWidget(self.gBox, 1, 1)
		self.grid.setRowStretch(2, 1)
		#self.grid.setColumnStretch(1, 3)

######################## Carbonat Gehalt TAB ############################

		self.lbl_caG_1 = QLabel(self.tab5)
		self.lbl_caG_1.setGeometry(QRect(40, 45, 151, 17))
		self.lbl_caG_1.setText("Einwage:")

		self.lbl_caG_2 = QLabel(self.tab5)
		self.lbl_caG_2.setGeometry(QRect(40, 85, 161, 17))
		self.lbl_caG_2.setText("Gebildetes CO\u2082:")

		self.lbl_caG_3 = QLabel(self.tab5)
		self.lbl_caG_3.setGeometry(QRect(40, 125, 180, 17))
		self.lbl_caG_3.setText("Raumtemperatur:")

		self.lbl_caG_4 = QLabel(self.tab5)
		self.lbl_caG_4.setGeometry(QRect(40, 165, 180, 17))
		self.lbl_caG_4.setText("Luftdruck:")

		self.txt_caG_einwage = QLineEdit(self.tab5)
		self.txt_caG_einwage.setGeometry(QRect(350, 40, 141, 27))
		self.txt_caG_einwage.setToolTip("Angabe in g")

		self.txt_caG_co2 = QLineEdit(self.tab5)
		self.txt_caG_co2.setGeometry(QRect(350, 80, 141, 27))
		self.txt_caG_co2.setToolTip("Angabe in ml")
		self.txt_caG_co2.setText("BLUUBB")

		self.txt_caG_temp = QLineEdit(self.tab5)
		self.txt_caG_temp.setGeometry(QRect(350, 120, 141, 27))
		self.txt_caG_temp.setToolTip("Angabe in °Celsius")

		self.txt_caG_preassure = QLineEdit(self.tab5)
		self.txt_caG_preassure.setGeometry(QRect(350, 160, 141, 27))
		self.txt_caG_preassure.setToolTip("Angabe in hPa")






################################################################


		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
