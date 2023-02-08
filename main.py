import sys, random, datetime, csv, re, json
import pandas as pd
from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi


class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("atmloginpage.ui", self)
        self.la_welcome.show()
        self.li_id.setValidator(QIntValidator(self))
        self.okB.clicked.connect(self.login)
        

      
    def login(self):
        self.id_number=self.li_id.text()
        self.password=self.li_password.text()
        CustomerScreen.id = self.id_number
        WithdrawScreen.id = self.id_number
        DepositScreen.id = self.id_number
        AccountState.id = self.id_number
        allcustomerScreen.id = self.id_number
        print("Login sayfasi giris")
        
        print(self.id_number)
        df=pd.read_csv('allcustomers1.csv')
        
        checkpassword = df[df['id_number'] == int(self.id_number)]['password']
        df.loc[df['id_number'] == int(self.id_number),('firstbalance')]=100
        df.to_csv('allcustomers1.csv', mode ='w')
        print(df)
        print(df.info())  
          
        if len(self.id_number)==0 or len (self.password)==0:
            self.la_error.setText("Please input all fields.")
            print("Bosluklar kontrol edildi")
        elif len(self.id_number) < 7 or len (self.password) < 7:
            self.la_error.setText("Please input invalid IDNumber or Password")
       
                    
        if str(self.id_number).startswith("999"):#ve password gecerli ise ibaresini de gir???
            
            self.go_to_customer_page()
                         
            
        elif str(self.id_number).startswith("0"):
                
            print("Startswith0")
            print(self.password)
            self.go_to_admin_page()
                
        
   
    def go_to_customer_page(self):
        self.li_id.clear()
        self.li_password.clear()
        customerScreen = CustomerScreen()
        widget.addWidget(customerScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def go_to_admin_page(self):
        self.li_id.clear()
        self.li_password.clear()
        adminScreen = AdminScreen()
        widget.addWidget(adminScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class AdminScreen(QMainWindow):
    def __init__(self,name,surname,email,firstbalance,id_number,password,now):
        self.name=name
        self.surname=surname
        self.email=email
        self.firstbalance=firstbalance
        self.id_number = id_number
        self.password = password
        self.now=now
    
    def __init__(self):
        super(AdminScreen, self).__init__()
        loadUi("adminpage.ui", self)
        self.B_save.clicked.connect(self.add_customer)
        self.B_allcustomers.clicked.connect(self.show_allcustomers)
        self.B_exit.clicked.connect(self.exit_admin)
        self.li_password.setValidator(QIntValidator(self))   #................. 
        print('init calisti')
        
    def add_customer(self):
        self.name=self.li_name.text()
        self.surname=self.li_surname.text()
        self.email=self.li_email.text()
        self.firstbalance=self.li_balance.text()
        self.id_number=self.li_accountno.text()
        self.password= self.li_password.text()
        self.now=str(datetime.datetime.now())
        
        print('pass,id_num,alindi')
        if self.name=="" or self.surname=="" or self.email=="" or self.id_number == 0 or self.password== 0 : #.......
            self.la_error.setText("Please input all fields.")
            print("Bosluklar kontrol edildi")
        else:
        
    
            with open('allcustomers1.csv','a',encoding="utf-8") as file:
                file.write(self.name+','+self.surname+','+self.email+','+str(self.id_number)+','+str(self.firstbalance)+','+str(self.password)+','+str(self.now)+'\n')  #.....iceri aldim
        print('dosya acti bilgileri yazdi')
        self.li_name.clear()
        self.li_surname.clear()
        self.li_email.clear()
        self.li_balance.clear()
        self.li_accountno.clear()
        self.li_password.clear()

             
      
    def show_allcustomers(self):
        allcustScreen = allcustomerScreen()
        widget.addWidget(allcustScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
           
    def exit_admin(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()-1)

class allcustomerScreen(QDialog):
    def __init__(self):
        super(allcustomerScreen,self).__init__()
        loadUi('all_customer.ui', self)
        self.B_exit.clicked.connect(self.exit_allcustom)
        self.B_refresh.clicked.connect(self.loadCsv)
             
    def loadCsv(self):
         with open ('allcustomers1.csv','r')as f:
            
            pass
                    
    def exit_allcustom(self):
        adminScreen = AdminScreen()
        widget.addWidget(adminScreen)
        widget.setCurrentIndex(widget.currentIndex()-1)

class CustomerScreen(QMainWindow):
    def __init__(self):
        super(CustomerScreen, self).__init__()
        loadUi('customerpage.ui', self)
        print('cust init çalıştı')
        #print(self.id)
        self.B_deposit.clicked.connect(self.button_deposit)
        self.B_withdraw.clicked.connect(self.button_withdraw)
        self.B_exit_cust_menu.clicked.connect(self.button_exit)
        self.B_changePassword.clicked.connect(self.change_password)
        self.B_statement.clicked.connect(self.account_statement)
        
        
        with open('allcustomers1.csv','r',encoding='utf8') as cf :
           customers = cf.readlines()
           #print(customers)
           
        cf= pd.read_csv('allcustomers1.csv')
        listcf=cf[["id_number",'password']]
        #print(listcf) 
        
    def button_deposit(self):
        depositScreen = DepositScreen()
        widget.addWidget(depositScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
    #go to screen import(deposit) money

    def button_withdraw(self):
        withdrawScreen = WithdrawScreen()
        widget.addWidget(withdrawScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
    #go to screen withdraw money

    def change_password(self):
        pass

    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)

        widget.setCurrentIndex(widget.currentIndex()-1)

    #go to login screen

    def current_balance(self):
        #-if id_number ==
        pass 
        balance = []
        for person in balance:
            pass
    #show the current balance(csv)

    def account_statement(self):
        accountScreen = AccountState()
        widget.addWidget(accountScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class DepositScreen(QMainWindow):
    def __init__(self):
         super(DepositScreen, self).__init__()
         loadUi("insertpage.ui", self)
         self.buttons()
         

    def buttons(self):
        self.B_exit.clicked.connect(self.button_exit)
        self.B_back.clicked.connect(self.button_back)
        #self.B_ok.clicked.connect()
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
    #self.button.clicked.connect()

    def button_ok():
        pass
    #csv dosyasını yenileme
    #tarih-saat-işlem kaydı
    
    def button_back(self):
        customerScreen = CustomerScreen()
        widget.addWidget(customerScreen)
        widget.setCurrentIndex(widget.currentIndex()-1)
    #go to previous screen

    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()-1)
    #go to login screen

    def current_balance():
        pass
    #show the current balance(csv)
    
    def deposit_cash():
        pass
    #butondan değer alma
    #yazarak değer alma
    #clicked ok will take this value

    def action0(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "0")
 
    def action1(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "1")
 
    def action2(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "2")
 
    def action3(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "3")
 
    def action4(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "4")
 
    def action5(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "5")
 
    def action6(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "6")
 
    def action7(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "7")
 
    def action8(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "8")
 
    def action9(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "9")
 
    def action_clear(self):
        # clearing the label text
        self.li_amount_withdraw.setText("")
 
    def action_del(self):
        # clearing a single digit
        text = self.li_amount_withdraw.text()
        print(text[:len(text)-1])
        self.li_amount_withdraw.setText(text[:len(text)-1])

class WithdrawScreen(QMainWindow):
    def __init__(self):
        super(WithdrawScreen, self).__init__()
        loadUi("withdrawpage.ui", self)
        #self.show()
        self.buttons()
        #self.go_to_loginscreen = LoginScreen()
        #self.go_to_customerscreen = CustomerScreen()

    def buttons(self):
        self.B_exit.clicked.connect(self.button_exit)
        self.B_back.clicked.connect(self.button_back)
        #self.B_ok.clicked.connect()
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
        self.B_10.clicked.connect(self.action10)
        self.B_20.clicked.connect(self.action20)
        self.B_50.clicked.connect(self.action50)
        self.B_100.clicked.connect(self.action100)
        self.B_200.clicked.connect(self.action200)
        self.B_500.clicked.connect(self.action500)
    

    def button_ok():
        pass
    #csv dosyasını yenileme
    #tarih-saat-işlem kaydı

    def button_back(self):
        customerScreen = CustomerScreen()
        widget.addWidget(customerScreen)
        widget.setCurrentIndex(widget.currentIndex()-1)
        
    #go to previous screen
    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()-2)
    
    #go to login screen

    def current_balance():
        pass
    #show the current balance(csv)

    def withdraw_cash():
        pass
    #butondan değer alma
    #yazarak değer alma
    #clicked ok will take this value

    def action0(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "0")
 
    def action1(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "1")
 
    def action2(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "2")
 
    def action3(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "3")
 
    def action4(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "4")
 
    def action5(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "5")
 
    def action6(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "6")
 
    def action7(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "7")
 
    def action8(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "8")
 
    def action9(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "9")
 
    def action_clear(self):
        # clearing the label text
        self.li_amount_withdraw.setText("")
 
    def action_del(self):
        # clearing a single digit
        text = self.li_amount_withdraw.text()
        print(text[:len(text)-1])
        self.li_amount_withdraw.setText(text[:len(text)-1])

    def action10(self):
        self.li_amount_withdraw.setText("10")
    
    def action20(self):
        self.li_amount_withdraw.setText("20")

    def action50(self):
        self.li_amount_withdraw.setText("50")

    def action100(self):
        self.li_amount_withdraw.setText("100")

    def action200(self):
        self.li_amount_withdraw.setText("200")

    def action500(self):
        self.li_amount_withdraw.setText("500")

class AccountState(QDialog):
    def __init__(self) :
        super(AccountState,self).__init__()
        loadUi('statementpage.ui', self)
        self.B_exit_state.clicked.connect(self.exit_state)
        
    
    def exit_state(self):
        customerScreen = CustomerScreen()
        widget.addWidget(customerScreen)
        widget.setCurrentIndex(widget.currentIndex()-2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginScreen()
    widget = QStackedWidget()
    widget.addWidget(window)
    widget.setFixedHeight(1000)
    widget.setFixedWidth(1000)
    widget.show()
    sys.exit(app.exec_())
