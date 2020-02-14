# Test circuit builder

# TBD
'''
* OpenQL not working from executable
* Window resize dynamic
* Minimum button size 30x30
* Make filenames local, only cnfg proj class
'''

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

import os
import json
import syntax
import syntax_cqasm

# PATH_QX = '/media/sf_QWorld/dev_tools_QCA/qx-simulator-bug-ckt-accumulation-qxelerator-72/build/bin/qx-simulator'
test_path = os.path.dirname(os.path.realpath(__file__))						# Get the path of this python code file
quine_path = os.path.dirname(test_path)
PATH_QX = os.path.join(quine_path, 'qx-simulator')

USER_MODE = True

class Window(QtWidgets.QMainWindow):
		
	def __init__(self):

		screen = app.primaryScreen()
		# print('Screen: %s' % screen.name())
		# size = screen.size()	# Size of monitor
		rect = screen.availableGeometry() # Usable size for OS
		self.win_cx = rect.width()
		self.win_ry = rect.height()

		super(Window,self).__init__()
		self.setGeometry(0,0,self.win_cx,self.win_ry)

		self.setWindowTitle("Quantum Innovation Environment")
		
		self.setWindowIcon(QtGui.QIcon('icons/app.png'))
		
		self.stsmsg = self.statusBar()
		self.stsmsg.showMessage('Create new project or Open existing project')

		self.layout = False
		self.saved = 1

		self.menu()
		
		self.show()

	########################## MAIN MENUS ##########################

	def menu(self):

		self.mainMenu = self.menuBar()
		
		self.menuFile = self.mainMenu.addMenu('&File')
		self.fileMenu()
		
		self.menuHelp = self.mainMenu.addMenu('&Help')
		self.helpMenu()
		
		self.menuDev = self.mainMenu.addMenu('&Nightly Sandbox')
		self.devMenu()
		if USER_MODE:
			self.menuDev.setEnabled(False)

	#~~~~~~~~~~~~~~~~~~~~~~~~~ file menu ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def fileMenu(self):

		self.menuFileNewProj = QtWidgets.QAction("&New Project",self)
		self.menuFileNewProj.setShortcut("Ctrl+N")
		self.menuFileNewProj.triggered.connect(self.newProject)
		self.menuFile.addAction(self.menuFileNewProj)

		self.menuFileOpenProj = QtWidgets.QAction("&Open Project",self)
		self.menuFileOpenProj.setShortcut("Ctrl+O")
		self.menuFileOpenProj.triggered.connect(self.openProject)
		self.menuFile.addAction(self.menuFileOpenProj)

		self.menuFileSaveProj = QtWidgets.QAction("&Save Project",self)
		self.menuFileSaveProj.setShortcut("Ctrl+S")
		self.menuFileSaveProj.triggered.connect(self.saveProject)
		self.menuFile.addAction(self.menuFileSaveProj)
		self.menuFileSaveProj.setEnabled(False)

		# Save sources: qasm ,openql, qcirc

		self.menuFileCloseProj = QtWidgets.QAction("&Close Project",self)
		# self.menuFileSaveP.setShortcut("Ctrl+X")
		self.menuFileCloseProj.triggered.connect(self.closeProject)
		self.menuFile.addAction(self.menuFileCloseProj)
		self.menuFileCloseProj.setEnabled(False)

		self.menuFile.addSeparator()

		self.menuFileNewO = QtWidgets.QAction("&New OpenQL",self)
		self.menuFileNewO.triggered.connect(self.createOpenql)
		self.menuFile.addAction(self.menuFileNewO)
		self.menuFileNewO.setEnabled(False)

		self.menuFileNewQ = QtWidgets.QAction("&New cQASM",self)
		self.menuFileNewQ.triggered.connect(self.createQasm)
		self.menuFile.addAction(self.menuFileNewQ)
		self.menuFileNewQ.setEnabled(False)

		self.menuFileNewC = QtWidgets.QAction("&New QCircuit",self)
		# self.menuFileOpenC.triggered.connect(self.TBD)
		self.menuFile.addAction(self.menuFileNewC)
		self.menuFileNewC.setEnabled(False)

		self.menuFile.addSeparator()

		self.menuFileImportO = QtWidgets.QAction("&Import OpenQL",self)
		self.menuFileImportO.triggered.connect(self.importOpenql)
		self.menuFile.addAction(self.menuFileImportO)
		self.menuFileImportO.setEnabled(False)

		self.menuFileImportQ = QtWidgets.QAction("&Import cQASM",self)
		self.menuFileImportQ.triggered.connect(self.importQasm)
		self.menuFile.addAction(self.menuFileImportQ)
		self.menuFileImportQ.setEnabled(False)

		self.menuFileImportC = QtWidgets.QAction("&Import QCircuit",self)
		# self.menuFileOpenC.triggered.connect(self.TBD)
		self.menuFile.addAction(self.menuFileImportC)
		self.menuFileImportC.setEnabled(False)

		self.menuFile.addSeparator()

		self.menuFileSaveO = QtWidgets.QAction("&Save OpenQL",self)
		self.menuFileSaveO.triggered.connect(self.exportOpenql)
		self.menuFile.addAction(self.menuFileSaveO)
		self.menuFileSaveO.setEnabled(False)

		self.menuFileSaveQ = QtWidgets.QAction("&Save cQASM",self)
		self.menuFileSaveQ.triggered.connect(self.exportQasm)
		self.menuFile.addAction(self.menuFileSaveQ)
		self.menuFileSaveQ.setEnabled(False)

		self.menuFileSaveC = QtWidgets.QAction("&Save QCircuit",self)
		# self.menuFileSaveC.triggered.connect(self.TBD)
		self.menuFile.addAction(self.menuFileSaveC)
		self.menuFileSaveC.setEnabled(False)

		self.menuFileExport = QtWidgets.QAction("&Export Circuit Image",self)
		# self.menuFileExport.triggered.connect(self.exportQCircImg)
		self.menuFile.addAction(self.menuFileExport)
		self.menuFileExport.setEnabled(False)

		self.menuFile.addSeparator()

		self.menuFileExit = QtWidgets.QAction("&Exit",self)
		self.menuFileExit.setShortcut("Ctrl+Q")
		self.menuFileExit.triggered.connect(self.closeApp)
		self.menuFile.addAction(self.menuFileExit)

	def closeApp(self):

		if self.saved == 0:
			choice = QtWidgets.QMessageBox.question(self,'sanity check',"You have unsaved progress. Are you sure you want to quit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
			if choice == QtWidgets.QMessageBox.Yes:
				sys.exit()
			else:
				pass
		else:
			sys.exit()

	#~~~~~~~~~~~~~~~~~~~~~~~~~ Project functions ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def newProject(self):

		self.nameProj, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Create Project")
		if self.nameProj != "":
			self.cnfgProj = {'name':self.nameProj}
			self.cnfgProj.update({'dir':self.nameProj[:self.nameProj.rindex('/')]})
			with open(self.nameProj,'w') as file:
				json.dump(self.cnfgProj,file,indent=2)
			file.close()

			self.menuFileSaveProj.setEnabled(True)
			self.menuFileCloseProj.setEnabled(True)

			self.menuFileNewO.setEnabled(True)
			self.menuFileNewQ.setEnabled(True)
			# self.menuFileNewC.setEnabled(True)

			self.menuFileImportO.setEnabled(True)
			self.menuFileImportQ.setEnabled(True)
			# self.menuFileImportC.setEnabled(True)

			self.menuFileSaveO.setEnabled(True)
			self.menuFileSaveQ.setEnabled(True)
			# self.menuFileSaveC.setEnabled(True)

			if self.layout == False:
				self.centerLayout()
				self.layout = True

			self.saved = 0

	def openProject(self):

		self.nameProj, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open Project")	
		if self.nameProj != "":
			with open(self.nameProj,'r') as file:
				self.cnfgProj = json.load(file)
			file.close()

			self.menuFileSaveProj.setEnabled(True)
			self.menuFileCloseProj.setEnabled(True)

			self.menuFileNewO.setEnabled(True)
			self.menuFileNewQ.setEnabled(True)
			# self.menuFileNewC.setEnabled(True)

			self.menuFileImportO.setEnabled(True)
			self.menuFileImportQ.setEnabled(True)
			# self.menuFileImportC.setEnabled(True)

			self.menuFileSaveO.setEnabled(True)
			self.menuFileSaveQ.setEnabled(True)
			# self.menuFileSaveC.setEnabled(True)

			if self.layout == False:
				self.centerLayout()
				self.layout = True

			if 'name_openql' in self.cnfgProj.keys():
				self.openOpenql()
			if 'name_cqasm' in self.cnfgProj.keys():
				self.openQasm()
			# self.openQcirc()

			self.saved = 0

	def saveProject(self):

		with open(self.cnfgProj['name'],'w') as file:
			json.dump(self.cnfgProj,file,indent=2)
		file.close()

		# self.saveOpenql()
		# self.saveQasm()


	def closeProject(self):

		self.menuFileSaveProj.setEnabled(False)
		self.menuFileCloseProj.setEnabled(False)

		self.menuFileNewO.setEnabled(False)
		self.menuFileNewQ.setEnabled(False)
		# self.menuFileNewC.setEnabled(False)

		self.menuFileImportO.setEnabled(False)
		self.menuFileImportQ.setEnabled(False)
		# self.menuFileImportC.setEnabled(False)

		self.menuFileSaveO.setEnabled(False)
		self.menuFileSaveQ.setEnabled(False)
		# self.menuFileSaveC.setEnabled(False)

		self.textQasm.setText("QASM Editor")
		self.textQasm.setEnabled(False)

		self.textLog.setText("Run Logs")
		self.textLog.setEnabled(False)

		self.textOpenql.setText("OpenQL Editor")
		self.textOpenql.setEnabled(False)

		self.btnQ2G.setEnabled(False)

		self.saved = 1

	#~~~~~~~~~~~~~~~~~~~~~~~~~ cQASM functions ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def createQasm(self):

		self.fileCqasm, _ = QtWidgets.QFileDialog.getSaveFileName(self,'Create cQASM File','',"*.qasm")
		if self.fileCqasm != "":
			self.cnfgProj.update({'name_cqasm':self.fileCqasm})

			self.textQasm.setEnabled(True)
			self.btnQ2G.setEnabled(True)
			# self.btnC2Q.setEnabled(False)	

	def importQasm(self):

		self.fileCqasm, _ = QtWidgets.QFileDialog.getOpenFileName(self,'Import cQASM File','',"*.qasm")
		if self.fileCqasm != "":
			with open(self.fileCqasm,'r') as file:
				text = file.read()
				self.textQasm.setText(text)
			self.cnfgProj.update({'name_cqasm':self.fileCqasm})

			self.textQasm.setEnabled(True)
			self.btnQ2G.setEnabled(True)
			# self.btnC2Q.setEnabled(False)

	def openQasm(self):

		self.textQasm.setEnabled(True)
		self.btnQ2G.setEnabled(True)

		with open(self.cnfgProj['name_cqasm'],'r') as file:
			text = file.read()
			self.textQasm.setText(text)	

	def exportQasm(self):
		
		if not 'name_cqasm' in self.cnfgProj.keys():
			self.fileCqasm, _ = QtWidgets.QFileDialog.getSaveFileName(self,'Export cQASM File','',"*.qasm")
			if self.fileCqasm != "":
				self.cnfgProj.update({'name_cqasm':self.fileCqasm})

		if 'name_cqasm' in self.cnfgProj.keys():
			file = open(self.cnfgProj['name_cqasm'],'w')
			text = self.textQasm.toPlainText()
			file.write(text)
			file.close()

	#~~~~~~~~~~~~~~~~~~~~~~~~~ OpenQL functions ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def createOpenql(self):

		self.fileOpenql, _ = QtWidgets.QFileDialog.getSaveFileName(self,'Create OpenQL File','',"*.py")
		if self.fileOpenql != "":
			self.cnfgProj.update({'name_openql':self.fileOpenql})

			self.textOpenql.setEnabled(True)
			self.btnO2Q.setEnabled(True)	

	def importOpenql(self):

		self.fileOpenql, _ = QtWidgets.QFileDialog.getOpenFileName(self,'Import OpenQL File','',"*.py")
		if self.fileOpenql != "":
			with open(self.fileOpenql,'r') as file:
				text = file.read()
				self.textOpenql.setText(text)
			self.cnfgProj.update({'name_openql':self.fileOpenql})

			self.textOpenql.setEnabled(True)
			self.btnO2Q.setEnabled(True)

	def openOpenql(self):

		self.textOpenql.setEnabled(True)
		self.btnO2Q.setEnabled(True)

		with open(self.cnfgProj['name_openql'],'r') as file:
			text = file.read()
			self.textOpenql.setText(text)	

	def exportOpenql(self):
		
		if not 'name_openql' in self.cnfgProj.keys():
			self.fileOpenql, _ = QtWidgets.QFileDialog.getSaveFileName(self,'Export OpenQL File','',"*.py")
			if self.fileOpenql != "":
				self.cnfgProj.update({'name_openql':self.fileOpenql})

		if 'name_openql' in self.cnfgProj.keys():
			file = open(self.cnfgProj['name_openql'],'w')
			text = self.textOpenql.toPlainText()
			file.write(text)
			file.close()

	#~~~~~~~~~~~~~~~~~~~~~~~~~ help menu ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def helpMenu(self):

		self.menuHelpTutorial = QtWidgets.QMenu("&Learn",self)
		self.menuHelp.addMenu(self.menuHelpTutorial)

		qtactn = QtWidgets.QAction("&OpenQL",self.menuHelpTutorial)
		qtactn.triggered.connect(self.learnOpenql)
		self.menuHelpTutorial.addAction(qtactn)

		qtactn = QtWidgets.QAction("&QX simulator",self.menuHelpTutorial)
		qtactn.triggered.connect(self.learnQxsim)
		self.menuHelpTutorial.addAction(qtactn)

		self.menuHelp.addSeparator()
		
		self.menuHelpLicense = QtWidgets.QAction("&License",self)
		self.menuHelpLicense.triggered.connect(self.license)
		self.menuHelp.addAction(self.menuHelpLicense)
		
		self.menuHelpUpdate = QtWidgets.QAction("&Update",self)
		# self.menuHelpUpdate.triggered.connect(self.TBD)
		self.menuHelp.addAction(self.menuHelpUpdate)
		self.menuHelpUpdate.setEnabled(False)
		
		self.menuHelpAbout = QtWidgets.QAction("&About",self)
		self.menuHelpAbout.triggered.connect(self.about)
		self.menuHelp.addAction(self.menuHelpAbout)

	def learnOpenql(self):

		QtWidgets.QMessageBox.about(self,"Learn OpenQL","Visit : https://openql.readthedocs.io")

	def learnQxsim(self):

		QtWidgets.QMessageBox.about(self,"Learn QX simulator","Visit : https://github.com/QE-Lab/qx-simulator")

	def license(self):

		QtWidgets.QMessageBox.about(self,"License",open("license.txt",'r').read())

	def about(self):

		QtWidgets.QMessageBox.about(self,"About",open("about.txt",'r').read())

	#~~~~~~~~~~~~~~~~~~~~~~~~~ dev menu ~~~~~~~~~~~~~~~~~~~~~~~~~#

	# features under development can be accessed from here

	def devMenu(self):

		self.menuDevThemes = QtWidgets.QMenu("&Themes",self)
		self.menuDev.addMenu(self.menuDevThemes)

		for style in QtWidgets.QStyleFactory.keys():
			qtStyle = QtWidgets.QAction(style,self.menuDevThemes)
			qtStyle.triggered.connect((lambda styleName: lambda: QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(styleName)))(style))
			self.menuDevThemes.addAction(qtStyle)

	########################## MAIN LAYOUT ##########################

	def centerLayout(self):

		self.quickaccess()	

		self.centralWidget = QtWidgets.QWidget(self)
		self.setCentralWidget(self.centralWidget)
		self.topLayoutV = QtWidgets.QVBoxLayout(self.centralWidget)
		
		self.topLayoutH1 = QtWidgets.QHBoxLayout()
		self.topLayoutH1.addSpacing(self.win_cx*0.05) # Indent for circuit palate
		self.openqlEditor()
		self.qasmEditor()
		self.topLayoutV.addLayout(self.topLayoutH1)
		
		self.topLayoutH2 = QtWidgets.QHBoxLayout()
		self.resultTabs()     
		self.topLayoutV.addLayout(self.topLayoutH2)

	#~~~~~~~~~~~~~~~~~~~~~~~~~ shortcuts ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def quickaccess(self):

		self.toolBar = self.addToolBar("QuickAccess")

		extractAction = QtWidgets.QAction(QtGui.QIcon('icons/plot5.png'),'Custom Plot',self)
		extractAction.triggered.connect(self.customPlot)
		self.toolBar.addAction(extractAction)
		extractAction.setEnabled(False)

		extractAction = QtWidgets.QAction(QtGui.QIcon('icons/layout3.png'),'Custom QPU',self)
		# extractAction.triggered.connect(self.TBD)
		self.toolBar.addAction(extractAction)
		extractAction.setEnabled(False)
		
		extractAction = QtWidgets.QAction(QtGui.QIcon('icons/uc3.png'),'View Microcode',self)
		# extractAction.triggered.connect(self.TBD)
		self.toolBar.addAction(extractAction)
		extractAction.setEnabled(False)

	def customPlot(self):
		return

	#~~~~~~~~~~~~~~~~~~~~~~~~~ openql ed ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def openqlEditor(self):

		self.openqlLayout = QtWidgets.QVBoxLayout()
		
		self.textOpenql = QtWidgets.QTextEdit(self)
		self.textOpenql.setFixedSize(self.win_cx*0.55,self.win_ry*0.45)
		self.textOpenql.setText("OpenQL Editor")
		self.textOpenql.setLineWrapMode(0)
		self.textOpenql.setFontFamily("Monospace")
		self.textOpenql.setTabStopWidth(40)
		self.highlightO = syntax.PythonHighlighter(self.textOpenql.document())
		self.openqlLayout.addWidget(self.textOpenql)
		self.textOpenql.setEnabled(False)



		self.btnLayoutOC = QtWidgets.QHBoxLayout()

		self.btnO2C = QtWidgets.QPushButton(u"\u2193",self)
		# self.btnO2C.clicked.connect(self.convO2C)
		self.btnO2C.setFixedSize(self.win_cx*0.015,self.win_ry*0.03)
		self.btnLayoutOC.addWidget(self.btnO2C)
		self.btnO2C.setEnabled(False)
		
		self.btnC2O = QtWidgets.QPushButton(u"\u2191",self)
		# self.btnC2O.clicked.connect(self.convC2O)
		self.btnC2O.setFixedSize(self.win_cx*0.015,self.win_ry*0.03)
		self.btnLayoutOC.addWidget(self.btnC2O)
		self.btnC2O.setEnabled(False)
		
		self.openqlLayout.addLayout(self.btnLayoutOC)

		self.topLayoutH1.addLayout(self.openqlLayout)

		self.btnLayoutOQ = QtWidgets.QVBoxLayout()
		
		self.btnO2Q = QtWidgets.QPushButton(u"\u2192",self)
		self.btnO2Q.clicked.connect(self.convO2Q)
		self.btnO2Q.setFixedSize(self.win_cx*0.015,self.win_ry*0.03)
		self.btnLayoutOQ.addWidget(self.btnO2Q)
		self.btnO2Q.setEnabled(False)

		self.btnQ2O = QtWidgets.QPushButton(u"\u2190",self)
		# self.btnQ2O.clicked.connect(self.TBD)
		self.btnQ2O.setFixedSize(self.win_cx*0.015,self.win_ry*0.03)
		self.btnLayoutOQ.addWidget(self.btnQ2O)
		self.btnQ2O.setEnabled(False)

		self.topLayoutH1.addLayout(self.btnLayoutOQ)

	#~~~~~~~~~~~~~~~~~~~~~~~~~ qasm ed ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def qasmEditor(self):

		self.qasmLayout = QtWidgets.QVBoxLayout()
		
		self.textQasm = QtWidgets.QTextEdit(self)
		self.textQasm.setFixedSize(self.win_cx*0.35,self.win_ry*0.45)
		self.textQasm.setText("QASM Editor")
		self.textQasm.setLineWrapMode(0)
		self.textQasm.setFontFamily("Monospace")
		self.textQasm.setTabStopWidth(40)
		self.highlightQ = syntax_cqasm.cQasmHighlighter(self.textQasm.document())
		self.qasmLayout.addWidget(self.textQasm)
		self.textQasm.setEnabled(False)

		self.btnLayoutQ = QtWidgets.QHBoxLayout()

		self.btnQ2G = QtWidgets.QPushButton(u"\u2193",self)
		self.btnQ2G.clicked.connect(self.convQ2G)
		self.btnQ2G.setFixedSize(self.win_cx*0.015,self.win_ry*0.03)
		self.btnLayoutQ.addWidget(self.btnQ2G,QtCore.Qt.AlignCenter)
		self.btnQ2G.setEnabled(False)
		
		self.btnC2Q = QtWidgets.QPushButton(u"\u2191",self)
		# self.btnC2Q.clicked.connect(self.convC2Q)
		self.btnC2Q.setFixedSize(self.win_cx*0.015,self.win_ry*0.03)
		self.btnLayoutQ.addWidget(self.btnC2Q,QtCore.Qt.AlignCenter)
		self.btnC2Q.setEnabled(False)

		self.qasmLayout.addLayout(self.btnLayoutQ)

		self.topLayoutH1.addLayout(self.qasmLayout)

	#~~~~~~~~~~~~~~~~~~~~~~~~~ results ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def resultTabs(self):

		self.textLog = QtWidgets.QTextEdit(self)
		self.textLog.setFixedSize(self.win_cx*0.35,self.win_ry*0.35)
		self.textLog.setText("Run Logs")
		self.textLog.setLineWrapMode(0)
		self.textLog.setFontFamily("Monospace")
		self.textLog.setEnabled(False)

		self.tabLayout = QtWidgets.QTabWidget(self)
		self.tabLayout.addTab(self.textLog,"Logs")
		
		self.topLayoutH2.addWidget(self.tabLayout,0,QtCore.Qt.AlignRight)


	########################## BUTTONS ##########################

	def convQ2G(self):

		self.textLog.setEnabled(True)
		self.textLog.setReadOnly(True)

		self.exportQasm()

		os.system(PATH_QX+" "+self.cnfgProj['name_cqasm']+" > "+self.cnfgProj['dir']+"/"+"logQ2G.txt")
		text = open(self.cnfgProj['dir']+"/"+"logQ2G.txt",'r').read()
		self.textLog.setText(text)
		self.tabLayout.setCurrentWidget(self.textLog)

	def convO2Q(self):   

		self.textLog.setEnabled(True)
		self.textLog.setReadOnly(True)

		self.exportOpenql()
		# self.saveQasm()		# current QASM backup
		
		os.system("python3 "+self.cnfgProj['name_openql']+" > "+self.cnfgProj['dir']+"/"+"logO2Q.txt 2>&1")
		text = open(self.cnfgProj['dir']+"/"+"logO2Q.txt",'r').read()
		self.textLog.setText(text)
		self.tabLayout.setCurrentWidget(self.textLog)

		name = self.cnfgProj['dir']+"/test_output/test.qasm"       # (TBD: get output file name from openql)
		with open(name,'r') as file:
			text = file.read()
			self.textQasm.setText(text)
		file.close()

		self.textQasm.setEnabled(True)
		self.btnQ2G.setEnabled(True)

	########################## FUNCTIONS ##########################

app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())