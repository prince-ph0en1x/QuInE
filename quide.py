#   cd /mnt/7A06EEA206EE5E9F/GoogleDrive/TUD_CE/Thesis/SimQG/QIDE/
#   python quide.py

import sys
from PyQt4 import QtGui, QtCore
import os

class Window(QtGui.QMainWindow):
    
    win_ry = 900
    win_cx = 1600
    saved = 0
    fileOpenql = "tmpO.py"
    fileQasm = "tmp0.qasm"

    def __init__(self):

        super(Window,self).__init__()
        self.setGeometry(150,50,self.win_cx,self.win_ry)
        self.setWindowTitle("Quantum Integrated Development Environment")
        self.setWindowIcon(QtGui.QIcon('icons/app.png'))
        self.statusBar()
        self.menu()             # Menu Bar
        self.quickaccess()      # Quick Access
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
        
        gsz = 40
        bsz = gsz - 0
        
        gsr = self.win_ry/2 + gsz/2 - 8
        gsc = self.win_cx - 3*gsz - 380

        
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

        self.toolBar.addSeparator()

        execO = QtGui.QAction(QtGui.QIcon('icons/o.png'),'execute openql',self)
        execO.triggered.connect(self.execOpenQL)
        self.toolBar.addAction(execO)

        execQ = QtGui.QAction(QtGui.QIcon('icons/q.png'),'execute qasm',self)
        execQ.triggered.connect(self.execQasm)
        self.toolBar.addAction(execQ)

        execC = QtGui.QAction(QtGui.QIcon('icons/c.png'),'execute circuit',self)
        execC.triggered.connect(self.TBD)
        self.toolBar.addAction(execC)
    
    def openqlEditor(self):

        self.textOpenql = QtGui.QTextEdit(self)
        self.textOpenql.setFixedSize(self.win_cx/2-14,400)
        self.textOpenql.setText("OpenQL Editor")
        self.textOpenql.setLineWrapMode(0)
        self.topLayoutH1.addWidget(self.textOpenql,0,QtCore.Qt.AlignLeft)
        
    def qasmEditor(self):

        self.textQasm = QtGui.QTextEdit(self)
        self.textQasm.setFixedSize(self.win_cx/2-14,400)
        self.textQasm.setText("QASM Editor")
        self.textQasm.setLineWrapMode(0)
        self.topLayoutH1.addWidget(self.textQasm,0,QtCore.Qt.AlignRight)

    def circuitEditor(self):

        self.circuit = QtGui.QTextEdit(self)
        self.circuit.setFixedSize(1000,400)
        self.circuit.setText("Circuit Editor")
        self.topLayoutH2.addWidget(self.circuit,0,QtCore.Qt.AlignLeft)
        # self.topLayoutH2.addSpacing(100)

    def layoutEditor(self):

        self.qclayout = QtGui.QTextEdit(self)
        self.qclayout.setFixedSize(400,400)
        self.qclayout.setText("Layout Editor")
        self.topLayoutH2.addWidget(self.qclayout,0,QtCore.Qt.AlignRight)

    def sandbox(self):

        action = 0

        # Default View

        self.centralWidget = QtGui.QWidget(self)
        self.setCentralWidget(self.centralWidget)
        
        self.topLayoutV = QtGui.QVBoxLayout(self.centralWidget)
        
        self.topLayoutH1 = QtGui.QHBoxLayout()
        self.openqlEditor()
        self.qasmEditor()
        self.topLayoutV.addLayout(self.topLayoutH1,QtCore.Qt.AlignBottom)
        
        self.topLayoutH2 = QtGui.QHBoxLayout()   
        self.circuitEditor()
        self.layoutEditor()     
        self.topLayoutV.addLayout(self.topLayoutH2,QtCore.Qt.AlignBottom)

        
    def execQasm(self):

        file = open(self.fileQasm,'w')
        text = self.textQasm.toPlainText()
        file.write(text)
        file.close()
        os.system("./qx_simulator_1.0.beta_linux_x86_64 "+str(self.fileQasm)+" > tmpG.txt")
        #plot output
        #generate openql and circuit
        
    def execOpenQL(self):

        file = open(self.fileOpenql,'w')
        text = self.textOpenql.toPlainText()
        file.write(text)
        file.close()
        os.system("python3 "+"tmpO.py")    # arbitratry file name
        # change qasm & circuit

        name = "test_output/qg.qasm"
        file = open(name,'r')
        with file:
            text = file.read()
            self.textQasm.setText(text)

    def close_app(self):
        if self.saved == 0:
            choice = QtGui.QMessageBox.question(self,'sanity check',"Quit without saving?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.Yes:
                # print("Exiting")
                sys.exit()
            else:
                pass

    def open_openql(self):

        self.fileOpenql = QtGui.QFileDialog.getOpenFileName(self,'Open File')
        file = open(self.fileOpenql,'r')
        with file:
            text = file.read()
            self.textOpenql.setText(text)
        # highlight = syntax.PythonHighlighter(editor.document())
            
    def open_qasm(self):

        self.fileQasm = QtGui.QFileDialog.getOpenFileName(self,'Open File')
        file = open(self.fileQasm,'r')
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
* Save circuit as functional blocks
* Autouncompute
* Statistical graphs
'''