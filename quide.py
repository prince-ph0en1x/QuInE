# \author: Aritra Sarkar

#   cd /mnt/7A06EEA206EE5E9F/GoogleDrive/TUD_CE/Thesis/SimQG/QIDE/
#   python quide.py

import sys
from PyQt4 import QtGui, QtCore
import os
import re
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import syntax

class Window(QtGui.QMainWindow):
    
    win_ry = 900
    win_cx = 1600
    saved = 0
    fileOpenql = "tmpO.py"
    fileQasm = "tmp0.qasm"
    
    circTick = 0
    gateNames = ("X","Y","Z","H","S","T","Rx","Ry","Rz","CX","CZ","Tf")
    gateCodes = ("x","y","z","h","s","t","rx","ry","rz","cnot","cphase","toffoli")
    drawGateQ = []
    drawMaxQ = 0
        
    def __init__(self):

        super(Window,self).__init__()
        self.setGeometry(150,50,self.win_cx,self.win_ry)
        self.setWindowTitle("Quantum Integrated Development Environment")
        self.setWindowIcon(QtGui.QIcon('icons/app.png'))
        # self.QtGui.QMainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.statusBar()
        self.menu()             # Menu Bar
        self.quickaccess()      # Quick Access
        self.sandbox()          # Sandbox
        self.show()
    
    def menu(self):

        mainMenu = self.menuBar()
        menuFile = mainMenu.addMenu('&File')
        menuEdit = mainMenu.addMenu('&Edit')
        menuEdit.setEnabled(False)
        menuView = mainMenu.addMenu('&View')
        menuHelp = mainMenu.addMenu('&Help')
        
        # File Menu

        extractAction = QtGui.QAction("&New Project",self)
        extractAction.setShortcut("Ctrl+N")
        extractAction.setStatusTip('new project')
        extractAction.triggered.connect(self.TBD)
        menuFile.addAction(extractAction)
        extractAction.setEnabled(False)
        
        menuFile.addSeparator()
        
        extractAction = QtGui.QAction("&Open Project",self)
        extractAction.setStatusTip('open existing project')
        extractAction.triggered.connect(self.TBD)
        menuFile.addAction(extractAction)
        extractAction.setEnabled(False)

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
        extractAction.setEnabled(False)
        
        extractAction = QtGui.QAction("&Export Qasm",self)
        extractAction.setStatusTip('export current circuit as qasm')
        extractAction.triggered.connect(self.export_qasm)
        menuFile.addAction(extractAction)
        
        extractAction = QtGui.QAction("&Export Circuit",self)
        extractAction.setStatusTip('export current circuit as image')
        extractAction.triggered.connect(self.exportCircuit)
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
        extractAction.setEnabled(False)
        
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
        extractAction.setEnabled(False)

        extractAction = QtGui.QAction("&Documentation",self)
        extractAction.setStatusTip('view documentation')
        extractAction.triggered.connect(self.TBD)
        menuHelp.addAction(extractAction)
        extractAction.setEnabled(False)

        menuHelp.addSeparator()
        
        extractAction = QtGui.QAction("&Release Notes",self)
        extractAction.setStatusTip('view release notes')
        extractAction.triggered.connect(self.TBD)
        menuHelp.addAction(extractAction)
        extractAction.setEnabled(False)
        
        extractAction = QtGui.QAction("&Update",self)
        extractAction.setStatusTip('check for updates')
        extractAction.triggered.connect(self.TBD)
        menuHelp.addAction(extractAction)
        extractAction.setEnabled(False)
        
        menuHelp.addSeparator()
        
        extractAction = QtGui.QAction("&License",self)
        extractAction.setStatusTip('view license')
        extractAction.triggered.connect(self.license)
        menuHelp.addAction(extractAction)
        
        extractAction = QtGui.QAction("&About",self)
        extractAction.setStatusTip('about devs')
        extractAction.triggered.connect(self.about)
        menuHelp.addAction(extractAction)

    def gateset(self):
        
        gsz = 40
        bsz = gsz - 0
        gsr = self.win_ry/2 + gsz/2 + 5
        gsc = 10 #self.win_cx - 3*gsz - 380 
        self.btn_g = {}
        self.gateSets = ("All","Universal {H, Tf}","Universal {1Qb, CX}")
        self.gateMasks = ("111111111111","000100000001","111111000100")
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
            self.btn_g[g].setFixedSize(bsz,bsz)
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
        
        self.topLayoutH2.addLayout(self.btnLayoutGates,QtCore.Qt.AlignLeft)
    
    def circSelGate(self,gateId):

        self.drawGate = gateId
        self.drawGateQ = []
        # self.circuit.setDragMode(QtGui.QGraphicsView.NoDrag)
    
    def pixelSelect(self, event):

        # undo/redo gate button
        # drag toggle button
        # make new kernel button
        # make new unitary button
        # insert custom kernel/unitary button

        name = "testC2G.qasm"
        file = open(name,'a')      

        ysp = 40
        qb = event.pos().y()/ysp
        self.drawGateQ.append(qb)
        if self.drawGate < 9:
            if len(self.drawGateQ) == 1:
                self.circGate(self.drawGate,self.drawGateQ)
                file.write(self.gateCodes[self.drawGate]+" q"+str(self.drawGateQ[0])+"\n")
                if qb+1 > self.drawMaxQ:
                    self.drawMaxQ = qb+1
        elif self.drawGate == 9:
            if len(self.drawGateQ) == 2:
                self.circGate(self.drawGate,self.drawGateQ)
                file.write(self.gateCodes[self.drawGate]+" q"+str(self.drawGateQ[0])+",q"+str(self.drawGateQ[1])+"\n")
                if qb+1 > self.drawMaxQ:
                    self.drawMaxQ = qb+1
        elif self.drawGate == 11:
            if len(self.drawGateQ) == 3:
                self.circGate(self.drawGate,self.drawGateQ)
                file.write(self.gateCodes[self.drawGate]+" q"+str(self.drawGateQ[0])+",q"+str(self.drawGateQ[1])+",q"+str(self.drawGateQ[2])+"\n")
                if qb+1 > self.drawMaxQ:
                    self.drawMaxQ = qb+1

        file.close()

    def execCirc(self):

        file = open("testC2G.qasm",'r+')
        content = file.read()+"display"
        file.seek(0, 0)
        file.write("qubits "+str(self.drawMaxQ)+"\n" + content)
        file.close()
        os.system("./qx_simulator_1.0.beta_linux_x86_64 "+str("testC2G.qasm")+" > tmpCG.txt")
        self.plotOutput()

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
        extractAction.triggered.connect(self.plotOutput)
        self.toolBar.addAction(extractAction)

        extractAction = QtGui.QAction(QtGui.QIcon('icons/help.png'),'feedback/assistance',self)
        extractAction.triggered.connect(self.TBD)
        self.toolBar.addAction(extractAction)

        # color = QtGui.QColor(0,0,0)
        # fontColor = QtGui.QAction('bg color',self)
        # fontColor.triggered.connect(self.color_picker)
        # self.toolBar.addAction(fontColor)

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
    
    def codeEditors(self):

        self.topLayoutH1.addSpacing(90) 
        
        self.textOpenql = QtGui.QTextEdit(self)
        self.textOpenql.setFixedSize(990,415)
        self.textOpenql.setText("OpenQL Editor")
        self.textOpenql.setLineWrapMode(0)
        self.highlight = syntax.PythonHighlighter(self.textOpenql.document())
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

        self.qasmLayout = QtGui.QVBoxLayout()
        
        self.textQasm = QtGui.QTextEdit(self)
        self.textQasm.setFixedSize(460,380)    # self.win_cx/2-30
        self.textQasm.setText("QASM Editor")
        self.textQasm.setLineWrapMode(0)
        self.qasmLayout.addWidget(self.textQasm,0,QtCore.Qt.AlignRight)

        self.btnLayoutQ = QtGui.QHBoxLayout()

        self.btnQ2C = QtGui.QPushButton(u"\u2193",self)
        self.btnQ2C.clicked.connect(self.convQ2C)
        self.btnQ2C.setFixedSize(30,30)
        self.btnLayoutQ.addWidget(self.btnQ2C,QtCore.Qt.AlignLeft)
        
        self.btnC2Q = QtGui.QPushButton(u"\u2191",self)
        self.btnC2Q.clicked.connect(self.TBD)
        self.btnC2Q.setFixedSize(30,30)
        self.btnLayoutQ.addWidget(self.btnC2Q,QtCore.Qt.AlignLeft)
        self.btnC2Q.setEnabled(False)
        
        self.btnLayoutQ.addSpacing(40) 

        self.btnQ2G = QtGui.QPushButton(u"\u2193",self)
        self.btnQ2G.clicked.connect(self.plotOutput)
        self.btnQ2G.setFixedSize(30,30)
        self.btnLayoutQ.addWidget(self.btnQ2G,0,QtCore.Qt.AlignLeft)
        
        self.qasmLayout.addLayout(self.btnLayoutQ,QtCore.Qt.AlignRight)

        self.topLayoutH1.addLayout(self.qasmLayout,QtCore.Qt.AlignRight)

    def circuitEditor(self):

        penG = QtGui.QPen(QtCore.Qt.blue)
        fill = QtGui.QBrush(QtCore.Qt.cyan)

        self.qcircuit = QtGui.QGraphicsScene()
        self.circReset()
        self.qcircuit.setBackgroundBrush(QtCore.Qt.white)

        self.btnLayoutC = QtGui.QHBoxLayout()

        self.circuit = QtGui.QGraphicsView(self.qcircuit)
        self.circuit.setFixedSize(1100,400)
        self.circuit.mousePressEvent = self.pixelSelect
        self.btnLayoutC.addWidget(self.circuit,QtCore.Qt.AlignLeft)

        self.btnC2G = QtGui.QPushButton(u"\u2192",self)
        self.btnC2G.clicked.connect(self.execCirc)
        self.btnC2G.setFixedSize(30,30)
        self.btnLayoutC.addWidget(self.btnC2G,0,QtCore.Qt.AlignTop)

        self.topLayoutH2.addLayout(self.btnLayoutC,QtCore.Qt.AlignLeft)

    def layoutEditor(self):

        tsz = 325

        # self.figure = Figure()
        # self.graphres = FigureCanvas(self.figure)
        # self.graphres.setFixedSize(tsz,tsz)

        self.figure = Figure()
        self.graphres = FigureCanvas(self.figure)
        self.graphres.setFixedSize(tsz,tsz)

        self.toolbar = NavigationToolbar(self.graphres, self)
        self.toolbar.setFixedSize(tsz,25)

        self.qcoutputw = QtGui.QWidget() 
        
        self.qcoutput = QtGui.QVBoxLayout(self.qcoutputw)
        self.qcoutput.addWidget(self.toolbar)
        self.qcoutput.addWidget(self.graphres)
        
        self.scene1 = QtGui.QGraphicsScene()
        self.qclayout = QtGui.QGraphicsView(self.scene1)
        self.qclayout.setFixedSize(tsz,tsz)
        self.pixmap_item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap('topologies/surface17a.png').scaled(tsz,tsz), None, self.scene1)

        self.scene4 = QtGui.QGraphicsScene()
        self.showlog = QtGui.QGraphicsView(self.scene4)
        self.showlog.setFixedSize(tsz,tsz)
        self.pixmap_item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap('icons/tbd.png').scaled(tsz,tsz), None, self.scene4)

        self.tabLayout = QtGui.QTabWidget(self)
        self.tabLayout.addTab(self.qcoutputw,"Output")
        self.tabLayout.addTab(self.qclayout,"Layout")
        self.tabLayout.addTab(self.showlog,"Logs")

        self.topLayoutH2.addWidget(self.tabLayout,0,QtCore.Qt.AlignRight)

        
        
        # self.penColor = QtCore.Qt.red
        # pen = QtGui.QPen(self.penColor)
        
        # self.scene = QtGui.QGraphicsScene()
        
        # self.qclayout = QtGui.QGraphicsView(self.scene)
        # self.qclayout.setFixedSize(400,400)
        # self.topLayoutH2.addWidget(self.qclayout,0,QtCore.Qt.AlignRight)

        # self.pixmap_item = QtGui.QGraphicsPixmapItem(QtGui.QPixmap('topologies/surface17a.png').scaled(300,300), None, self.scene)
        # self.pixmap_item.mousePressEvent = self.pixelSelect

    def sandbox(self):

        self.centralWidget = QtGui.QWidget(self)
        self.setCentralWidget(self.centralWidget)
        
        self.topLayoutV = QtGui.QVBoxLayout(self.centralWidget)
        
        self.topLayoutH1 = QtGui.QHBoxLayout()
        self.codeEditors()
        self.topLayoutV.addLayout(self.topLayoutH1,QtCore.Qt.AlignBottom)
        
        self.topLayoutH2 = QtGui.QHBoxLayout()
        self.gateset()
        self.circuitEditor()
        self.layoutEditor()     
        self.topLayoutV.addLayout(self.topLayoutH2,QtCore.Qt.AlignBottom)

    def exportCircuit(self):
        
        name = QtGui.QFileDialog.getSaveFileName(self,'Save File')
        pixmap = QtGui.QPixmap(self.qcircuit.sceneRect().width(),self.qcircuit.sceneRect().height())
        painter = QtGui.QPainter(pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        self.qcircuit.render(painter)
        painter.end()
        pixmap.save(name)
        return
    
    def plotOutput(self):

        self.filePlot = QtGui.QFileDialog.getOpenFileName(self,'Open File')
        file = open(self.filePlot,'r')
        
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
                ploty[state] = x**2 + y**2      # check, sqrt reqd?

        ax = self.figure.add_subplot(1,1,1)   
        ax.clear()
        ax.plot(ploty, '*-r')
        ax.set_xlim([0,2**qbno-1])
        ax.set_ylim([0,1])
        self.graphres.draw()

        # layout.addWidget(self.canvas)

        return

    # New Project -- SET PATH to new folder fro temp files

    def execQasm(self):

        file = open(self.fileQasm,'w')
        text = self.textQasm.toPlainText()
        file.write(text)
        file.close()
        os.system("./qx_simulator_1.0.beta_linux_x86_64 "+str(self.fileQasm)+" > tmpG.txt")
        #plot output
        #generate openql and circuit

    def saveOpenql(self):

        self.fileOpenql = QtGui.QFileDialog.getSaveFileName(self,'Save File')
        file = open(self.fileOpenql,'w')
        text = self.textOpenql.toPlainText()
        file.write(text)
        file.close()

    def execOpenQL(self):

        if self.fileOpenql == "tmpO.py":    # change to any unsaved file
            self.saveOpenql()
        os.system("python3 "+str(self.fileOpenql)+" > logO2Q.txt 2>&1")

    def convO2Q(self):   

        self.execOpenQL()
        if self.fileQasm == "tmpO.qasm":            # change to any unsaved file
            self.export_qasm()
        self.fileQasm = "test_output/qg.qasm"       # get output file name from openql
        file = open(self.fileQasm,'r')
        with file:
            text = file.read()
            self.textQasm.setText(text)

    def circReset(self):

        os.remove("testC2G.qasm")
        for item in self.qcircuit.items():
            self.qcircuit.removeItem(item)
        pen = QtGui.QPen(QtCore.Qt.black)
        qubits = 50
        for i in range(0,qubits):
            t = self.qcircuit.addText("q["+str(i)+"]")
            t.setPos(0,i*40)
            self.qcircuit.addLine(QtCore.QLineF(50,i*40+12,80,i*40+12),pen)
        self.circTick = 0 

    def circGate(self,gateId,qbset):

        beg = 80
        xsp = 50
        ysp = 40

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

        self.circTick = self.circTick + 1   # allow parallel scheduling

        return

    def convQ2C(self):

        self.circReset()
        
        # save qasm/circ
        
        gates = len(self.gateNames)
        name = QtGui.QFileDialog.getOpenFileName(self,'Open File')
        file = open(name,'r')
        for line in iter(file):

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

        self.circuit.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
       
        return

    def saveQasm(self): # diff btwen save n export.... save would change current file name

        self.fileQasm = QtGui.QFileDialog.getSaveFileName(self,'Save File')
        file = open(self.fileQasm,'w')
        text = self.textQasm.toPlainText()
        file.write(text)
        file.close()

    def export_qasm(self):
        
        name = QtGui.QFileDialog.getSaveFileName(self,'Save File')
        file = open(name,'w')
        text = self.textQasm.toPlainText()
        file.write(text)
        file.close()

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

    def ins_gate(self):

        print("f")
        
    def color_picker(self):

        color = QtGui.QColorDialog.getColor()
        self.penColor = color
        # self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def license(self):

        QtGui.QMessageBox.about(self,"License",open("license.txt",'r').read())

    def about(self):

        QtGui.QMessageBox.about(self,"About",open("about.txt",'r').read())

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
* Save/Open Project
* Disable TBD buttons
* Change toolbox to Layout
* Show/Hide Toolbar
* Tab width in TextEdit
* QASM syntax highlighting
'''