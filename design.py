# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import sys
import csv
import xlsxwriter
import sqlite3 as lite
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import *  #QRegExp
#from PyQt5.Qt import QApplication
#from PyQt5.QtGui import *   #QRegExpValidator
#from PyQt5.QtWidgets import QMessageBox, QMainWindow, QMenu, QApplicatio
#from PyQt5.QtWidgets import *
#from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *








class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("TerraStatum")
        MainWindow.resize(900, 600)
        MainWindow.setFixedSize(900, 600)                           # prevents resizing of MainWindow
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.tabWidget.setMovable(True)
        self.tabWidget.setMinimumSize(900, 600)
        MainWindow.setWindowTitle("TerraStatum")
        #self.tabWidget.resize(True)



#        menubar = self.menuBar()
#        if sys.platform == "darwin":					#		my workaround for mac os
#            menubar.setNativeMenuBar(False)				#
#        elif sys.platform == "win32":
#            menubar.setNativeMenuBar(True)
#        else:									#
#            pass
#        fileMenu = menubar.addMenu('File')
        #saveMenu = menubar.addMenu("Save")

        global vol
        global g_cm3
        global rd_dry          # temporary test for feststoffdichte
        rd_dry = None           # temprory test for feststoffdichte
        vol = " % Vol."
        g_cm3 = " g/cm\u00B3"


        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.tabWidget.addTab(self.tab, "")
        #self.tab_2 = QtWidgets.QWidget()
        #self.tab_2.setObjectName("tab_2")
        #self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")



        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 45, 151, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 85, 161, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 125, 180, 17))
        self.label_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(260, 40, 141, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 80, 141, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 120, 141, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 120, 17))
        self.label_4.setObjectName("label_4")
        self.lbl_rd_dry = QtWidgets.QLabel(self.tab)
        self.lbl_rd_dry.setGeometry(QtCore.QRect(40, 240, 120, 17))
        self.lbl_rd_dry.setObjectName("lbl_rd_dry")
        self.rd_Berechnen = QtWidgets.QPushButton(self.tab)
        self.rd_Berechnen.setGeometry(QtCore.QRect(280, 270, 100, 30))
        self.rd_Berechnen.setObjectName("rd_Berechnen")

        self.lbl_res_rd_wet = QtWidgets.QLabel(self.tab)
        self.lbl_res_rd_wet.setGeometry(QtCore.QRect(290, 200, 120, 22))

        self.lbl_res_rd_dry = QtWidgets.QLabel(self.tab)
        self.lbl_res_rd_dry.setGeometry(QtCore.QRect(290, 240, 120, 22))

        #self.lbl_res_rd_dry = QtWidgets.QLabel(self.tab)
        #self.lbl_res_rd_dry.setGeometry(QtCore.QRect(290, 240, 90, 17))

        self.lbl_org_subs = QtWidgets.QLabel(self.tab_2)
        self.lbl_org_subs.setGeometry(QtCore.QRect(40, 45, 200, 17))
        self.lbl_org_subs.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lbl_org_subs.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.lbl_org_subs.setObjectName("lbl_org_subs")

        self.txt_wkmax_atro = QtWidgets.QLineEdit(self.tab_2)
        self.txt_wkmax_atro.setGeometry(QtCore.QRect(350, 40, 141, 27))
        self.txt_wkmax_atro.setObjectName("txt_wkmax_atro")

        self.lbl_wkmax_wkmax = QtWidgets.QLabel(self.tab_2)
        self.lbl_wkmax_wkmax.setGeometry(QtCore.QRect(40, 85, 300, 17))
        self.lbl_wkmax_wkmax.setObjectName("lbl_wkmax_wkmax")

        self.txt_wkmax_wkmax = QtWidgets.QLineEdit(self.tab_2)
        self.txt_wkmax_wkmax.setGeometry(QtCore.QRect(350, 80, 141, 27))
        self.txt_wkmax_wkmax.setObjectName("txt_wkmax_wkmax")

        self.lbl_wkmax_Zylinder = QtWidgets.QLabel(self.tab_2)
        self.lbl_wkmax_Zylinder.setGeometry(QtCore.QRect(40, 125, 300, 17))
        self.lbl_wkmax_Zylinder.setObjectName("lbl_wkmax_Zylinder")

        self.txt_wkmax_Zylinder = QtWidgets.QLineEdit(self.tab_2)
        self.txt_wkmax_Zylinder.setGeometry(QtCore.QRect(350, 120, 141, 27))
        self.txt_wkmax_Zylinder.setObjectName("txt_wkmax_Zylinder")

        self.lbl_wkmax_lblres = QtWidgets.QLabel(self.tab_2)
        self.lbl_wkmax_lblres.setGeometry(QtCore.QRect(40, 200, 200, 17))
        self.lbl_wkmax_lblres.setObjectName("lbl_wkmax_lblres")

        self.lbl_wkmax_Result = QtWidgets.QLabel(self.tab_2)
        self.lbl_wkmax_Result.setGeometry(QtCore.QRect(400, 200, 120, 17))
        self.lbl_wkmax_Result.setObjectName("lbl_wkmax_Result")

        self.btn_wkmax_calc = QtWidgets.QPushButton(self.tab_2)
        self.btn_wkmax_calc.setGeometry(QtCore.QRect(365, 270, 100, 30))

        self.lbl_festD_Masse = QtWidgets.QLabel(self.tab_3)
        self.lbl_festD_Masse.setGeometry(QtCore.QRect(40, 45, 200, 17))
        self.lbl_festD_Masse.setObjectName("lbl_festD_Masse")

        self.lbl_festD_Xylol = QtWidgets.QLabel(self.tab_3)
        self.lbl_festD_Xylol.setGeometry(QtCore.QRect(40, 85, 300, 17))
        self.lbl_festD_Xylol.setObjectName("lbl_festD_Xylol")


        self.txt_festD_Masse = QtWidgets.QLineEdit(self.tab_3)
        self.txt_festD_Masse.setGeometry(QtCore.QRect(350, 40, 141, 27))
        self.txt_festD_Masse.setObjectName("txt_festD_Masse")

        self.txt_festD_Xylol = QtWidgets.QLineEdit(self.tab_3)
        self.txt_festD_Xylol.setGeometry(QtCore.QRect(350, 80, 141, 27))
        self.txt_festD_Xylol.setObjectName("txt_festD_Xylol")


        self.lbl_festD_FestD = QtWidgets.QLabel(self.tab_3)
        self.lbl_festD_FestD.setGeometry(QtCore.QRect(40, 125, 300, 17))
        self.lbl_festD_FestD.setObjectName("lbl_festD_FestD")

        self.lbl_festD_res_FestD = QtWidgets.QLabel(self.tab_3)
        self.lbl_festD_res_FestD.setGeometry(QtCore.QRect(350, 125, 300, 17))
        self.lbl_festD_res_FestD.setObjectName("lbl_festD_res_FestD")
        self.lbl_festD_res_FestD.setText("")

        self.btn_festD_calc = QtWidgets.QPushButton(self.tab_3)
        self.btn_festD_calc.setGeometry(QtCore.QRect(365, 270, 100, 30))
        self.btn_festD_calc.setObjectName("btn_festD_calc")

        self.lbl_festD_rohDry = QtWidgets.QLabel(self.tab_3)
        self.lbl_festD_rohDry.setGeometry(QtCore.QRect(40, 165, 300, 17))
        self.lbl_festD_rohDry.setObjectName("lbl_festD_rohDry")

        self.txt_festD_rohDry = QtWidgets.QLineEdit(self.tab_3)
        self.txt_festD_rohDry.setGeometry(QtCore.QRect(350, 160, 141, 27))
        self.txt_festD_rohDry.setObjectName("txt_festD_rohDry")

        self.lbl_festD_SubstanzV = QLabel(self.tab_3)
        self.lbl_festD_SubstanzV.setGeometry(QtCore.QRect(40, 205, 300, 17))
        self.lbl_festD_SubstanzV.setObjectName("lbl_festD_SubstanzV")
        self.lbl_festD_SubstanzV.setText("Substanzvolumen:")

        self.lbl_festD_SubstanzResult = QLabel(self.tab_3)
        self.lbl_festD_SubstanzResult.setGeometry(QtCore.QRect(350, 205, 300, 17))
        self.lbl_festD_SubstanzResult.setText("")

        self.lbl_festD_GPV = QLabel(self.tab_3)
        self.lbl_festD_GPV.setGeometry(QRect(40, 245, 300, 17))
        self.lbl_festD_GPV.setText("Gesamtporenvolumen:")

        self.lbl_festD_GPV_result = QLabel(self.tab_3)
        self.lbl_festD_GPV_result.setGeometry(QRect(350, 245, 300, 17))
        self.lbl_festD_GPV_result.setText("")


        ###################     HUMUSgehalt ##########################


        self.comboBox_Chroma = QComboBox(self.tab_4)
        self.comboBox_Chroma.setGeometry(QRect(250, 100, 190, 27))
        self.comboBox_Chroma.addItem("")
        self.comboBox_Chroma.addItem("")
        self.comboBox_Chroma.addItem("")
        self.comboBox_Chroma.setItemText(0, "----- Chroma XXX-----")

        self.comboBox_Value = QComboBox(self.tab_4)
        self.comboBox_Value.setGeometry(QRect(250, 150, 190, 27))
        self.comboBox_Value.addItem("")
        self.comboBox_Value.addItem("Value 2")
        self.comboBox_Value.setItemText(0, "--- Value ---")

        # self.rbtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        # self.rbtn.setText("Trocken")
        # self.rbtn.setObjectName("rbtnTrocken")
        # self.gridLayout.addWidget(self.rbtn, 1, 0, 1, 1)
        # self.rbtn.toggled.connect(self.state)
        #
        # self.rbtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        # self.rbtn.setText("Feucht")
        # self.rbtn.setObjectName("rbtnFeucht")
        # self.gridLayout.addWidget(self.rbtn, 0, 0, 1, 1)
        # self.rbtn.toggled.connect(self.state)
        #
        # self.tabWidget.addTab(self.tab_4, "")




        #self.inputWD = QInputDialog(self.tab_4)








        font = QtGui.QFont()
        #font.setPointSize(12)
        font.setBold(True)
        #font.setWeight(75)
        self.lbl_res_rd_wet.setFont(font)
        self.lbl_res_rd_wet.setObjectName("lbl_res_rd_wet")
        self.lbl_res_rd_dry.setFont(font)
        self.lbl_res_rd_dry.setObjectName("lbl_rd_dry")
        self.lbl_wkmax_Result.setFont(font)




        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(740, 520, 85, 27))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 851, 27))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())




        #self.formLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 250, 481, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")



        #self.formLayoutWidget.setGeometry(QtCore.QRect(50, 250, 481, 171))
        #self.comboBox.setGeometry(QRect(50, 250, 200, 200))
        #self.comboBox.setObjectName("comboBox")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")

        #self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.comboBox)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_3.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "--- Chroma ---")
        self.comboBox_3.model().item(0).setEnabled(False)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        #self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        #self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setToolTip("Value")
        self.comboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "--- Value ---")
        self.comboBox_2.model().item(0).setEnabled(False)
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(1, "0.5 hellgrau")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(2, "1.0 hellgrau")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(3, "grau                                        !")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(4, "grau                                       !")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(5, "grau                                       !")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(6, "dunkelgrau                            !")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(7, "dunkelgrau                            !")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lbl_humus_lbl = QtWidgets.QLabel(self.tab_4)
        self.lbl_humus_lbl.setGeometry(QtCore.QRect(40, 140, 171, 17))
        self.lbl_humus_lbl.setObjectName("lbl_humus_lbl")
        self.lbl_humus_lbl.setText("Humusgehalt: ")
        self.lbl_humus_out = QtWidgets.QLabel(self.tab_4)
        self.lbl_humus_out.setGeometry(QtCore.QRect(150, 140, 171, 17))
        self.lbl_humus_out.setObjectName("lbl_humus_out")
        self.lbl_humus_out.setText("")











        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.lineEdit.textChanged.connect(self.Survey)
        self.rd_Berechnen.clicked.connect(self.newNoInput)
        #self.rd_Berechnen.clicked.connect(self.rohdichte)
        self.btn_wkmax_calc.clicked.connect(self.noInput_2)
        self.btn_festD_calc.clicked.connect(self.errorFeststoff)
        #self.actionSave.triggered.connect(self.Save)
        self.actionSave.triggered.connect(self.Excel)


        #self.lineEdit_2.textChanged[str].connect(self.justNumbers)


        #############   Input Validation        #######################

        #reg_ex = QRegExp("[0-9]+.?[0-9]{,4}")              TIPP: https://regex101.com/         https://docs.python.org/3/howto/regex.html
        reg_ex = QRegExp("[0-9]+\.[0-9]+")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit)

        self.lineEdit.setValidator(input_validator)
        self.lineEdit_2.setValidator(input_validator)
        self.lineEdit_3.setValidator(input_validator)

        self.txt_wkmax_atro.setValidator(input_validator)
        self.txt_wkmax_wkmax.setValidator(input_validator)
        self.txt_wkmax_Zylinder.setValidator(input_validator)

        self.txt_festD_Masse.setValidator(input_validator)
        self.txt_festD_Xylol.setValidator(input_validator)
        self.txt_festD_rohDry.setValidator(input_validator)






    def state(self):
        if self.rbtn.isChecked():
            print("Checked")


    def creatGrid_tab4(self):
        self.gridGroupBox = QGroupBox("Humus gehalt nach Munsell")
        layout = QGridLayout()
        layout.addWidget()


    def chroma(self, chrom):
        global chroma                       #every function creates own namespace => define global variable in namespace to make change global variable from within function!
        chroma = 0.0
        if chrom ==1:
            chroma = 0
            print (chroma)
        elif chrom == 2:
            chroma = 0.5
            return (chroma)
            print (chroma)
        elif chrom == 3:
            chroma = 1.0
            print (chroma)


    def humus(self, value):

        #print(value)
        if value  == 1:
            value = 7.0
            #print (value)
        elif value == 2:
            value = 6.5
            #print (value)
        elif value == 3:
            value = 6.0
            #print ("Value is:", value)
        elif value == 4:
            value = 5.5
            #print ("Value is: ", value)
        elif value == 5:
            value = 5.0
            #print ("Value is: ", value)
        elif value == 6:
            value = 4.5
            #print ("Value is: ", value)
        elif value == 7:
            value = 4.0
            #print ("Value is: ", value)
        elif value == 8:
            value = 3.5
            #print ("Value is: ", value)
        elif value == 9:
            value = 3.0
            #print("Value is: ", value)
        elif value == 10:
            value = 2.5
            #print ("Value is: ", value)
        elif value == 11:
            value = 2.0
            #print ("Value is: ", value)

        if chroma == 0:
            print (chroma)
            value = value + chroma
            #print ("Value is now: ", value)
        elif chroma == 0.5:
            value = value + chroma
            #print ("Value is now: ", value)
        elif chroma == 1.0:
            value = value + chroma
            #print ("Value is now: ", value)

        con = lite.connect('humus.sqlite')

        cur = con.cursor()
        check = "G"
        check_value = value
        cur.execute(f"SELECT {check} FROM humus WHERE db_value = {check_value}")
        rows = cur.fetchall()
        for row in rows:
            hum_geh = row[0]

        self.lbl_humus_out.setText(str(hum_geh) + proz)




    def about(self):
        QMessageBox.about(self, "About Menu",
            "The <b>Menu</b> example shows how to create menu-bar menus "
            "and context menus.")

    def createActions(self):
        self.aboutAct = QAction("&About", self,
            statusTip="Show the application's About box",
            triggered=self.about)

        self.aboutQtAct = QAction("About &Qt", self,
            statusTip="Show the Qt library's About box")
        self.aboutQtAct.triggered.connect(QApplication.instance().aboutQt)




    def createMenus(self):
        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)




    def setText(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
            "User name:", QLineEdit.Normal, QDir.home().dirName())
        if ok and text != '':
            self.textLabel.setText(text)


    def newNoInput(self):
        try:
            self.rohdichte()
        except ValueError:
            return(QMessageBox.warning(None, 'Error', 'Fehlende Parameter zur Berechnung!'))


    def errorFeststoff(self):
        try:
            self.feststoffdichte()
        except ValueError:
            return(QMessageBox.warning(None, "Error", "Fehlende Paramter zur Berechnung!"))




    def noInput(self):
        txt1 = self.lineEdit.text()
        txt2 = self.lineEdit_2.text()
        txt3 = self.lineEdit_3.text()
        list_new = [txt1, txt2, txt3]
        dia = QtWidgets.QErrorMessage(self.tab)
        none = ""
        if none in list_new:
            reply = dia.showMessage("Input ERROR!!\nFehlende Paramter zur Berechnung der Rohdichte(n)")
        else:
            self.rohdichte()

    def noInput_2(self):
        txt1 = self.txt_wkmax_atro.text()
        txt2 = self.txt_wkmax_wkmax.text()
        txt3 = self.txt_wkmax_Zylinder.text()
        list_new = [txt1, txt2, txt3]
        dia = QtWidgets.QErrorMessage(self.tab_2)
        none = ""
        if none in list_new:
            reply = dia.showMessage("Input ERROR!!\nFehlende Parameter zur Berechnung von Wkmax")
        else:
            self.wkmax()

    def noInput_festD(self):
        txt1 = self.txt_festD_Masse.text()
        txt2 = self.txt_festD_Xylol.text()
        list_new = [txt1, txt2]
        dia = QtWidgets.QErrorMessage(self.tab_3)
        none = ""
        if none in list_new:
            return(QMessageBox.warning(None, 'Error', 'Fehlende Parameter zur Berechnung!'))
            #reply = dia.showMessage("Input ERROR!!\nFehlende Parameter zur Berechnung der Feststoffdichte")
        else:
            self.feststoffdichte()

    def rohdichte(self):
        masse_frisch = float(self.lineEdit.text())
        masse_trocken = float(self.lineEdit_2.text())
        stechzyl_Volumen = float(self.lineEdit_3.text())
        global rd_wet
        #global rd_dry
        rd_wet = str(round((masse_frisch/stechzyl_Volumen),4))
        rd_dry = str(round((masse_trocken/stechzyl_Volumen),4))
        self.lbl_res_rd_wet.setText(rd_wet + g_cm3)
        self.lbl_res_rd_dry.setText(rd_dry + g_cm3)
        self.txt_festD_rohDry.setText(rd_dry)               # rohdichte dry is needed in feststoffdichte ! if value calculated it is set in tab_3


    def wkmax(self):
        masse_atro = float(self.txt_wkmax_atro.text())
        masse_wkmax = float(self.txt_wkmax_wkmax.text())
        stechzyl_Volumen = float(self.txt_wkmax_Zylinder.text())
        res_wkmax = round((((masse_wkmax - masse_atro)/stechzyl_Volumen)*100),2)
        global wkmax
        wkmax = str(res_wkmax)
        self.lbl_wkmax_Result.setText(wkmax + vol)

    def feststoffdichte(self):
        #rd_dry = float(self.txt_festD_rohDry.text())
        #if rd_dry is None:
            #self.txt_festD_rohDry = QtWidgets.QLineEdit(self.tab_3)
            #self.txt_festD_rohDry.setGeometry(QtCore.QRect(350, 120, 141, 27))
            #return(QMessageBox.warning(None, 'Title', 'Trockenrohdichte benötigt!'))
            #return(QInputDialog.getText(self, "User name:", QLineEdit.Normal, QDir.home().dirName()))
            #reply = dia.showMessage("Berechne die Rohdichte!")
        rd_dry = float(self.txt_festD_rohDry.text())
        #print(rd_dry)
        masse = float(self.txt_festD_Masse.text())
        xylol = float(self.txt_festD_Xylol.text())
        res_feststoff = round((masse/(50-xylol)), 3)
        substanzV = round(((rd_dry/res_feststoff)*100), 2)
        #res_feststoff = str(res_feststoff)
        #substanzV=str(substanzV)
        gpv = round((1 - (rd_dry/res_feststoff))*100, 2)



        self.lbl_festD_res_FestD.setText(str(res_feststoff) + g_cm3)
        self.lbl_festD_SubstanzResult.setText(str(substanzV) + vol)
        self.lbl_festD_GPV_result.setText(str(gpv) + vol)


    def Save(self):
        try:
            data_header=["Bestimmter Paramter", "Wert", "Einheit"]
            data = [["Wkmax", wkmax, vol],["Rohdichte feucht", rd_wet, g_cm3], ["Rohdichte_trocken", rd_dry, g_cm3]]
            with open("result.csv", "w") as file_writer:
                writer=csv.writer(file_writer)
                writer.writerow(data_header)
                for item in data:
                    writer.writerow(item)
                print(rd_wet, rd_dry)
                print(wkmax)
        except NameError:
            reply = dia.showMessage("Input ERROR!!\nFehlende Parameter zur Berechnung der Feststoffdichte")

    def Excel(self):
        try:
            workbook = xlsxwriter.Workbook('result.xlsx')
            worksheet = workbook.add_worksheet()
            worksheet.set_column('A:A', 20)
            worksheet.write('A1', 'Berechneter Parameter')
            worksheet.write('B1', "Wert")
            worksheet.write("C1", "Einheit")                      # Mit Uhrzeit und Autor angeben
            worksheet.write(1, 0, "Wkmax")
            worksheet.write(1, 1, wkmax)
            worksheet.write(1, 2, vol)
            worksheet.write(2, 0, "Rohdichte trocken")
            worksheet.write(2, 1, rd_dry)
            worksheet.write(2, 2, g_cm3)
            worksheet.write(3, 0, "Rohdichte feucht")
            worksheet.write(3, 1, rd_wet)
            worksheet.write(3, 2, g_cm3)
            workbook.close()
        except BaseException as error:
            #dia = QtWidgets.QMessageBox(self.centralwidget)
            #return(dia.showMessage('Ein Fehler ist aufgetreten!\n Keine Werte zum Abspeichern vorhanden!'))  #'Ein Fehler ist aufgetreten: {}'.format(error)
            return(QMessageBox.warning(None, 'Error', 'Error!\nKeine Werte zum Abspeichern vorhanden!'))
            #new = QErrorMessage(self.centralwidget)
            #return(new.showMessage("ERROR!"))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Masse der Probe frisch:"))
        self.label_2.setText(_translate("MainWindow", "Masser der Probe trocken:"))
        self.label_3.setText(_translate("MainWindow", "Volumen des Stechzylinders:"))
        self.lbl_org_subs.setText(_translate("MainWindow", "Masse der Probe atro (105 °C):"))
        self.lbl_wkmax_wkmax.setText(_translate("MainWindow", "Masse bei maximaler H\u2082O Sättigung:"))
        self.lbl_wkmax_Zylinder.setText(_translate("MainWindow", "Volumen des Stechzylinders:"))
        self.lbl_wkmax_lblres.setText(_translate("MainWindow", "Wassergehalt in % Volumen:"))
        self.lbl_wkmax_Result.setText(_translate("MainWindow", ""))
        self.lineEdit.setToolTip(_translate("MainWindow", "Angabe in g"))
        self.lineEdit_2.setToolTip(_translate("MainWindow", "Angabe in g"))
        self.lineEdit_3.setToolTip(_translate("MainWindow", "Volumen in cm\u00B3"))
        self.txt_wkmax_atro.setToolTip(_translate("MainWindow", "Angabe in g"))
        self.txt_wkmax_wkmax.setToolTip(_translate("MainWindow", "Angabe in g"))
        self.txt_wkmax_Zylinder.setToolTip(_translate("MainWindow", "Angabe in cm\u00B3"))
        self.label_4.setText(_translate("MainWindow", "Rohdichte feucht:"))
        self.lbl_rd_dry.setText(_translate("MainWindow", "Rohdichte trocken:"))
        self.rd_Berechnen.setText(_translate("MainWindow", "Berechnen"))
        self.btn_wkmax_calc.setText(_translate("MainWindow", "Berechnen"))
        self.btn_festD_calc.setText(_translate("MainWindow", "Berechnen"))
        self.lbl_res_rd_wet.setText(_translate("MainWindow", ""))
        self.lbl_res_rd_dry.setText(_translate("MainWindow", ""))
        self.lbl_festD_Masse.setText(_translate("MainWindow", "Masse der Probe (gemörsert):"))
        self.txt_festD_Masse.setToolTip(_translate("MainWindow", "Angabe in g"))
        self.txt_festD_rohDry.setToolTip(_translate("MainWindow", "Angabe in g/cm\u00B3"))

        self.lbl_festD_Xylol.setText(_translate("MainWindow", "Xylolverbrauch:"))
        self.txt_festD_Xylol.setToolTip(_translate("MainWindow", "Angabe in ml"))
        self.lbl_festD_FestD.setText(_translate("MainWindow", "Feststoffdichte:"))

        self.lbl_festD_rohDry.setText(_translate("MainWindow", "Rohdichte trocken:"))


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Rohdichte"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Wkmax"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Feststoffdichte"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Organische Substanz"))

        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", " Save"))
        self.actionExit.setText(_translate("MainWindow", ' &Exit'))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
