"""Main class"""
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import sys
from customerpage import CustomerScreen
from adminpage import AdminScreen

class LoginScreen(QMainWindow):
   
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("atmloginpage.ui", self)
        self.show()
        self.CustomerScreen_go=CustomerScreen()
        self.AdminScreen_go=AdminScreen()
        self.la_welcome.show()
        self.li_id.setValidator(QIntValidator(self))
        self.okB.clicked.connect(self.login)
        #self.login()

      
    def login(self):
        id_number=self.li_id.text()
        password=self.li_password.text()
        print(id_number)
        print("Login sayfasi giris")
        if len( id_number)==0 or len (password)==0:
            self.la_error.setText("Please input all fields.")
            print("Bosluklar kontrol edildi")
        #elif   len( id_number) < 7 or len (password) < 7:
            #self.la_error.setText("Please input invalid IDNumber or Password") 
        
        
        if str(id_number).startswith("999"):
            #costumer sayfasina git degilse admin sayfasina git
                #self.okB.clicked.connect(self.go_to_customer_page)
                print("Startswith999")
                self.go_to_customer_page()
            
        else:
                #str(id_number).startswith("0"):
                #self.okB.clicked.connect(self.go_to_admin_page)
                print("Startswith0")
                self.go_to_admin_page()
                #gecersiz id veya password girerse csv lazimmmmmmmm?????
        
   
    def go_to_customer_page(self):
        self.CustomerScreen_go.show()
        self.hide()
        
    def go_to_admin_page(self):
        self.AdminScreen_go.show()
        self.hide()
        

"""class CustomerScreen(QMainWindow):
    def __init__(self):
        super(CustomerScreen, self).__init__()
        loadUi("customerpage.ui", self)
   
    
class AdminScreen(QMainWindow):
    def __init__(self):
      super(AdminScreen, self).__init__()
      loadUi("adminpage.ui", self)  """      

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    #app.setQuitOnLastWindowClosed(False)
    widget = QWidget()
    loginscreen=LoginScreen()
    loginscreen.show()
    sys.exit(app.exec_())

