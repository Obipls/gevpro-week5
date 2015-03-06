# #!/usr/bin/env python
# tel_ngram.py
# Olivier Louwaars s2814714
# 3-3-2015

import sys
from collections import Counter
from PyQt4 import QtGui,QtCore

class ShowGrams(QtGui.QWidget):
    
    def __init__(self):
        super(ShowGrams,self).__init__()
        self.initUI()  
     
    def initUI(self):
    	self.hbox=QtGui.QHBoxLayout()
    	self.vbox=QtGui.QVBoxLayout()
    	self.vbox.addLayout(self.hbox)
    	self.setLayout(self.vbox)
    	
    	self.button = QtGui.QPushButton('Kies een bestand', self)
    	self.button.clicked.connect(self.clickSelect)
        self.vbox.addWidget(self.button)
            				
    	self.setGeometry(200, 200, 100, 150)
    	self.setWindowTitle('Gramselector')
    	self.show()
    	
    	
    
    def clickSelect(self):
		self.userFile=QtGui.QFileDialog.getOpenFileName(self)
		return self.userFile

		

if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	ex=ShowGrams()
	sys.exit(app.exec_())
