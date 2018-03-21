#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * #QWidget, QDesktopWidget, QApplication, QPushButton, QLineEdit, QLabel
#from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import *

class Example(QMainWindow):
	def __init__(self):
		super(Example, self).__init__()

		widget = QWidget()
		self.setCentralWidget(widget)
		self.resize(450, 350)
		bottomFiller = QWidget()
		bottomFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		#self.center()
		#self.setWindowTitle('Center')
		#self.show()

		self.infoLabel = QLabel("<i>Choose a menu option, or right-click to invoke a context menu</i>", alignment=Qt.AlignCenter)
		self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

		vbox = QVBoxLayout()
		vbox.setContentsMargins(5, 5, 5, 5)
		#vbox.addWidget(topFiller)
		vbox.addWidget(self.infoLabel)
		vbox.addWidget(bottomFiller)
		widget.setLayout(vbox)

		self.createActions()
		self.createMenus()

		qbtn = QPushButton('Quit', self)
		qbtn.clicked.connect(QCoreApplication.instance().quit)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(50, 50)
		#txt = QLineEdit(self)
		self.txt1=QLineEdit(self)
		self.txt1.move(80, 40)
		self.txt1.resize(100, 20)
		lbl1 = QLabel(self)
		lbl1.move(280, 150)
		lbl1.resize(60,20)
		#self.txt1.editingFinished(self.test)
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

		self.aboutQtAct = QAction("About &Qt", self) #triggered=self.aboutQt)

		#self.aboutQtAct = QAction("About &Qt", self,
		#		statusTip="Show the Qt library's About box",
		#		triggered=self.aboutQt)
		self.aboutQtAct.triggered.connect(QApplication.instance().aboutQt)

	def createMenus(self):
		self.helpMenu = self.menuBar().addMenu("&Help")
		self.helpMenu.addAction(self.aboutAct)
		self.helpMenu.addAction(self.aboutQtAct)

	def about(self):
		QMessageBox.about(self, "About Menu",
				"The <b>Menu</b> example shows how to create menu-bar menus "
				"and context menus.")

	#def aboutQt(self):
	#	self.infoLabel.setText("Invoked <b>Help|About Qt</b>")




	def test(self):
		data = self.txt1.text()
		self.lbl1.setText(str(data))



	'''def initUI(self):

		qbtn = QPushButton('Quit', self)
		qbtn.clicked.connect(QCoreApplication.instance().quit)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(50, 50)
		txt = QLineEdit(self)
		txt.move(80, 40)
		txt.resize(100, 20)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Quit button')
		self.show()
	'''
if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Example()
	ex.show()
	sys.exit(app.exec_())
