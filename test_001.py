# Test basic window based on available screen size

import sys
from PyQt5 import QtWidgets

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
		
		self.show()

app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())