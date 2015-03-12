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
		self.x=1
		self.scroll=QtGui.QScrollArea()
		self.hbox=QtGui.QHBoxLayout()
		self.vbox=QtGui.QVBoxLayout()
		self.vbox.addLayout(self.hbox)
		self.vbox.addSpacing(0)
		self.setLayout(self.vbox)
		
		self.cbox=QtGui.QComboBox(self)
		self.cbox.addItems(["Unigrams","Bigrams"])
		self.vbox.addWidget(self.cbox)
		self.cbox.currentIndexChanged['QString'].connect(self.handleChanged)
		
		self.button=QtGui.QPushButton('Kies een bestand', self)
		self.button.setStyleSheet("text-align:left")
		self.button.clicked.connect(self.clickSelect)
		self.vbox.addWidget(self.button)

		self.ilist=QtGui.QListWidget()
		
							
		self.setGeometry(250,250,250,250)
		self.setWindowTitle('Gramselector')
		self.show()
	
	def handleChanged(self):
		if self.cbox.currentText()=='Bigrams':
			self.x=2
		else:
			self.x=1
		return self.x

	def showResults(self,results):
		for item in results:
			self.ilist.addItem(str(item[1])+':'+'  '+item[0])
		self.vbox.addWidget(self.ilist)
		
	def clickSelect(self):
		self.ilist.clear()
		userFile=QtGui.QFileDialog.getOpenFileName(self)
		wordCount=biCount=Counter()
		if self.x==1:
			for line in open(userFile):
				wordCount.update(line.split())
			self.showResults(wordCount.most_common(20))

		else:
			biGramList=[]
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
				words=' '.join(biDict.get(str(item[0])))
				biGramList.append((words,item[1]))
			self.showResults(biGramList)
				
if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	ex=ShowGrams()
	sys.exit(app.exec_())
