from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from atmloginpage import LoginScreen
import datetime
import random
import string 
import sys

class AdminScreen(QMainWindow):
    def __init__(self,name,surname,email,firstbalance,id_number,password,now):
        self.name=name
        self.surname=surname
        self.email=email
        self.firstbalance=firstbalance
        self.id_number=id_number
        self.password=password
        self.now=now
    
    def __init__(self):
         super(AdminScreen, self).__init__()
         loadUi("adminpage.ui", self)
         self.show()
         self.LoginScreen_go = LoginScreen()
         self.B_save.clicked.connect(self.add_customer)
         self.B_allcustomers.clicked.connect(self.show_allcustomers)
         self.B_exit.clicked.connect(self.exit_admin)
         
         print('init calisti')
        
    def add_customer(self):
        self.name=self.li_name.text()
        self.surname=self.li_surname.text()
        self.email=self.li_email.text()
        self.firstbalance=self.li_balance.text()
        self.id_number=self.li_accountno.text()
        self.password=self.li_password.text()
        self.now=str(datetime.datetime.now())
        
        print('pass,id_num,alindi')
    
        with open('allcustomers1.txt','a',encoding="utf-8") as file:
            file.write(self.name+','+self.surname+','+self.email+','+self.id_number+','+self.firstbalance+','+self.password+','+self.now+'\n')
        print('dosya acti bilgileri yazdi')
    def show_allcustomers(self):
        
        with open('allcustomers1.txt','r',encoding="utf-8") as file:
            file.write(self.name+','+self.surname+','+self.email+','+self.id_number+','+self.firstbalance+','+self.password+','+self.now+'\n')
        print('dosya okundu')
        #csv'nin güncellenmesi gerekiyor
    
    def exit_admin(self):
        self.LoginScreen_go.show()
        self.hide()
        print('log screene gitti')
if __name__=="__main__":
    app=QApplication(sys.argv)
    widget=QWidget()
    #widget.show()
    window=AdminScreen()
    window.show()
    sys.exit(app.exec_())
