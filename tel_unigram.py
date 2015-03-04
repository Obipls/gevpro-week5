# #!/usr/bin/env python
# tel_unigrams.py
# Olivier Louwaars s2814714
# 3-3-2015

import sys
from collections import Counter
from PyQt4 import QtGui, QtCore

class ShowResults(QtGui.QWidget):
    
    def __init__(self):
        super(ShowResults, self).__init__()
        self.initUI()
        
    def initUI(self):
    	self.hbox=QtGui.QHBoxLayout()
    	self.vbox=QtGui.QVBoxLayout()
    	self.setGeometry(200, 200, 100, 150)
    	self.setWindowTitle('Top Unigrams')
    	self.show()


def main(argv):
	
	# Check for valid program call
	if len(argv)<2:
		print("Usage = tel_unigram.py [desired textfile]")
		exit(-1)
	wordCount=Counter()
	for line in open(argv[1]):
		wordCount.update(line.split())
	print(wordCount.most_common(20))

	



if __name__=="__main__":
	main(sys.argv)
	app=QtGui.QApplication(sys.argv)
	sys.exit(app.exec_())