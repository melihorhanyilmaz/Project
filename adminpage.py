from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from atmloginpage import LoginScreen
from datetime import datetime
import random
import string 
import sys

class AdminScreen():
    widget=QWidget()
    customer_list=[]
    customer_id = 9990000
    
    
    def __init__(self):
         super(AdminScreen, self).__init__()
         loadUi("adminpage.ui", self)
         self.show()
         self.LoginScreen_go = LoginScreen()
         self.B_save.clicked.connect(self.add_customer)
         self.B_allcustomers.clicked.connect(self.show_allcustomers)
         self.B_exit.clicked.connect(self.exit_admin)
         
    def create_random_password(length):
        password=random.randint(1000000,9999999)
        return password
    create_random_password(7)
    pass
    '''def create_random_password(self):
        digits=[0,1,2,3,4,5,6,7,8,9]
        nummers = string.digits
        password = ''.join(random.choice(nummers) for i in range(7))
        return password
    '''
    
 
    '''def create_random_password(length):
        nummers = string.digits
        result = ''.join(random.choice(nummers) for i in range(length))
        return result
    print(create_random_password(7))'''
    
    def add_customer(self):
        name=self.li_name.text()
        
        surname=self.li_surname.text()
        
        email=self.li_email.text()
        
        firstbalance=self.li_balance.text()
        
        password=self.create_random_password()
        
        AdminScreen.customer_id +=1
        self.customer_id = AdminScreen.customer_id
        #AdminScreen.customer_list.append([self.name,self.surname,self.email])
        
        now=datetime.datetime.now()
        
        
        
        with open('allcustomers.txt','a',encoding="utf-8") as file:
            file.write(self.name+' '+self.surname+':'+self.email+','+self.customer_id+','+self.firstbalance+','+self.password+','+self.now+'\n')
    pass        

        
        
    
    
    def show_allcustomers(self):
        
        with open('allcustomers.txt','r',encoding="utf-8") as file:
            file.write(self.name+' '+self.surname+':'+self.email+','+self.accountnumber+','+self.firstbalance+','+self.password+','+self.now+'\n')
     #csv'nin güncellenmesi gerekiyor
    
    def exit_admin(self):
        self.LoginScreen_go.show()
        self.hide()
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    widget=QWidget()
    #widget.show()
    window=AdminScreen()
    window.show()
    sys.exit(app.exec_())