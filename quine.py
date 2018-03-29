# \author: Aritra Sarkar

#   cd /mnt/7A06EEA206EE5E9F/GoogleDrive/TUD_CE/Thesis/SimQG/QuInE/
#   python quine.py

import sys
from PyQt4 import QtGui, QtCore
import os
import re
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import syntax
import json
import math
from resultPlot import customPlot

class Window(QtGui.QMainWindow):
	
	win_ry = 900
	win_cx = 1600
	saved = 0
	
	circTick = 0
	gateNames = ("X","Y","Z","H","S","T","Rx","Ry","Rz","CX","CZ","Tf",u"\u23F2",u"\U0001F441")
	gateCodes = ("x","y","z","h","s","t","rx","ry","rz","cnot","cphase","toffoli","measure","display")
	gateSets = ("All","Universal {H, Tf}","Universal {1Qb, CX}")
	gateMasks = ("11111111111111","00010000000111","11111100010011")
	drawGateQ = []
	drawMaxQ = 0
	delGateLno = 0
		
	def __init__(self):

		super(Window,self).__init__()
		self.setGeometry(150,50,self.win_cx,self.win_ry)	# window placement and size (TBD: variable/fullscreen)
		self.setWindowTitle("Quantum Integrated Development Environment")
		self.setWindowIcon(QtGui.QIcon('icons/app.png'))	# (TBD: decide logo)

		self.menu()
		self.quickaccess()
		self.stsmsg = self.statusBar()
		self.stsmsg.showMessage('Create new project or Open existing project')
		self.show()
	
	########################## MAIN MENUS ##########################

	def menu(self):

		self.mainMenu = self.menuBar()
		self.menuFile = self.mainMenu.addMenu('&File')
		self.fileMenu()
		self.menuView = self.mainMenu.addMenu('&View')
		self.viewMenu()
		self.menuHelp = self.mainMenu.addMenu('&Help')
		self.helpMenu()

	#~~~~~~~~~~~~~~~~~~~~~~~~~ file menu ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def fileMenu(self):

		self.menuFileNewProj = QtGui.QAction("&New Project",self)
		self.menuFileNewProj.setShortcut("Ctrl+N")
		self.menuFileNewProj.triggered.connect(self.newProject)
		self.menuFile.addAction(self.menuFileNewProj)

		self.menuFile.addSeparator()

		self.menuFileOpenProj = QtGui.QAction("&Open Project",self)
		self.menuFileOpenProj.setShortcut("Ctrl+O")
		self.menuFileOpenProj.triggered.connect(self.openProject)
		self.menuFile.addAction(self.menuFileOpenProj)

		self.menuFileOpenO = QtGui.QAction("&Import OpenQL",self)
		self.menuFileOpenO.triggered.connect(self.importOpenql)
		self.menuFile.addAction(self.menuFileOpenO)
		self.menuFileOpenO.setEnabled(False)

		self.menuFileOpenQ = QtGui.QAction("&Import QASM",self)
		self.menuFileOpenQ.triggered.connect(self.importQasm)
		self.menuFile.addAction(self.menuFileOpenQ)
		self.menuFileOpenQ.setEnabled(False)

		self.menuFileOpenC = QtGui.QAction("&Import QCircuit",self)
		self.menuFileOpenC.triggered.connect(self.TBD)
		self.menuFile.addAction(self.menuFileOpenC)
		self.menuFileOpenC.setEnabled(False)							# (TBD)

		self.menuFile.addSeparator()

		self.menuFileSaveP = QtGui.QAction("&Save Project",self)
		self.menuFileSaveP.setShortcut("Ctrl+S")
		self.menuFileSaveP.triggered.connect(self.saveProject)
		self.menuFile.addAction(self.menuFileSaveP)
		self.menuFileSaveP.setEnabled(False)

		self.menuFileSaveO = QtGui.QAction("&Export OpenQL",self)
		self.menuFileSaveO.triggered.connect(self.exportOpenql)
		self.menuFile.addAction(self.menuFileSaveO)
		self.menuFileSaveO.setEnabled(False)

		self.menuFileSaveQ = QtGui.QAction("&Export QASM",self)
		self.menuFileSaveQ.triggered.connect(self.exportQasm)
		self.menuFile.addAction(self.menuFileSaveQ)
		self.menuFileSaveQ.setEnabled(False)

		self.menuFileSaveC = QtGui.QAction("&Export QCircuit",self)
		self.menuFileSaveC.triggered.connect(self.TBD)
		self.menuFile.addAction(self.menuFileSaveC)
		self.menuFileSaveC.setEnabled(False)							# (TBD)

		self.menuFileExport = QtGui.QAction("&Export QCircuit Image",self)
		self.menuFileExport.triggered.connect(self.exportQCircImg)
		self.menuFile.addAction(self.menuFileExport)
		self.menuFileExport.setEnabled(False)

		self.menuFile.addSeparator()

		self.menuFileExit = QtGui.QAction("&Exit",self)
		self.menuFileExit.setShortcut("Ctrl+Q")
		self.menuFileExit.triggered.connect(self.closeApp)
		self.menuFile.addAction(self.menuFileExit)

	def closeApp(self):
		if self.saved == 0:
			choice = QtGui.QMessageBox.question(self,'sanity check',"Quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
			if choice == QtGui.QMessageBox.Yes:
				sys.exit()
			else:
				pass

	def newProject(self):

		self.dirProj = str(QtGui.QFileDialog.getExistingDirectory(self,'New Project Directory'))
		self.nameProj = self.dirProj[self.dirProj.rindex('/')+1:]
		self.configProj = {'name':self.nameProj}
		self.configProj.update({'path':self.dirProj})
		self.centerLayout()
		file = open(self.fileQCirc,'w')
		file.write("")
		file.close()

	def saveProject(self):

		self.configProjJson = self.dirProj+'/'+self.nameProj+'.qide'
		with open(self.configProjJson,'w') as file:
			json.dump(self.configProj,file,indent=2)
		file.close()

		self.saveOpenql()
		self.saveQasm()

	def saveOpenql(self):

		file = open(self.fileOpenql,'w')
		text = self.textOpenql.toPlainText()
		file.write(text)
		file.close()

	def saveQasm(self):

		file = open(self.fileQasm,'w')
		text = self.textQasm.toPlainText()
		file.write(text)
		file.close()

	def openProject(self):

		self.configProjJson = QtGui.QFileDialog.getOpenFileName(self,'Open QuIDE Project File','',"*.qide")
		print(self.configProjJson)
		pathCnfg = str(self.configProjJson)
		self.dirProj = pathCnfg[:pathCnfg.rindex('/')]
		nameCnfg = pathCnfg[pathCnfg.rindex('/')+1:]
		self.nameProj = nameCnfg[:nameCnfg.rindex('.')]	
		self.configProj = {'name':self.nameProj}
		self.configProj.update({'path':self.dirProj})
		self.centerLayout()
		self.openOpenql()
		self.openQasm()
		self.openQcirc()

	def openOpenql(self):
		
		file = open(self.fileOpenql,'r')
		with file:
			text = file.read()
			self.textOpenql.setText(text)

	def openQasm(self):

		file = open(self.fileQasm,'r')
		with file:
			text = file.read()
			self.textQasm.setText(text)

	def openQcirc(self):

		self.circReset()
		gates = len(self.gateNames)
		file = open(self.fileQCirc,'r')
		self.drawMaxQ = 1	# For drawing measure and display, if circuit was not executed before
		for line in iter(file):

			# Qubits
			ptrn = re.compile('^qubits\s(\d+)',re.IGNORECASE)
			mtch = ptrn.search(line)
			if mtch != None:
				self.drawMaxQ = int(mtch.group(1))

			# Single Qubit Gates
			for g in range(0,9):
				ptrn = re.compile('^\s*'+self.gateNames[g]+'\sq(\d+)',re.IGNORECASE)
				mtch = ptrn.search(line)
				if mtch != None:
					self.circGate(g,[int(mtch.group(1))])
			# Two Qubit Gates
			ptrn = re.compile("cnot"+'\sq(\d+),q(\d+)',re.IGNORECASE)
			mtch = ptrn.search(line)
			if mtch != None:
				self.circGate(9,[int(mtch.group(1)),int(mtch.group(2))])
			# Three Qubit Gates
			ptrn = re.compile("toffoli"+'\sq(\d+),q(\d+),q(\d+)',re.IGNORECASE)
			mtch = ptrn.search(line)
			if mtch != None:
				self.circGate(11,[int(mtch.group(1)),int(mtch.group(2)),int(mtch.group(3))])
			# Measure
			ptrn = re.compile("measure")
			mtch = ptrn.search(line)
			if mtch != None:
				self.circGate(12,[0])
			# Display
			ptrn = re.compile("display")
			mtch = ptrn.search(line)
			if mtch != None:
				self.circGate(13,[0])
		# self.circuit.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)

	def importOpenql(self):

		name = QtGui.QFileDialog.getOpenFileName(self,'Import OpenQL File','',"*.py")
		file = open(name,'r')
		with file:
			text = file.read()
			self.textOpenql.setText(text)			

	def importQasm(self):

		name = QtGui.QFileDialog.getOpenFileName(self,'Import QASM File','',"*.qasm")
		file = open(name,'r')
		with file:
			text = file.read()
			self.textQasm.setText(text)

	def exportOpenql(self):
		
		name = QtGui.QFileDialog.getSaveFileName(self,'Export OpenQL File','',"*.py")
		file = open(name,'w')
		text = self.textOpenql.toPlainText()
		file.write(text)
		file.close()
		
	def exportQasm(self):
		
		name = QtGui.QFileDialog.getSaveFileName(self,'Export QASM File','',"*.qasm")
		file = open(name,'w')
		text = self.textQasm.toPlainText()
		file.write(text)
		file.close()

	def exportQCircImg(self):
		
		name = QtGui.QFileDialog.getSaveFileName(self,'Export Circuit Image','',"*.png")
		pixmap = QtGui.QPixmap(self.qcircuit.sceneRect().width(),self.qcircuit.sceneRect().height())
		painter = QtGui.QPainter(pixmap)
		painter.setRenderHint(QtGui.QPainter.Antialiasing)
		self.qcircuit.render(painter)
		painter.end()
		pixmap.save(name)

	#~~~~~~~~~~~~~~~~~~~~~~~~~ view menu ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def viewMenu(self):
	
		self.menuViewThemes = QtGui.QMenu("&Themes",self)
		self.menuView.addMenu(self.menuViewThemes)

		qtactn = QtGui.QAction("gtk+",self.menuViewThemes)
		qtactn.triggered.connect(lambda: QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("gtk+")))
		self.menuViewThemes.addAction(qtactn)

		qtactn = QtGui.QAction("motif",self.menuViewThemes)
		qtactn.triggered.connect(lambda: QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("motif")))
		self.menuViewThemes.addAction(qtactn)
		
		qtactn = QtGui.QAction("plastique",self.menuViewThemes)
		qtactn.triggered.connect(lambda: QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("plastique")))
		self.menuViewThemes.addAction(qtactn)
		
		qtactn = QtGui.QAction("windows",self.menuViewThemes)
		qtactn.triggered.connect(lambda: QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("windows")))
		self.menuViewThemes.addAction(qtactn)
		
		qtactn = QtGui.QAction("cleanlooks",self.menuViewThemes)
		qtactn.triggered.connect(lambda: QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("cleanlooks")))
		self.menuViewThemes.addAction(qtactn)
		
		qtactn = QtGui.QAction("cde",self.menuViewThemes)
		qtactn.triggered.connect(lambda: QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("cde")))
		self.menuViewThemes.addAction(qtactn)

	#~~~~~~~~~~~~~~~~~~~~~~~~~ help menu ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def helpMenu(self):

		self.menuHelpTutorial = QtGui.QMenu("&Learn",self)
		self.menuHelp.addMenu(self.menuHelpTutorial)

		qtactn = QtGui.QAction("&QuIDE and QCirc",self.menuViewThemes)
		qtactn.triggered.connect(self.learnQuide)
		self.menuHelpTutorial.addAction(qtactn)

		qtactn = QtGui.QAction("&OpenQL",self.menuViewThemes)
		qtactn.triggered.connect(self.learnOpenql)
		self.menuHelpTutorial.addAction(qtactn)

		qtactn = QtGui.QAction("&QX-Sim",self.menuViewThemes)
		qtactn.triggered.connect(self.learnQxsim)
		self.menuHelpTutorial.addAction(qtactn)

		self.menuHelp.addSeparator()
		
		self.menuHelpRelease = QtGui.QAction("&Release Notes",self)
		self.menuHelpRelease.triggered.connect(self.TBD)
		self.menuHelp.addAction(self.menuHelpRelease)
		self.menuHelpRelease.setEnabled(False)				# (TBD)
		
		self.menuHelpUpdate = QtGui.QAction("&Update",self)
		self.menuHelpUpdate.triggered.connect(self.TBD)
		self.menuHelp.addAction(self.menuHelpUpdate)
		self.menuHelpUpdate.setEnabled(False)				# (TBD)
		
		self.menuHelp.addSeparator()
		
		self.menuHelpLicense = QtGui.QAction("&License",self)
		self.menuHelpLicense.triggered.connect(self.license)
		self.menuHelp.addAction(self.menuHelpLicense)
		
		self.menuHelpAbout = QtGui.QAction("&About",self)
		self.menuHelpAbout.triggered.connect(self.about)
		self.menuHelp.addAction(self.menuHelpAbout)

	def learnQuide(self):

		QtGui.QMessageBox.about(self,"Learn QuIDE & QCirc","Visit : https://gitlab.com/prince-ph0en1x/QIDE")

	def learnOpenql(self):

		QtGui.QMessageBox.about(self,"Learn OpenQL","Visit : https://gitlab.com/qutech-ce/openql")

	def learnQxsim(self):

		QtGui.QMessageBox.about(self,"Learn OpenQL","Visit : https://gitlab.com/qutech-ce/qx-simulator")

	def license(self):

		QtGui.QMessageBox.about(self,"License",open("license.txt",'r').read())

	def about(self):

		QtGui.QMessageBox.about(self,"About",open("about.txt",'r').read())

	#~~~~~~~~~~~~~~~~~~~~~~~~~ shortcuts ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def quickaccess(self):

		self.toolBar = self.addToolBar("QuickAccess")

		extractAction = QtGui.QAction(QtGui.QIcon('icons/plot5.png'),'Custom Plot',self)
		extractAction.triggered.connect(self.TBD)
		self.toolBar.addAction(extractAction)
		extractAction.setEnabled(False)

		extractAction = QtGui.QAction(QtGui.QIcon('icons/layout3.png'),'Custom Layout',self)
		extractAction.triggered.connect(self.TBD)
		self.toolBar.addAction(extractAction)
		extractAction.setEnabled(False)
		
		extractAction = QtGui.QAction(QtGui.QIcon('icons/uc3.png'),'View Microcode',self)
		extractAction.triggered.connect(self.TBD)
		self.toolBar.addAction(extractAction)
		extractAction.setEnabled(False)
		
	########################## MAIN LAYOUT ##########################

	def centerLayout(self):

		self.menuFileSaveP.setEnabled(True)
		self.stsmsg.showMessage('Current Project Directory : '+self.dirProj)
		self.fileOpenql = self.dirProj+"/"+self.nameProj+".py"
		self.fileQasm = self.dirProj+"/"+self.nameProj+".qasm"
		self.fileQCirc = self.dirProj+"/"+self.nameProj+".qcir"
		
		self.centralWidget = QtGui.QWidget(self)
		self.setCentralWidget(self.centralWidget)
		self.topLayoutV = QtGui.QVBoxLayout(self.centralWidget)
		
		self.topLayoutH1 = QtGui.QHBoxLayout()
		self.openqlEditor()
		self.qasmEditor()
		self.topLayoutV.addLayout(self.topLayoutH1,QtCore.Qt.AlignBottom)
		
		self.topLayoutH2 = QtGui.QHBoxLayout()
		self.gateset()
		self.circuitEditor()
		self.resultTabs()     
		self.topLayoutV.addLayout(self.topLayoutH2,QtCore.Qt.AlignBottom)

		self.menuFileOpenO.setEnabled(True)
		self.menuFileOpenQ.setEnabled(True)
		# self.menuFileOpenC.setEnabled(True)
		self.menuFileSaveO.setEnabled(True)
		self.menuFileSaveQ.setEnabled(True)
		# self.menuFileSaveC.setEnabled(True)
		self.menuFileExport.setEnabled(True)

	#~~~~~~~~~~~~~~~~~~~~~~~~~ openql ed ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def openqlEditor(self):

		self.topLayoutH1.addSpacing(90) 
		
		self.textOpenql = QtGui.QTextEdit(self)
		self.textOpenql.setFixedSize(990,415)
		self.textOpenql.setText("OpenQL Editor")
		self.topLayoutH1.addWidget(self.textOpenql,QtCore.Qt.AlignRight)

		self.btnLayoutOQ = QtGui.QVBoxLayout()
		
		self.btnO2Q = QtGui.QPushButton(u"\u2192",self)
		self.btnO2Q.clicked.connect(self.convO2Q)
		self.btnO2Q.setFixedSize(30,30)
		self.btnLayoutOQ.addWidget(self.btnO2Q,0,QtCore.Qt.AlignBottom)

		self.btnQ2O = QtGui.QPushButton(u"\u2190",self)
		self.btnQ2O.clicked.connect(self.TBD)
		self.btnQ2O.setFixedSize(30,30)
		self.btnLayoutOQ.addWidget(self.btnQ2O,QtCore.Qt.AlignBottom)
		self.btnQ2O.setEnabled(False)

		self.btnLayoutOQ.addSpacing(40) 

		self.topLayoutH1.addLayout(self.btnLayoutOQ,QtCore.Qt.AlignCenter)
		self.editorConfig()

	def editorConfig(self):

		# (TBD : Load from project json)
		self.textOpenql.setLineWrapMode(0)
		self.highlight = syntax.PythonHighlighter(self.textOpenql.document())
		self.textOpenql.setTabStopWidth(40)
		self.textOpenql.setFontFamily("Monospace")

	def convO2Q(self):   

		self.saveOpenql()
		self.saveQasm()		# current QASM backup
		os.system("python3 "+self.fileOpenql+" > "+self.dirProj+"/"+"logO2Q.txt 2>&1")
		name = "test_output/qg.qasm"       # (TBD: get output file name from openql)
		file = open(name,'r')
		with file:
			text = file.read()
			self.textQasm.setText(text)
		file.close()
		text = open(self.dirProj+"/"+"logO2Q.txt",'r').read()
		self.textLog.setText(text)
		self.tabLayout.setCurrentWidget(self.textLog)

	#~~~~~~~~~~~~~~~~~~~~~~~~~ qasm ed ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def qasmEditor(self):

		self.qasmLayout = QtGui.QVBoxLayout()
		
		self.textQasm = QtGui.QTextEdit(self)
		self.textQasm.setFixedSize(460,380)
		self.textQasm.setText("QASM Editor")
		self.textQasm.setLineWrapMode(0)
		self.qasmLayout.addWidget(self.textQasm,0,QtCore.Qt.AlignRight)

		self.btnLayoutQ = QtGui.QHBoxLayout()

		self.btnQ2C = QtGui.QPushButton(u"\u2193",self)
		self.btnQ2C.clicked.connect(self.convQ2C)
		self.btnQ2C.setFixedSize(30,30)
		self.btnLayoutQ.addWidget(self.btnQ2C,QtCore.Qt.AlignLeft)
		
		self.btnC2Q = QtGui.QPushButton(u"\u2191",self)
		self.btnC2Q.clicked.connect(self.convC2Q)
		self.btnC2Q.setFixedSize(30,30)
		self.btnLayoutQ.addWidget(self.btnC2Q,QtCore.Qt.AlignLeft)
		
		self.btnLayoutQ.addSpacing(40) 

		self.btnQ2G = QtGui.QPushButton(u"\u2193",self)
		self.btnQ2G.clicked.connect(self.convQ2G)
		self.btnQ2G.setFixedSize(30,30)
		self.btnLayoutQ.addWidget(self.btnQ2G,0,QtCore.Qt.AlignLeft)
		
		self.qasmLayout.addLayout(self.btnLayoutQ,QtCore.Qt.AlignRight)

		self.topLayoutH1.addLayout(self.qasmLayout,QtCore.Qt.AlignRight)

	def convQ2G(self):

		self.saveQasm()
		os.system("./qx_simulator_1.0.beta_linux_x86_64 "+self.fileQasm+" > "+self.dirProj+"/"+"logQ2G.txt")
		file = open(self.dirProj+"/"+"logQ2G.txt",'r')
		self.plotOutput(file)
		file.close()
		text = open(self.dirProj+"/"+"logQ2G.txt",'r').read()
		self.textLog.setText(text)
		self.tabLayout.setCurrentWidget(self.textLog)

	def convQ2C(self):
		
		self.saveQasm()
		file = open(self.fileQasm,'r')
		with file:
			text = file.read()
		file.close()
		file = open(self.fileQCirc,'w')
		file.write(text)
		file.close()
		self.openQcirc()
		
	#~~~~~~~~~~~~~~~~~~~~~~~~~ qcircuit ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def circuitEditor(self):

		penG = QtGui.QPen(QtCore.Qt.blue)
		fill = QtGui.QBrush(QtCore.Qt.cyan)

		self.qcircuit = QtGui.QGraphicsScene()
		self.qcircuit.setBackgroundBrush(QtCore.Qt.white)

		self.btnLayoutC = QtGui.QHBoxLayout()

		self.circuit = QtGui.QGraphicsView(self.qcircuit)
		self.circuit.setFixedSize(1100,420)
		# self.circuit.mousePressEvent = self.pixelSelect
		self.btnLayoutC.addWidget(self.circuit,QtCore.Qt.AlignLeft)
		self.circReset()
		
		self.btnC2G = QtGui.QPushButton(u"\u2192",self)
		self.btnC2G.clicked.connect(self.convC2G)
		self.btnC2G.setFixedSize(30,30)
		self.btnLayoutC.addWidget(self.btnC2G,0,QtCore.Qt.AlignTop)

		self.topLayoutH2.addLayout(self.btnLayoutC,QtCore.Qt.AlignLeft)

	def circReset(self):

		for item in self.qcircuit.items():
			self.qcircuit.removeItem(item)
		pen = QtGui.QPen(QtCore.Qt.black)
		qubits = 50
		for i in range(0,qubits):
			t = self.qcircuit.addText("q["+str(i)+"]")
			t.setPos(0,i*40)
			self.qcircuit.addLine(QtCore.QLineF(50,i*40+12,80,i*40+12),pen)
		self.circTick = 0 
		self.circuit.centerOn(QtCore.QPointF(0,0))
		# self.qcircuit.addEllipse(QtCore.QRectF(0,0,10,10),QtCore.Qt.black,QtCore.Qt.black)

	def gateset(self):
		
		gsz = 39
		bsz = gsz - 0
		gsr = self.win_ry/2 + gsz/2 + 5
		gsc = 10 
		self.btn_g = {}
		self.btnLayoutGates = QtGui.QGridLayout()
		comboBox = QtGui.QComboBox(self)
		for gs in range(0,len(self.gateSets)):
			comboBox.addItem(self.gateSets[gs])      
		comboBox.setFixedSize(2*gsz+5,gsz)
		comboBox.activated[str].connect(self.gateEnbl)
		self.btnLayoutGates.addWidget(comboBox,0,0,1,2,QtCore.Qt.AlignTop)
		gsr = gsr+gsz  
		gr = 0
		gc = 0
		gates = len(self.gateNames)
		for g in range(0,gates):
			self.btn_g[g] = QtGui.QPushButton(self.gateNames[g],self)
			self.btn_g[g].setFixedSize(bsz,bsz-15)
			self.btnLayoutGates.addWidget(self.btn_g[g],g/2+1,g%2,QtCore.Qt.AlignTop)
			gc = (gc + 1)%2
			if gc == 0:
				gr = gr + 1
		self.btn_g[0].clicked.connect(lambda: self.circSelGate(0))
		self.btn_g[1].clicked.connect(lambda: self.circSelGate(1))
		self.btn_g[2].clicked.connect(lambda: self.circSelGate(2))
		self.btn_g[3].clicked.connect(lambda: self.circSelGate(3))
		self.btn_g[4].clicked.connect(lambda: self.circSelGate(4))
		self.btn_g[5].clicked.connect(lambda: self.circSelGate(5))
		self.btn_g[6].clicked.connect(lambda: self.circSelGate(6))
		self.btn_g[7].clicked.connect(lambda: self.circSelGate(7))
		self.btn_g[8].clicked.connect(lambda: self.circSelGate(8))
		self.btn_g[9].clicked.connect(lambda: self.circSelGate(9))
		self.btn_g[10].clicked.connect(lambda: self.circSelGate(10))
		self.btn_g[11].clicked.connect(lambda: self.circSelGate(11))
		self.btn_g[12].clicked.connect(lambda: self.circSelGate(12))
		self.btn_g[13].clicked.connect(lambda: self.circSelGate(13))
		
		g = gates 
		self.btnGDel = QtGui.QPushButton(u"\u2700",self)
		#self.btnGDel = QtGui.QPushButton(QtGui.QIcon("icons/del1.png"),'',self)
		self.btnGDel.setFixedSize(bsz,bsz)
		self.btnLayoutGates.addWidget(self.btnGDel,g/2+1,g%2,QtCore.Qt.AlignTop)
		self.btnGDel.clicked.connect(self.delGate)

		g = g+1 
		#self.btnGNew = QtGui.QPushButton(u"\U0001F441",self)
		self.btnGNew = QtGui.QPushButton(QtGui.QIcon("icons/cg.png"),'',self)
		self.btnGNew.setFixedSize(bsz,bsz)
		self.btnLayoutGates.addWidget(self.btnGNew,g/2+1,g%2,QtCore.Qt.AlignTop)
		self.btnGNew.clicked.connect(self.makeGate)

		g = g+1
		comboBox = QtGui.QComboBox(self)
		for gs in range(0,5):
			comboBox.addItem("Cust. G"+str(gs))      
		comboBox.setFixedSize(2*gsz+5,gsz)
		comboBox.activated[str].connect(self.TBD)
		self.btnLayoutGates.addWidget(comboBox,g/2+1,g%2,1,2,QtCore.Qt.AlignTop)

		self.topLayoutH2.addLayout(self.btnLayoutGates,QtCore.Qt.AlignLeft)
	
	def delGate(self):

		self.qcircuit.mousePressEvent = self.getDelGate
		return

	def getDelGate(self,event):

		beg = 80
		xsp = 50
		ysp = 40
		pos = QtCore.QPointF(event.scenePos())
		
		#qb = round((pos.y()-12)/ysp)
		tk = round((pos.x() - beg - xsp/4)/xsp)

		file = open(self.fileQCirc,'r+')
		lines = file.readlines()
		file.close()
		
		file = open(self.fileQCirc,'w')
		lno = 0
		for line in lines:
			if lno != int(tk)+1:
				file.write(line)
			lno = lno + 1
		file.close()
		self.openQcirc()

	def makeGate(self):

		# enable drag box
		# self.circuit.dropEvent = self.lol
		# print("hi")
		# print(self.circuit.QGraphicsSceneDragDropEvent.pos())

		self.makeGateBound = []
		self.qcircuit.mousePressEvent = self.getGateBound
		return

	def getGateBound(self,event):

		beg = 80
		xsp = 50
		ysp = 40
		pos = QtCore.QPointF(event.scenePos())
		
		qb = round((pos.y()-12)/ysp)
		tk = round((pos.x() - beg - xsp/4)/xsp)

		self.delGateLno = tk
		print([qb,tk])

	def gateEnbl(self,set):

		gs = 0
		for i in range(0,len(self.gateSets)):
			if set == self.gateSets[i]:
				gs = i
				break
		for g in range(0,len(self.gateMasks[0])):
			if self.gateMasks[gs][g] == '1':
				self.btn_g[g].setEnabled(True)
			else:
				self.btn_g[g].setEnabled(False)

	def circSelGate(self,gateId):

		self.drawGate = gateId
		self.drawGateQ = []
		# self.circuit.setDragMode(QtGui.QGraphicsView.NoDrag)
		self.qcircuit.mousePressEvent = self.pixelSelect
	
# LOGIC RESIDES WHERE WE THINK IT RESIDES
# UNIVERSE EVOLVED INTELLIGENCE TO REDISCOVER ITSELF

# IF WE ARE THE CENTRE OF OUR FRAME OF REFERENCE, WHY DO WE NEED TO USE ENERGY
# DREAM IS THE ILLUSION (MAYA) AND THE URGE TO BE IN IT IS THE DESIRE (MOH)
# THE INFORMATIONAL DIFFERENCE BETWEEN A SARCASTIC AND NORMAL ANSWER IS 0, YET IT CAN TRANSMIT 1 SHANNON BIT OF INFORMATION TO THE RECEIVER


	def pixelSelect(self, event):

		# undo/redo gate button
		# drag toggle button
		# make new kernel button
		# make new unitary button
		# insert custom kernel/unitary button

		
		file = open(self.fileQCirc,'r+')
		content = file.read()
		ptrn = re.compile('qubits')
		mtch = ptrn.search(content)
		if mtch == None:
			file.seek(0, 0)
			file.write("qubits "+str(int(self.drawMaxQ))+"\n" + content)
		file.close()

		file = open(self.fileQCirc,'a')
		ysp = 40
		qb = math.floor(event.scenePos().y()/ysp)
		self.drawGateQ.append(qb)
		if self.drawGate < 9:
			if len(self.drawGateQ) == 1:
				self.circGate(self.drawGate,self.drawGateQ)
				file.write(self.gateCodes[self.drawGate]+" q"+str(int(self.drawGateQ[0]))+"\n")
				# self.circuit.mousePressEvent = None
				# self.circuit.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
		elif self.drawGate == 9:	# CNOT
			if len(self.drawGateQ) == 2:
				self.circGate(self.drawGate,self.drawGateQ)
				file.write(self.gateCodes[self.drawGate]+" q"+str(int(self.drawGateQ[0]))+",q"+str(int(self.drawGateQ[1]))+"\n")
		elif self.drawGate == 11:	# Toffoli
			if len(self.drawGateQ) == 3:
				self.circGate(self.drawGate,self.drawGateQ)
				file.write(self.gateCodes[self.drawGate]+" q"+str(int(self.drawGateQ[0]))+",q"+str(int(self.drawGateQ[1]))+",q"+str(int(self.drawGateQ[2]))+"\n")
		elif self.drawGate >= 12:
			if len(self.drawGateQ) == 1:
				self.circGate(self.drawGate,self.drawGateQ)
				file.write(self.gateCodes[self.drawGate]+"\n")
		file.close()

	def circGate(self,gateId,qbset):

		beg = 80
		xsp = 50
		ysp = 40

		for i in range (0,len(qbset)):
		 	if qbset[i]+1 > self.drawMaxQ:
				self.drawMaxQ = qbset[i]+1

		pen = QtGui.QPen(QtCore.Qt.black)
		qubits = 50
		for i in range(0,qubits):
			self.qcircuit.addLine(QtCore.QLineF(beg+xsp*self.circTick,i*40+12,beg+xsp*(self.circTick+1),i*40+12),pen)
		
		penG = QtGui.QPen(QtCore.Qt.gray)
		fill = QtGui.QBrush(QtCore.Qt.cyan)
		rsz = 24
		csz = 14
		if gateId < 9:
			qbt = qbset[0]
			self.qcircuit.addRect(QtCore.QRectF(beg+xsp*self.circTick,ysp*qbt,rsz,rsz),penG,fill)
			t = self.qcircuit.addText(self.gateNames[gateId])
			t.setPos(beg+xsp*self.circTick+4,ysp*qbt)
		elif gateId == 9:
			qbc1 = qbset[0]
			qbt = qbset[1]
			self.qcircuit.addLine(QtCore.QLineF(beg+xsp*self.circTick+5+7,ysp*qbc1+5+7,beg+xsp*self.circTick+12,ysp*qbt+12),penG)
			self.qcircuit.addEllipse(QtCore.QRectF(beg+xsp*self.circTick+(rsz-csz)/2,ysp*qbc1+(rsz-csz)/2,csz,csz),penG,QtCore.Qt.black)
			self.qcircuit.addRect(QtCore.QRectF(beg+xsp*self.circTick,ysp*qbt,rsz,rsz),penG,fill)
			t = self.qcircuit.addText("X")
			t.setPos(beg+xsp*self.circTick+4,ysp*qbt)
		elif gateId == 11:
			qbc2 = qbset[0]
			qbc1 = qbset[1]
			qbt = qbset[2]
			self.qcircuit.addLine(QtCore.QLineF(beg+xsp*self.circTick+5+7,ysp*qbc1+5+7,beg+xsp*self.circTick+12,ysp*qbt+12),penG)
			self.qcircuit.addLine(QtCore.QLineF(beg+xsp*self.circTick+5+7,ysp*qbc2+5+7,beg+xsp*self.circTick+12,ysp*qbt+12),penG)
			self.qcircuit.addEllipse(QtCore.QRectF(beg+xsp*self.circTick+(rsz-csz)/2,ysp*qbc1+(rsz-csz)/2,csz,csz),penG,QtCore.Qt.black)
			self.qcircuit.addEllipse(QtCore.QRectF(beg+xsp*self.circTick+(rsz-csz)/2,ysp*qbc2+(rsz-csz)/2,csz,csz),penG,QtCore.Qt.black)
			self.qcircuit.addRect(QtCore.QRectF(beg+xsp*self.circTick,ysp*qbt,rsz,rsz),penG,fill)
			t = self.qcircuit.addText("X")
			t.setPos(beg+xsp*self.circTick+4,ysp*qbt)
		elif gateId >= 12:		# Display
			if gateId == 13:
				fill = QtGui.QBrush(QtCore.Qt.green)
			self.qcircuit.addRect(QtCore.QRectF(beg+xsp*self.circTick,ysp*0,rsz,ysp*int(self.drawMaxQ-1)+rsz),penG,fill)
			for qbt in range(0,int(self.drawMaxQ)):
				t = self.qcircuit.addText(self.gateNames[gateId])
				t.setPos(beg+xsp*self.circTick+1,ysp*qbt)
		pen.setStyle(QtCore.Qt.DotLine)
		self.qcircuit.addLine(QtCore.QLineF(beg+xsp*self.circTick-xsp/4,0,beg+xsp*self.circTick-xsp/4,ysp*qubits-ysp/4),pen)
		self.circTick = self.circTick + 1   # allow parallel scheduling
	
	def convC2Q(self):

		file = open(self.fileQCirc,'r')
		with file:
			text = file.read()
			self.textQasm.setText(text)
		file.close()

	def convC2G(self):

		file = open(self.fileQCirc,'r+')
		content = file.read()
		file.close()
		ptrn = re.compile('^qubits\s(\d+)',re.IGNORECASE)
		mtch = ptrn.search(content)
		if mtch == None:
			file = open(self.fileQCirc,'r+')
			file.seek(0, 0)
			file.write("qubits "+str(int(self.drawMaxQ))+"\n" + content)
			file.close()
		else:
			file = open(self.fileQCirc,'r+')
			lines = file.readlines()
			file.close()
			file = open(self.fileQCirc,'w')
			for line in lines:
				mtch = ptrn.search(line)
				if mtch == None:
					file.write(line)
			file.close()
			file = open(self.fileQCirc,'r+')
			content = file.read()
			file.seek(0, 0)
			file.write("qubits "+str(int(self.drawMaxQ))+"\n" + content)
			file.close()
		os.system("./qx_simulator_1.0.beta_linux_x86_64 "+self.fileQCirc+" > "+self.dirProj+"/"+"logC2G.txt")
		file = open(self.dirProj+"/"+"logC2G.txt",'r')
		self.plotOutput(file)
		file.close()
		text = open(self.dirProj+"/"+"logC2G.txt",'r').read()
		self.textLog.setText(text)
		self.tabLayout.setCurrentWidget(self.textLog)

	#~~~~~~~~~~~~~~~~~~~~~~~~~ results ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def resultTabs(self):

		tsz = 325

		self.figure = Figure()
		self.graphres = FigureCanvas(self.figure)
		self.graphres.setFixedSize(tsz,tsz)

		self.toolbar = NavigationToolbar(self.graphres, self)
		self.toolbar.setFixedSize(tsz,25)

		self.qcoutputw = QtGui.QWidget() 
		
		self.qcoutput = QtGui.QVBoxLayout(self.qcoutputw)
		self.qcoutput.addWidget(self.toolbar)
		self.qcoutput.addWidget(self.graphres)
		
		self.textLog = QtGui.QTextEdit(self)
		self.textLog.setFixedSize(343,388)
		self.textLog.setText("Run Logs")
		self.textLog.setLineWrapMode(0)
		self.textLog.setFontFamily("Monospace")

		# self.scene1 = QtGui.QGraphicsScene()
		# self.qclayout = QtGui.QGraphicsView(self.scene1)
		# self.qclayout.setFixedSize(tsz,tsz)
		# self.pixmap_item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap('topologies/surface17a.png').scaled(tsz,tsz), None, self.scene1)

		self.tabLayout = QtGui.QTabWidget(self)
		self.tabLayout.addTab(self.qcoutputw,"Output")
		self.tabLayout.addTab(self.textLog,"Logs")
		
		self.topLayoutH2.addWidget(self.tabLayout,0,QtCore.Qt.AlignRight)

	def plotOutput(self,file):

		qbno = 0
		ptrn = re.compile('(\d*)\squbits')
		for line in iter(file):
			mtch = ptrn.search(line)
			if mtch != None:
				qbno = int(mtch.group(1))
				break
		ploty = [0]*(2**qbno)
		ptrn = re.compile('\(([+-]\d+.\d*),([+-]\d+.\d*)\)\s[|]([0-1]*)>')
		for line in iter(file):
			mtch = ptrn.search(line)
			if mtch != None:
				x = float(mtch.group(1))
				y = float(mtch.group(2))
				state = int(mtch.group(3),2) 
				ploty[state] = x #x**2 + y**2      # check, sqrt reqd? OR z.z'
		cstmPloty = customPlot(ploty)
		#return
		ax = self.figure.add_subplot(1,1,1)   
		ax.clear()
		#ax.plot(cstmPloty, '*-r')
		ax.bar(range(len(cstmPloty)),cstmPloty)
		ax.set_xlim([0,len(cstmPloty)])
		ax.tick_params(axis='x',labelbottom='off')
		ax.set_ylim([-1,1])
		self.graphres.draw()

	########################## LEGACIES ##########################

	def color_picker(self):

		color = QtGui.QColorDialog.getColor()
		self.penColor = color
		# self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

	def TBD(self):

		print("TBD")

app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())

## TODOs: FEATURES

'''
* Allow Topology Definition
* Save circuit as functional blocks
* Autouncompute
* Statistical graphs
'''

## TODOs: UI

'''
* Change toolbox to Layout
* Show/Hide Toolbar
* Tab width in TextEdit
* QASM syntax highlighting
* LineNUmbers to textedit
'''

## TODOs: KNOWN ISSUES

'''
* drawMaxQ not getting updated on project load
'''