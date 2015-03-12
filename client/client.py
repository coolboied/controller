import sys
from PyQt4 import QtCore, QtGui
from TcpClient import *
from ResultGui import *

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow():
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(800, 600)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.commander = QtGui.QTextEdit(self.centralwidget)
		self.commander.setGeometry(QtCore.QRect(10, 30, 631, 51))
		self.commander.setObjectName(_fromUtf8("commander"))
		self.commit_button = QtGui.QPushButton(self.centralwidget)
		self.commit_button.setGeometry(QtCore.QRect(460, 90, 75, 23))
		self.commit_button.setObjectName(_fromUtf8("commit_button"))
		self.clear_button = QtGui.QPushButton(self.centralwidget)
		self.clear_button.setGeometry(QtCore.QRect(560, 90, 75, 23))
		self.clear_button.setObjectName(_fromUtf8("clear_button"))
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
		self.label.setObjectName(_fromUtf8("label"))
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))

		self.retranslateUi(MainWindow)
		self.reg_clicker(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.commit_button.setText(_translate("MainWindow", "提交命令", None))
		self.clear_button.setText(_translate("MainWindow", "清空", None))
		self.label.setText(_translate("MainWindow", "执行命令:", None))
	
	def reg_clicker(self,MainWindow):
		MainWindow.connect(self.commit_button,QtCore.SIGNAL('clicked()'),self.commit_commander) 
	
	def commit_commander(self):
		tcpClient = TcpClient()
		tcpClient.send_mess(self.commander.toPlainText())
		data = tcpClient.recv_mess()
		print(data.decode('utf-8'))
		self.result_gui = ResultGui(data.decode('utf-8'))
		self.result_gui.show()

def main():

	app = QtGui.QApplication(sys.argv)

	w = QtGui.QWidget()
	u = Ui_MainWindow()
	u.setupUi(w)
	w.show()

	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
