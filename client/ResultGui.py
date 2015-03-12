from PyQt4 import QtCore, QtGui

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

class ResultGui(QtGui.QWidget):
	def __init__(self, text):
		QtGui.QWidget.__init__(self)
		self.resize(400, 500)
		self.label = QtGui.QTextBrowser(self)
		self.verticalScrollBar = QtGui.QScrollBar(self.label)
		self.verticalScrollBar.setGeometry(QtCore.QRect(410, 0, 16, 461))
		self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
		self.label.setGeometry(QtCore.QRect(10, 10, 380, 480))
		self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label.setObjectName(_fromUtf8("label"))
		self.label.setText(text)
