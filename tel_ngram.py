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
		
		self.cbox=QtGui.QComboBox(self)
		self.cbox.addItems(["unigrams","bigrams"])
		self.vbox.addWidget(self.cbox)
		self.cbox.currentIndexChanged['QString'].connect(self.handleChanged)
		
		self.button=QtGui.QPushButton('Kies een bestand', self)
			
		self.button.clicked.connect(self.clickSelect)
		self.vbox.addWidget(self.button)
							
		self.setGeometry(200, 200, 100, 150)
		self.setWindowTitle('Gramselector')
		self.show()
	
	def handleChanged(self):
		self.x=1
		if self.cbox.currentText()=='bigrams':
			self.x=2
		return self.x
		
	def clickSelect(self):
		userFile=QtGui.QFileDialog.getOpenFileName(self)
		wordCount=biCount=Counter()
		if self.x==1:
			for line in open(userFile):
				wordCount.update(line.split())
			print wordCount.most_common(20)
			for item in wordCount.most_common(20):
				lbl=QtGui.QLabel(str(item[0]+'    '+str(item[1])),self)
				lbl.setAlignment(QtCore.Qt.AlignRight)
				self.vbox.addWidget(lbl)
		else:
			biDict={}
			for line in open(userFile):
				senLen=len(line.split())
				words=line.split()
				for i in range(senLen-1):
					biGramConc=''.join(words[:2])
					biGram=[]
					biGram.append(biGramConc)
					biCount.update(biGram)
					biDict[biGramConc]=words[:2]
					words.pop(0)
			for item in biCount.most_common(20):
				#print ' '.join(biDict.get(str(item[0])))
				lbl=QtGui.QLabel(' '.join(biDict.get(str(item[0])))+'    '+str(item[1]),self)
				lbl.setAlignment(QtCore.Qt.AlignRight)
				self.vbox.addWidget(lbl)
				
if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	ex=ShowGrams()
	sys.exit(app.exec_())
