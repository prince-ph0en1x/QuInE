# Test menu, exit check

import sys
from PyQt5 import QtGui, QtWidgets

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

		self.saved = 0
		self.menu()
		
		self.show()

# 	########################## MAIN MENUS ##########################

	def menu(self):

		self.mainMenu = self.menuBar()
		self.menuFile = self.mainMenu.addMenu('&File')
		self.fileMenu()

# 	#~~~~~~~~~~~~~~~~~~~~~~~~~ file menu ~~~~~~~~~~~~~~~~~~~~~~~~~#

	def fileMenu(self):

		self.menuFileNewProj = QtWidgets.QAction("&New Project",self)
		self.menuFileNewProj.setShortcut("Ctrl+N")
		self.menuFileNewProj.triggered.connect(self.newProject)
		self.menuFile.addAction(self.menuFileNewProj)

		self.menuFileOpenProj = QtWidgets.QAction("&Open Project",self)
		self.menuFileOpenProj.setShortcut("Ctrl+O")
		self.menuFileOpenProj.triggered.connect(self.openProject)
		self.menuFile.addAction(self.menuFileOpenProj)

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

	def newProject(self):
		return

	def openProject(self):
		return

app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())