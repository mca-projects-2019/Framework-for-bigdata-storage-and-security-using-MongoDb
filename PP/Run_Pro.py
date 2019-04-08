import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from pymongo import MongoClient



try: 
    conn = MongoClient()
    db = conn.uds
    collection = db.DF
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB")

    


class Main_Home(QMainWindow):
    def __init__(self):
            super(Main_Home,self).__init__()
            loadUi('Main_Home.ui',self)
            self.setWindowTitle('UDS')
            #self.setWindowIcon(QtGui.QIcon('logo.png'))
            #self.actionInsert.clicked.connect(self.openDialog)
            
            self.actionInsert.triggered.connect(self.ins_window)
            self.actionRetrieve.triggered.connect(self.ret_window)
            

            
            
    def ins_window(self):
            self.nd = Insert_File(self)
            self.nd.show()

    def ret_window(self):
            self.nd = Retrieve_File(self)
            self.nd.show()


   
		


class Insert_File(QDialog):
    def __init__(self,parent):
	    super(Insert_File,self).__init__(parent)
	    loadUi('ins_base.ui',self)
	    #self.setWindowTitle('Insert')
	    #self.setWindowIcon(QtGui.QIcon('logo.png'))
	    self.pushButton.clicked.connect(self.ins_main)

    def ins_main(self):
            x=self.lineEdit.text()
            f = open(x)
            text = f.read()
            DF_ins = { "fname":x,  "content":text}
            if(collection.insert(DF_ins)):
                print("insertion successful")
                QMessageBox.about(self, "UDS", "Insertion Successful")
                QDialog.reject()
            
		

class Retrieve_File(QDialog):
	def __init__(self,parent):
		super(Retrieve_File,self).__init__(parent)
		loadUi('ret_base.ui',self)
		#self.setWindowTitle('Insert')
		#self.setWindowIcon(QtGui.QIcon('logo.png'))
    


app=QApplication(sys.argv)
widget=Main_Home()
widget.show()
sys.exit(app.exec_())
