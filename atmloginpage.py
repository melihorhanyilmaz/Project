"""Main class"""
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import sys
#from customerpage  import CustomerScreen
from adminpage import AdminScreen

class LoginScreen(QMainWindow):
    clicked=pyqtSignal
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("atmloginpage.ui", self)
        self.show()
        self.CustomerScreen_go=CustomerScreen()
        self.AdminScreen_go=AdminScreen()
        self.la_welcome.show()
        self.li_id.setValidator(QIntValidator(self))
        self.okB.clicked.connect(self.login)
        

        """""
        self.passwordlogin()
        self.idlogin()
        central_widget=QWidget(self)
        self.setCentralWidget(central_widget)
        
        layout=QVBoxLayout(central_widget)
        
        self.li_id=QLineEdit()
        self.li_password=QLineEdit()
        layout.addWidget(self.li_id)
        layout.addWidget(self.li_password)
        
        self.li_id.clicked.connect(lambda:self.disable_line_edits(self.li_id))
        self.li_password.clicked.connect(lambda:self.disable_line_edits(self.li_password))
        
    def disable_line_edits(self,current_line_edit):
        if current_line_edit==self.li_id:
            self.li_password.setDisabled(True)
        elif current_line_edit==self.li_password:
             self.li_id.setDisabled(True)    
             
     
      
      
        #self.password_buttons()
        #self.id_buttons()
        
    
    
    def passwordlogin(self):  
        self.zeroB.clicked.connect(self.action0)
        self.oneB.clicked.connect(self.action1)
        self.twoB.clicked.connect(self.action2)
        self.threeB.clicked.connect(self.action3)
        self.fourB.clicked.connect(self.action4)
        self.fiveB.clicked.connect(self.action5)
        self.sixB.clicked.connect(self.action6)
        self.sevenB.clicked.connect(self.action7)
        self.eightB.clicked.connect(self.action8)
        self.nineB.clicked.connect(self.action9)
        self.delB.clicked.connect(self.action_del)
        self.clearB.clicked.connect(self.action_clear)
        
     
    
    def idlogin(self):  
        self.zeroB.clicked.connect(self.id_action0)
        self.oneB.clicked.connect(self.id_action1)
        self.twoB.clicked.connect(self.id_action2)
        self.threeB.clicked.connect(self.id_action3)
        self.fourB.clicked.connect(self.id_action4)
        self.fiveB.clicked.connect(self.id_action5)
        self.sixB.clicked.connect(self.id_action6)
        self.sevenB.clicked.connect(self.id_action7)
        self.eightB.clicked.connect(self.id_action8)
        self.nineB.clicked.connect(self.id_action9)
      

    def action0(self):
        # appending label text
        text = self.li_password.text()
        self.li_password.setText(text + "0")
        
    def action1(self):
        # appending label text
        text = self.li_password.text()
        self.li_password.setText(text + "1")
    def action2(self):
        # appending label text
        text = self.li_password.text()
        self.li_password.setText(text + "2")
    def action3(self):
        # appending label text
        text = self.li_password.text()
        self.li_password.setText(text + "3")
    def action4(self):
        # appending label text
        text = self.li_password.text()
        self.li_password.setText(text + "4")
    def action5(self):
        # appending label text
        text = self.li_password.text()
        self.li_password.setText(text + "5")
    def action6(self):
        # appending label text
        text = self.li_password.text()
        self.li_password.setText(text + "6")
    def action7(self):
        # appending label text
        text = self.li_password.text()
        self.li_password.setText(text + "7")
    def action8(self):
        # appending label text
        text = self.li_password.text()
        self.li_password.setText(text + "8")
    def action9(self):
        # appending label text
        text = self.li_password.text()
        self.li_password.setText(text + "9")
    def action_clear(self):
        # clearing the label text
        self.li_id.setText("")
        self.li_password.setText("")
    def action_del(self):
        # clearing a single digit
        text = self.li_password.text()
        print(text[:len(text)-1])
        self.li_password.setText(text[:len(text)-1])   
    def id_action0(self):
        # appending label text
        text1 = self.li_id.text()
        self.li_id.setText(text1 + "0")
        
    def id_action1(self):
        # appending label text
        text1 = self.li_id.text()
        self.li_id.setText(text1 + "1")
    def id_action2(self):
        # appending label text
        text1 = self.li_id.text()
        self.li_id.setText(text1 + "2")
    def id_action3(self):
        # appending label text
        text1 = self.li_id.text()
        self.li_id.setText(text1 + "3")
    def id_action4(self):
        # appending label text
        text1 = self.li_id.text()
        self.li_id.setText(text1 + "4")
    def id_action5(self):
        # appending label text
        text1 = self.li_id.text()
        self.li_id.setText(text1 + "5")
    def id_action6(self):
        # appending label text
        text1 = self.li_id.text()
        self.li_id.setText(text1 + "6")
    def id_action7(self):
        # appending label text
        text1 = self.li_id.text()
        self.li_id.setText(text1 + "7")
    def id_action8(self):
        # appending label text
        text1 = self.li_id.text()
        self.li_id.setText(text1 + "8")
    def id_action9(self):
        # appending label text
        text1 = self.li_id.text()
        self.li_id.setText(text1 + "9")
        """""
    def login(self):
        id_number=self.li_password.text()
        password=self.li_password.text()
        if len( id_number)==0 or len (password)==0:
           self.la_error.setText("Please input all fields.")
        elif   len( id_number) < 7 or len (password) < 7:
            self.la_error.setText("Please input invalid IDNumber or Password") 
        else:
              if str(id_number).startswith("999"):
            #costumer sayfasina git degilse admin sayfasina git
                self.okB.clicked.connect(self.go_to_customer_page)
              elif str(id_number).startswith("0"):
                self.okB.clicked.connect(self.go_to_admin_page)
                #gecersiz id veya password girerse csv lazimmmmmmmm?????
            
  
   
    def go_to_customer_page(self):
        self.CustomerScreen_go.show()
        self.hide()
        
    def go_to_admin_page(self):
        self.AdminScreen_go.show()
        self.hide()
        
        
  
class CustomerScreen(QMainWindow):
    def __init__(self):
         super(CustomerScreen, self).__init__()
         loadUi("customerpage.ui", self)
   



    
class AdminScreen(QMainWindow):
    def __init__(self):
      super(AdminScreen, self).__init__()
      loadUi("adminpage.ui", self)
    
    
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    widget = QWidget()
    loginscreen=LoginScreen()
    loginscreen.show()
    sys.exit(app.exec_())


