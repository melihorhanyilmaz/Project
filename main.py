import pandas as pd
import sys, random, datetime, csv, re
from PyQt5 import QtCore, QtGui, QtWidgets
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
        CustomerInfoScreen.id = self.id_number
      
        
        #pandas kodları
        datadf=pd.read_csv('allcustomers1.csv')  
        #df.loc[df['id_number'] == int(self.id_number),('firstbalance')]
        #checkpassword =len(df[df['id_number'] == int(self.id_number)]['password'])
        #idnumber = len(df[df['id_number'] == int(self.id_number)]['id_number'])
        
        
        #Pf len(self.id_number)==0 or len(self.password)==0 :
           # self.la_error.setText("Please input all fields.")
            
        #elif len(self.id_number) < 7 or len (self.password) < 7:
        #    self.la_error.setText("Please input valid IDNumber or Password")
        #if checkpassword == self.password :
        
        #ve password gecerli ise ibaresini de gir???
        
           
        df = pd.DataFrame(datadf)
        # df[(df[str('id_number')] != str(self.id_number)) | (df[str('password')] != str(self.password))]
        #self.la_error.setText("Please input a valid IDNumber or Password")
        df.loc[(df[str('id_number')] == str(self.id_number)) & (df[str('password')] == str(self.password))]
        if str(self.id_number).startswith("999") and len(self.id_number) == 7:
            self.go_to_customer_page()
            
        elif self.id_number == "0112233" and self.password == "1223330":
                print("Startswith0")
                self.go_to_admin_page()
        
        else: 
            self.la_error.setText("Please input valid IDNumber or Password")
                


    def go_to_customer_page(self):
        self.li_id.clear()
        self.li_password.clear()
        customerScreen = CustomerScreen()
        widget.addWidget(customerScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

    def go_to_admin_page(self):
        self.li_id.clear()
        self.li_password.clear()
        adminScreen = NewAdminScreen()
        widget.addWidget(adminScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class NewAdminScreen(QMainWindow):
    def __init__(self):
        super(NewAdminScreen,self).__init__() 
        loadUi('newadminpage.ui', self)
        #print('cust init çalıştı')
        #print(self.id)
        self.B_info.clicked.connect(self.button_info)
        self.B_newcust.clicked.connect(self.button_new_customer)
        self.B_updatecust.clicked.connect(self.button_update_customer)
        self.B_exit.clicked.connect(self.button_exit)  
    
    def button_info(self):
        custInfoScreen = CustomerInfoScreen()
        widget.addWidget(custInfoScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_new_customer():
        createCustScreen = CreateCustomerScreen()
        widget.addWidget(createCustScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_update_customer():
        updateScreen = UpdateScreen()
        widget.addWidget(updateScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_exit():
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CustomerInfoScreen(QDialog):
    def __init__(self):
        super(CustomerInfoScreen,self).__init__()
        loadUi('all_customer.ui', self)
        self.B_back.clicked.connect(self.button_back)
        self.B_exit.clicked.connect(self.exit_allcustom)
        list = ["Melih", "Sema", "Ebubekir"]
        self.c_date_2.addItems(list)
        self.c_date_2.setEditable(True)
        #self.B_refresh.clicked.connect(self.loadCsv)
       
    def button_back(self):
        newAdminScreen = NewAdminScreen()
        widget.addWidget(newAdminScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def exit_allcustom(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateCustomerScreen(QMainWindow):
    id_number= 9990000
    def __init__(self):
        super(CreateCustomerScreen, self).__init__()
        loadUi("createcustomerpage.ui", self)
        self.B_save.clicked.connect(self.add_customer)
        self.B_back.clicked.connect(self.button_back)
        self.B_exit.clicked.connect(self.button_exit)
        #self.li_password.setValidator(QIntValidator(self))   #................. 
        print('init calisti')   
        #setlabel gelecek csvdeki son satırdakindan 1 fazla
        df = pd.read_csv('allcustomers1.csv')
        #Erow = pd.concat(df.iloc[-1,:])
        #print(row)

    def add_customer(self):
        self.name=self.li_name.text()
        self.surname = self.li_surname.text()
        self.email = self.li_email.text()
        self.firstbalance = int(self.li_balance.text())
        self.password = self.li_password.text()
        self.now = str(datetime.datetime.now())
        self.id_number=CreateCustomerScreen.id_number 
        self.id_number+=1
        self.la_id.setText(str(self.id_number))
        self.withdrawmoney = 0
        self.depositmoney = 0
        self.sum = 0
        #CustomerScreen.balance=self.firstbalance
        WithdrawScreen.firstbalance = self.firstbalance
        DepositScreen.firstbalance = self.firstbalance     
        
        #print('pass,id_num,alindi')
        if self.name=="" or self.surname=="" or self.email=="" or self.id_number == 0 or self.password== 0 : #.......
            self.la_error.setText("Please input all fields.")
            #print("Bosluklar kontrol edildi")
        else:
        
    
            with open('allcustomers1.csv','a',encoding="utf-8") as file:
                file.write(self.name+','+self.surname+','+self.email+','+str(self.id_number)+','+str(self.firstbalance)+','+str(self.password)+','+str(self.now)+','+str(self.withdrawmoney)+','+str(self.depositmoney)+','+str(self.sum)+'\n')  #.....iceri aldim
                
            with open(f'{self.id_number}.csv','a',encoding="utf-8") as file:
                statement = csv.writer(file)
                statement.writerow(["Date", "Transaction Type","Current Balance"])
                statement.writerow([datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"New Account",self.firstbalance])
            
            #print('dosya acti bilgileri yazdi')
            self.li_name.clear()
            self.li_surname.clear()
            self.li_email.clear()
            self.la_id.update()
            self.li_balance.clear()
            self.li_password.clear()
       
        df=pd.read_csv("allcustomers1.csv") 
        df['sum'] = df.sum(axis=1)
        df.loc[df['id_number'] == (self.id_number),('sum')] = df['firstbalance']
        df.to_csv('allcustomers1.csv', mode ='r+', index = False )    
        print(df)
        
    def button_back(self):
        newAdminScreen = NewAdminScreen()
        widget.addWidget(newAdminScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

           
    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class UpdateScreen(QMainWindow):
    def __init__(self):
        super(UpdateScreen,self).__init__() 
        loadUi('updatepage.ui', self)
        self.B_update.clicked.connect(self.update_customer)
        self.B_back.clicked.connect(self.button_back)
        self.B_exit.clicked.connect(self.button_exit)

    def update_customer(self):
        pass

    def button_back(self):
        newAdminScreen = NewAdminScreen()
        widget.addWidget(newAdminScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CustomerScreen(QMainWindow):
    def __init__(self):
        super(CustomerScreen, self).__init__()
        loadUi('customerpage.ui', self)
        #print('cust init çalıştı')
        #print(self.id)
        self.B_deposit.clicked.connect(self.button_deposit)
        self.B_withdraw.clicked.connect(self.button_withdraw)
        self.B_exit_cust_menu.clicked.connect(self.button_exit)
        self.B_statement.clicked.connect(self.account_statement)
        
        
        

       # with open('allcustomers1.csv','r',encoding='utf8') as df :
          # customers =df.readlines()
      #print(customers)
        df= pd.read_csv('allcustomers1.csv')
        balance=str(df[df['id_number'] == int(self.id)]['sum'])
        self.la_balance.setText(balance)
                
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
    def account_statement(self):
        pass

    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
       
class DepositScreen(QMainWindow):
    def __init__(self): 
        super(DepositScreen, self).__init__()
        loadUi("insertpage.ui", self)
        
        
        df= pd.read_csv('allcustomers1.csv')
        self.balance=str(df[df['id_number'] == int(self.id)]['sum'])
        self.la_balance.setText(self.balance)
        self.buttons()
         

    def buttons(self):
        self.B_exit.clicked.connect(self.button_exit)
        self.B_back.clicked.connect(self.button_back)
        self.B_ok.clicked.connect(self.button_ok)
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

    def button_ok(self):
        self.money=self.li_amount_withdraw.text() 
        print(self.money)
        df=pd.read_csv("allcustomers1.csv")
        #df.loc[df['id_number'] == int(self.id),('withdrawmoney')]=self.amount
        df.loc[df['id_number'] == int(self.id),('depositmoney')]=self.money
        df.to_csv('allcustomers1.csv', mode ='r+', index = False )
        df['sum'] = df.sum(axis=1)
       
        df.loc[df['id_number'] == int(self.id),('sum')] = df['firstbalance'] + int(self.money)
        df.to_csv('allcustomers1.csv', mode ='r+', index = False ) 
        
        file = f"{self.id}.csv"
        with open (file, "a", newline="\n") as f:
            writer = csv.writer(f)
            self.balance=str(df[df['id_number'] == int(self.id)]['sum'])
            writer.writerow([datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"Deposit", self.balance+"€"])
        
        
        
        self.button_back()
    #csv dosyasını yenileme
    #tarih-saat-işlem kaydı
    
    def button_back(self):
        self.customerScreen = CustomerScreen()
        widget.addWidget(self.customerScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
       
    #go to previous screen

    def button_exit(self):
        self.loginScreen = LoginScreen()
        widget.addWidget(self.loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    #go to login screen

   
        
    #show the current balance(csv)
        

   
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
        
        
        df= pd.read_csv('allcustomers1.csv')
        self.balance=str(df[df['id_number'] == int(self.id)]['sum'])
        self.la_balance.setText(self.balance)
        self.buttons()

    def buttons(self):
        #Gself.B_exit.clicked.connect(self.button_exit)
        self.B_back.clicked.connect(self.button_back)
        self.B_ok.clicked.connect(self.button_ok)
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
    

    def button_ok(self):
        self.amount=self.li_amount_withdraw.text() 
        print(self.amount)
        df=pd.read_csv("allcustomers1.csv")
        #df.loc[df['id_number'] == int(self.id),('withdrawmoney')]=self.amount
        df.loc[df['id_number'] == int(self.id),('withdrawmoney')]=self.amount
        df.to_csv('allcustomers1.csv', mode ='r+', index = False ) 
        #Gprint(df['withdrawmoney'].dtypes) 
        
        df['sum'] = df.sum(axis=1)
       
        df.loc[df['id_number'] == int(self.id),('sum')] = df['sum'] - int(self.amount)
        df.to_csv('allcustomers1.csv', mode ='r+', index = False ) 
        #Gdf.to_csv('allcustomers1.csv', mode ='r+', index = False )
        file = f"{self.id}.csv"
        with open (file, "a", newline="\n") as f:
            self.balance=str(df[df['id_number'] == int(self.id)]['sum'])
            writer = csv.writer(f)
            writer.writerow([datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),"Withdraw", self.balance+"€"])
        
        
        
        self.button_back()

    #csv dosyasını yenileme
    #tarih-saat-işlem kaydı

    def button_back(self):
        customerScreen = CustomerScreen()
        widget.addWidget(customerScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    #go to previous screen
    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    #go to login screen

    
        
    #show the current balance(csv)

    #def withdraw_cash(self):
        
        
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

       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginScreen()
    widget = QStackedWidget()
    widget.addWidget(window)
    widget.setFixedHeight(1000)
    widget.setFixedWidth(1000)
    widget.show()
    try:
        sys.exit(app.exec_())

    except:
        print("Closing")
