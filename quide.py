#   cd /mnt/7A06EEA206EE5E9F/GoogleDrive/TUD_CE/Thesis/SimQG/QIDE/
#   python quide.py

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    
    win_ry = 900
    win_cx = 1600

    saved = 0

    fileOpenql = ""

    def __init__(self):

        super(Window,self).__init__()
        self.setGeometry(150,50,self.win_cx,self.win_ry)
        self.setWindowTitle("Quantum Integrated Development Environment")
        self.setWindowIcon(QtGui.QIcon('icons/a.png'))
        
        self.statusBar()
        self.menu()             # Menu Bar
        self.quickaccess()      # Quick Access
        
        self.topWidget = QtGui.QWidget(self)
        self.setCentralWidget(self.topWidget)
        self.topLayout = QtGui.QGridLayout(self.topWidget)

        self.gateset()          # Tool Box
        self.sandbox()          # Sandbox
        self.show()
    
    def menu(self):

        mainMenu = self.menuBar()
        menuFile = mainMenu.addMenu('&File')
        menu_edit = mainMenu.addMenu('&Edit')
        menuView = mainMenu.addMenu('&View')
        menuHelp = mainMenu.addMenu('&Help')
        
        # File Menu

        extractAction = QtGui.QAction("&New Project",self)
        extractAction.setShortcut("Ctrl+N")
        extractAction.setStatusTip('new project')
        extractAction.triggered.connect(self.TBD)
        menuFile.addAction(extractAction)
        
        menuFile.addSeparator()
        
        extractAction = QtGui.QAction("&Open Project",self)
        extractAction.setStatusTip('open existing project')
        extractAction.triggered.connect(self.TBD)
        menuFile.addAction(extractAction)

        extractAction = QtGui.QAction("&Open OpenQL",self)
        extractAction.setStatusTip('open exiting openql')
        extractAction.triggered.connect(self.open_openql)
        menuFile.addAction(extractAction)
        
        extractAction = QtGui.QAction("&Open Qasm",self)
        extractAction.setStatusTip('open exiting qasm')
        extractAction.triggered.connect(self.open_qasm)
        menuFile.addAction(extractAction)
        
        menuFile.addSeparator()
        
        extractAction = QtGui.QAction("&Save Project",self)
        extractAction.setShortcut("Ctrl+S")
        extractAction.setStatusTip('save')
        extractAction.triggered.connect(self.TBD)
        menuFile.addAction(extractAction)
        
        extractAction = QtGui.QAction("&Export Qasm",self)
        extractAction.setStatusTip('export current circuit as qasm')
        extractAction.triggered.connect(self.export_qasm)
        menuFile.addAction(extractAction)
        
        menuFile.addSeparator()
        
        extractAction = QtGui.QAction("&Exit",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('leave')
        extractAction.triggered.connect(self.close_app)
        menuFile.addAction(extractAction)

        # View Menu

        extractAction = QtGui.QAction("&Show Toolbar",self)
        extractAction.setStatusTip('show toolbar')
        extractAction.triggered.connect(self.quickaccess)
        menuView.addAction(extractAction)

        extractAction = QtGui.QAction("&Show OpenQL Editor",self)
        extractAction.setStatusTip('show openql editor')
        extractAction.triggered.connect(self.openqlEditor)
        menuView.addAction(extractAction)
        
        extractAction = QtGui.QAction("&Show QASM Editor",self)
        extractAction.setStatusTip('show qasm editor')
        extractAction.triggered.connect(self.qasmEditor)
        menuView.addAction(extractAction)
        
        menuView.addSeparator()
        
        menuViewThemes = QtGui.QMenu("&Themes",self)
        menuViewThemes.setStatusTip('select themes')
        menuView.addMenu(menuViewThemes)

        extractAction = QtGui.QAction("gtk+",menuViewThemes)
        extractAction.triggered.connect(lambda: QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("gtk+")))
        menuViewThemes.addAction(extractAction)

        extractAction = QtGui.QAction("motif",menuViewThemes)
        extractAction.triggered.connect(lambda: QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("motif")))
        menuViewThemes.addAction(extractAction)
        
        extractAction = QtGui.QAction("plastique",menuViewThemes)
        extractAction.triggered.connect(lambda: QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("plastique")))
        menuViewThemes.addAction(extractAction)
        
        extractAction = QtGui.QAction("windows",menuViewThemes)
        extractAction.triggered.connect(lambda: QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("windows")))
        menuViewThemes.addAction(extractAction)
        
        extractAction = QtGui.QAction("cleanlooks",menuViewThemes)
        extractAction.triggered.connect(lambda: QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("cleanlooks")))
        menuViewThemes.addAction(extractAction)
        
        extractAction = QtGui.QAction("cde",menuViewThemes)
        extractAction.triggered.connect(lambda: QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("cde")))
        menuViewThemes.addAction(extractAction)
        
        # Help Menu

        extractAction = QtGui.QAction("&Tutorial",self)
        extractAction.setStatusTip('enter tutorial mode')
        extractAction.triggered.connect(self.TBD)
        menuHelp.addAction(extractAction)
        
        extractAction = QtGui.QAction("&Documentation",self)
        extractAction.setStatusTip('view documentation')
        extractAction.triggered.connect(self.TBD)
        menuHelp.addAction(extractAction)
        
        menuHelp.addSeparator()
        
        extractAction = QtGui.QAction("&Release Notes",self)
        extractAction.setStatusTip('view release notes')
        extractAction.triggered.connect(self.TBD)
        menuHelp.addAction(extractAction)
        
        extractAction = QtGui.QAction("&Update",self)
        extractAction.setStatusTip('check for updates')
        extractAction.triggered.connect(self.TBD)
        menuHelp.addAction(extractAction)
        
        menuHelp.addSeparator()
        
        extractAction = QtGui.QAction("&License",self)
        extractAction.setStatusTip('view license')
        extractAction.triggered.connect(self.TBD)
        menuHelp.addAction(extractAction)
        
        extractAction = QtGui.QAction("&About",self)
        extractAction.setStatusTip('about devs')
        extractAction.triggered.connect(self.about)
        menuHelp.addAction(extractAction)

    def gateset(self):
        
        gsr = 40
        gsc = 15

        gSet = 1
        gsz = 40
        bsz = gsz - 0

        gateNames = ("X","Y","Z","H","S","T","Rx","Ry","Rz","CX","CZ","Tf")
        self.btn_g = {}
        self.gateSets = ("All","Universal {H, Tf}","Universal {1Qb, CX}")
        self.gateMasks = ("111111111111","000100000001","111111000100")

        comboBox = QtGui.QComboBox(self)
        for gs in range(0,len(self.gateSets)):
            comboBox.addItem(self.gateSets[gs])      
        comboBox.move(gsc,gsr)
        comboBox.resize(2*gsz,gsz)
        comboBox.activated[str].connect(self.gateEnbl)
        gsr = gsr+gsz  
        gr = 0
        gc = 0
        gates = len(gateNames)
        for g in range(0,gates):
            self.btn_g[g] = QtGui.QPushButton(gateNames[g],self)
            self.btn_g[g].clicked.connect(self.TBD)
            self.btn_g[g].resize(bsz,bsz)
            self.btn_g[g].move(gsc+gc*gsz,gsr+gr*gsz)
            gc = (gc + 1)%2
            if gc == 0:
                gr = gr + 1
    
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

    def quickaccess(self):

        self.toolBar = self.addToolBar("QuickAccess")

        extractAction = QtGui.QAction(QtGui.QIcon('icons/new.png'),'create a new project',self)
        extractAction.triggered.connect(self.TBD)
        self.toolBar.addAction(extractAction)

        extractAction = QtGui.QAction(QtGui.QIcon('icons/plot.png'),'plot output amplitude trend',self)
        extractAction.triggered.connect(self.TBD)
        self.toolBar.addAction(extractAction)

        extractAction = QtGui.QAction(QtGui.QIcon('icons/help.png'),'feedback/assistance',self)
        extractAction.triggered.connect(self.TBD)
        self.toolBar.addAction(extractAction)

        color = QtGui.QColor(0,0,0)
        fontColor = QtGui.QAction('bg color',self)
        fontColor.triggered.connect(self.color_picker)
        self.toolBar.addAction(fontColor)
    
    def openqlEditor(self):

        self.textOpenql = QtGui.QTextEdit(self)
        self.textOpenql.setFixedSize(600,400)
        self.textOpenql.setText("OpenQL Editor")
        self.topLayout.addWidget(self.textOpenql,0,1,1,1)
        
    def qasmEditor(self):

        self.textQasm = QtGui.QTextEdit(self)
        self.textQasm.setFixedSize(600,400)
        self.textQasm.setText("QASM Editor")
        self.topLayout.addWidget(self.textQasm,1,1,1,1)
        # layout.setAlignment(dummy1,QtCore.Qt.AlignRight)
        
    def sandbox(self):

        action = 0

        # Default View
        self.openqlEditor()
        self.qasmEditor()

        self.textQasm = QtGui.QTextEdit(self)
        self.textQasm.setFixedSize(1000,400)
        self.topLayout.addWidget(self.textQasm,1,0,1,1)


        # self.btn11 = QtGui.QPushButton("BtnWgt",self)
        # self.btn11.clicked.connect(self.close_app)
        # self.btn11.setFixedSize(30,30)
        # # self.btn11.setVisible(False)
        # # self.btn11.setEnabled(False)
        # self.topLayout.addWidget(self.btn11,0,0,1,1)



    def close_app(self):
        if self.saved == 0:
            choice = QtGui.QMessageBox.question(self,'sanity check',"Quit without saving?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.Yes:
                # print("Exiting")
                sys.exit()
            else:
                pass

    def open_openql(self):

        name = QtGui.QFileDialog.getOpenFileName(self,'Open File')
        self.fileOpenql = name
        file = open(name,'r')
        with file:
            text = file.read()
            self.textOpenql.setText(text)
            
    def open_qasm(self):

        name = QtGui.QFileDialog.getOpenFileName(self,'Open File')
        file = open(name,'r')
        with file:
            text = file.read()
            self.textQasm.setText(text)

    def export_qasm(self):

        name = QtGui.QFileDialog.getSaveFileName(self,'Save File')
        file = open(name,'w')

        text = self.textEdit.toPlainText()

        self.show_editor()
        file.write(text)
        file.close()
        
    def about(self):
        print(self.fileOpenql)
        print("Alex")
    
    def ins_gate(self):

        print("f")
        
    def color_picker(self):

        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def TBD(self):

        print("TBD")

app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())

## TODOS

'''

* Allow Topology Definition
* Real time qasm and openql rendering and viceversa
* Save circuit as functional blocks
* Autouncompute
* Statistical graphs
* Toolset of universal gate set
* Style COnfiguration file

'''

# checkbox v8
# progress bar
# fonts v11
# colour v12
# calender v12