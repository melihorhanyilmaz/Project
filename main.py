import sys, random, datetime, csv, re, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import psycopg2


class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("atmloginpage.ui", self)
        self.la_welcome.show()
        self.li_id.setValidator(QIntValidator(self))
        self.okB.clicked.connect(self.login)
    
    def login(self):
        self.id_number=str(self.li_id.text())
        self.password=self.li_password.text()
        CustomerScreen.id = self.id_number
        WithdrawScreen.id = self.id_number
        DepositScreen.id = self.id_number
        CustomerInfoScreen.id = self.id_number
        CustomerSettings.id = self.id_number
        InternalScreen.id = self.id_number
        ExternalScreen.id = self.id_number
      
        #try: 
        if str(self.id_number).startswith("1") and len(self.id_number) == 7:
            conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
            cur = conn.cursor() 
            cur.execute("SELECT * FROM admin_info WHERE admin_id = '"+ self.id_number +"'")
            result=cur.fetchone()
            if result:
                self.go_to_admin_page()
            cur.close()
            conn.commit()
            conn.close()
    
        elif str(self.id_number).startswith("999") and len(self.id_number) == 7:
            
            conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
            cur = conn.cursor() 
            cur.execute("SELECT * FROM customer_info WHERE customer_id = ' "+ self.id_number +"' and password = '"+ self.password +"'")
            result=cur.fetchone()
            if result:
                self.go_to_customer_page()
            elif len(self.id_number) < 7 or str(self.id_number).startswith('9'):
                self.la_error.setText("Please input valid IDNumber and Password")
            cur.close()
            conn.commit()
            conn.close()

        else: 
            self.la_error.setText("Please input valid IDNumber and Password")
        #except:
                #self.la_error.setText("Please input Password")


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

        conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
        cur = conn.cursor()
        cur.execute("SELECT SUM(balance) FROM customer_info") 
        totalmoney=cur.fetchone()[0]
        cur.close()
        conn.commit()
        conn.close()
        self.la_totalmoney.setText(str(totalmoney))

        conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
        cur = conn.cursor()
        cur.execute("SELECT SUM(withdraw_money) FROM customer_info") 
        dwithdraw=cur.fetchone()[0]
        cur.close()
        conn.commit()
        conn.close()
        self.la_dailywithdraw.setText(str(dwithdraw))

        conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
        cur = conn.cursor()
        cur.execute("SELECT SUM(deposit_money) FROM customer_info") 
        ddeposit=cur.fetchone()[0]
        cur.close()
        conn.commit()
        conn.close()
        self.la_dailydeposit.setText(str(ddeposit))

    def button_info(self):
        custInfoScreen = CustomerInfoScreen()
        widget.addWidget(custInfoScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_new_customer(self):
        createCustScreen = CreateCustomerScreen()
        widget.addWidget(createCustScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_update_customer(self):
        updateScreen = UpdateScreen()
        widget.addWidget(updateScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_exit(self):
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
    def __init__(self):
        super(CreateCustomerScreen, self).__init__()
        loadUi("createcustomerpage.ui", self)
        self.B_save.clicked.connect(self.add_customer)
        self.B_back.clicked.connect(self.button_back)
        self.B_exit.clicked.connect(self.button_exit)

    def add_customer(self):
        self.name=self.li_name.text()
        self.surname = self.li_surname.text()
        self.email = self.li_email.text()
        self.firstbalance = int(self.li_balance.text())
        self.password = self.li_password.text()
        self.now = str(datetime.datetime.now())
        
       
        self.withdrawmoney = 0
        self.depositmoney = 0
        self.sum = 0
        WithdrawScreen.firstbalance = self.firstbalance
        DepositScreen.firstbalance = self.firstbalance
        CustomerScreen.balance = self.firstbalance     
        
        if self.name=="" or self.surname=="" or self.email=="" or self.password== 0 : 
            self.la_error.setText("Please input all fields.")
        else:
            conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
            cur = conn.cursor() 
            cur.execute('INSERT INTO customer_info (password, first_name, surname, email, balance) VALUES(%s,%s,%s,%s,%s)',(self.password,str(self.name),str(self.surname),str(self.email),self.firstbalance))
            cur.close()
            conn.commit()
            conn.close()
            self.la_error.setText("Succesfully Created")

           
            self.li_name.clear()
            self.li_surname.clear()
            self.li_email.clear()
            self.li_balance.clear()
            self.li_password.clear()
            
        
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
        self.customer_id=self.li_customerid.text()
        self.new_name=self.li_name.text()      
        self.new_surname = self.li_surname.text()
        self.new_email = self.li_email.text()
        self.new_password = self.li_newpassword.text()
        #self.now = str(datetime.datetime.now())
        
        if self.new_name=="" or self.new_surname=="" or self.new_email=="" or self.new_password== 0 : 
            self.la_error.setText("Please input all fields.")
            
         
        else:
            conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
            cur = conn.cursor()
            cur.execute('UPDATE customer_info SET first_name=%s where customer_id=%s',(self.new_name,self.customer_id))
            cur.execute('UPDATE customer_info SET surname=%s where customer_id=%s',(self.new_surname,self.customer_id))
            cur.execute('UPDATE customer_info SET email=%s where customer_id=%s',(self.new_email,self.customer_id))
            cur.execute('UPDATE customer_info SET password=%s where customer_id=%s',(self.new_password,self.customer_id))
            cur.close()
            conn.commit()
            conn.close()
            self.la_error.setText("Succesfully Changed")

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
        self.B_deposit.clicked.connect(self.button_deposit)
        self.B_withdraw.clicked.connect(self.button_withdraw)
        self.B_exit_cust_menu.clicked.connect(self.button_exit)
        self.B_statement.clicked.connect(self.account_statement)
        self.B_settings.clicked.connect(self.button_settings)
        self.B_internal.clicked.connect(self.button_internal)
        self.B_external.clicked.connect(self.button_external)
     
        conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
        cur = conn.cursor()
        cur.execute("SELECT balance FROM customer_info WHERE customer_id = '"+ self.id +"'") 
        result=cur.fetchone()[0]
        cur.close()
        conn.commit()
        conn.close()
        self.la_balance.setText(str(result))
       
        
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
        statementScreen = StatementScreen()
        widget.addWidget(statementScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_settings(self):
        changecustomer = CustomerSettings()
        widget.addWidget(changecustomer)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_internal(self):
        self.internalScreen = InternalScreen()
        widget.addWidget(self.internalScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_external(self):
        self.externalScreen = ExternalScreen()
        widget.addWidget(self.externalScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
   
class CustomerSettings(QMainWindow):
    def __init__(self):
        super(CustomerSettings,self).__init__() 
        loadUi('settingscustomer.ui', self)
        self.B_exit.clicked.connect(self.button_exit)
        self.B_back.clicked.connect(self.button_back)
        self.B_save.clicked.connect(self.save_change)

    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_back(self):
        self.customerScreen = CustomerScreen()
        widget.addWidget(self.customerScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def save_change(self):
        self.new_email=self.li_name.text()      #buradaki buton adlarini new_name,new_email yapmali miyiz?
        self.new_password = self.li_password.text()
        self.new_confpassword = self.li_confpass.text()
        #self.now = str(datetime.datetime.now())
        
        if self.new_email=="" or self.new_password == "" or self.new_confpassword == "" or self.new_password != self.new_confpassword:
            self.la_error.setText("Please input all fields.")
            #print("Bosluklar kontrol edildi")
            
        else:
            conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
            cur = conn.cursor()
            cur.execute('UPDATE customer_info SET email=%s where customer_id=%s',(self.new_email,self.id))
            cur.execute('UPDATE customer_info SET password=%s where customer_id=%s',(self.new_password,self.id))
            cur.close()
            conn.commit()
            conn.close()
            self.la_error.setText("Succesfully Changed")
       
class DepositScreen(QMainWindow):
    def __init__(self): 
        super(DepositScreen, self).__init__()
        loadUi("insertpage.ui", self)
        
        conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
        cur = conn.cursor()
        cur.execute("SELECT balance FROM customer_info WHERE customer_id = '"+ self.id +"'") 
        result=cur.fetchone()[0]
        cur.close()
        conn.commit()
        conn.close()
        self.la_balance.setText(str(result))
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
        #try:
        conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
        cur = conn.cursor()
        cur.execute("SELECT balance FROM customer_info WHERE customer_id = '"+ self.id +"'") 
        result=cur.fetchone()[0]
        cur.close()
        conn.commit()
        conn.close()
        if result: 
            self.new_balance = result + int(self.money)    
        conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
        cur = conn.cursor()
        cur.execute('UPDATE customer_info SET deposit_money = %s WHERE customer_id=%s',(self.money,self.id))
        cur.execute('UPDATE customer_info SET balance= %s WHERE customer_id = %s', (self.new_balance, self.id))
        cur.close()
        conn.commit()
        conn.close()
        self.la_error.setText("Your money is in the account.")
        self.la_balance.setText(str(self.new_balance))
        # except:
        #    self.la_error.setText("Something went wrong. Please try again")
                
              
        
        
        #self.button_back()
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
        
        conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
        cur = conn.cursor()
        cur.execute("SELECT balance FROM customer_info WHERE customer_id = '"+ self.id +"'") 
        result=cur.fetchone()[0]
        cur.close()
        conn.commit()
        conn.close()
        self.la_balance.setText(str(result))
        self.buttons()

    def buttons(self):
        #Gself.B_exit.clicked.connect(self.button_exit)
        self.B_back.clicked.connect(self.button_back)
        self.B_ok.clicked.connect(self.button_ok)
        self.B_exit.clicked.connect(self.button_exit)
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
        self.money=self.li_amount_withdraw.text() 
        #try:
        conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
        cur = conn.cursor()
        cur.execute("SELECT balance FROM customer_info WHERE customer_id = '"+ self.id +"'") 
        result=cur.fetchone()[0]
        cur.close()
        conn.commit()
        conn.close()
        if result>int(self.money): 
            self.new_balance = result - int(self.money)
            conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
            cur = conn.cursor()
            cur.execute('UPDATE customer_info SET withdraw_money = %s WHERE customer_id=%s',(self.money,self.id))
            cur.execute('UPDATE customer_info SET balance= %s WHERE customer_id = %s', (self.new_balance, self.id))
            cur.close()
            conn.commit()
            conn.close()
            self.la_error.setText(f"From your account {self.money} € has been withdrawn")
            self.la_balance.setText(str(self.new_balance))
        else: 
            self.la_error.setText(f"You have only {result} € in your account")
        #except:
            #self.la_error.setText("Something went wrong. Please try again")
        
         
        #self.button_back()

    #csv dosyasını yenileme
    #tarih-saat-işlem kaydı

    def button_back(self):
        self.customerScreen = CustomerScreen()
        widget.addWidget(self.customerScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    #go to previous screen
    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
   

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

class InternalScreen(QMainWindow):
    def __init__(self):
        super(InternalScreen, self).__init__()
        loadUi("internal.ui", self)
        self.la_welcome.show()
        self.la_balance.show()
        self.li_id.setValidator(QIntValidator(self))
        self.B_exit.clicked.connect(self.button_exit)
        self.B_back.clicked.connect(self.button_back)
        self.B_send.clicked.connect(self.button_internal_send)
    
    def button_internal_send(self):
        id_alici=str(self.li_alici_id.text())
        send_amount=(self.li_amount.text())
        name_alici=str(self.li_alici_name.text())
        surname_alici=str(self.li_alici_surname.text())
        #checking if id number exist or not
        conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
        cur = conn.cursor()
        cur.execute("SELECT balance FROM customer_info WHERE customer_id = %s"+ (self.id))###self.customer_id mi olmali?
        balance=cur.fetchone()[0]
        if not balance:
            self.la_error.setText("ID NUMBER is not exist.Please enter a invalid ID Number")
            cur.close()
            conn.close()
        else: #check if recipient's name and surname match with ID number
            conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
            cur = conn.cursor()
            cur.execute("SELECT * FROM customer_info WHERE customer_id = %s AND first_name=%s AND surname=%s",(id_alici,name_alici,surname_alici))
            result_match=cur.fetchone()
            if not result_match:
                self.la_error.setText("Recipient ID ,Name and Surname not matched!!!")
                cur.close()
                conn.close()
                return
            else:#bakiye dusur ve upload yap##########uploadi externalda yapmayi unttum onu da yap
                if (send_amount)>0 and (send_amount)<=balance:
                    conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
                    cur = conn.cursor()
                    cur.execute("UPDATE customer_info SET balance=%s WHERE customer_id=%s ",(balance,self.customer_id) )
                    ###########self.customer_id mi olacak???????????????????????????????????????????????????????
                    conn.commit()
                    self.balance.setText(str(balance))
                    self.la_error.setText("Money Transfer succesful!")
                else:
                    self.la_error.setText("Insufficient Current Balance")
                cur.close()
                conn.close()
    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def button_back(self):
        self.customerScreen = CustomerScreen()
        widget.addWidget(self.customerScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ExternalScreen(QMainWindow):
    def __init__(self):
        super(ExternalScreen, self).__init__()
        loadUi("external.ui", self)
        self.la_welcome.show()
        self.la_balance.show()
        self.li_id.setValidator(QIntValidator(self))
        self.B_exit.clicked.connect(self.button_exit)
        self.B_back.clicked.connect(self.button_back)
        self.B_send.clicked.connect(self.button_external_send)

    def button_external_send(self):
        id_alici=str(self.li_alici_id.text())
        send_amount=float(self.li_amount.text())
        balance=self.balance
        conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")
        cur = conn.cursor()
        cur.execute("SELECT * FROM customer_info WHERE customer_id = %s"+ (self.id))
        result1=cur.fetchone()
        if result1 is None:
            #Allow external money transfer
            if send_amount   > 0 and send_amount<=balance:
                 balance=balance-send_amount
                 #Update the balance
            else:
                 self.la_error.setText(" Insufficient Current Balance ,please check your Current Balance")
        else:
            #Deny External money transfer as recipient is a customer of the Bank
             self.la_error.setText("Please choose Internal Money Transfer Option")
        cur.close()
        conn.commit()
        conn.close()

    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def button_back(self):
        self.customerScreen = CustomerScreen()
        widget.addWidget(self.customerScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class StatementScreen(QDialog):
    def __init__(self):
        super(StatementScreen,self).__init__() 
        loadUi('accountstatementpage.ui', self)
        self.B_back.clicked.connect(self.button_back)
        self.B_exit.clicked.connect(self.button_exit)
        self.tableWidget.setColumnWidth(0,125)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,75)
        self.tableWidget.setColumnWidth(4,100)
        self.now = datetime.datetime.now()

        # File name.
        fileName = 'customer_actions.csv'

        # Database connection variable.
        connect = None

        # Check if the file path exists.
        if os.path.exists(fileName):

            try:

                # Connect to database.
                conn = psycopg2.connect("dbname=atm_proje user = postgres password=12345")

            except psycopg2.DatabaseError as e:

                # Confirm unsuccessful connection and stop program execution.
                print("Database connection unsuccessful.")
                quit()

            # Cursor to execute query.
            cursor = conn.cursor()

            # SQL to select data from the person table.
            sqlSelect = \
                "SELECT custactions_id, customer_id, cust_actions, amount, action_date \
                FROM customer_actions"

            try:

                # Execute query.
                cursor.execute(sqlSelect)

                # Fetch the data returned.
                results = cursor.fetchall()

                # Extract the table headers.
                headers = [i[0] for i in cursor.description]

                # Open CSV file for writing.
                csvFile = csv.writer(open(fileName, 'w'),
                                    delimiter=',', lineterminator='\r\n',
                                    quoting=csv.QUOTE_ALL, escapechar='\\')

                # Add the headers and data to the CSV file.
                csvFile.writerow(headers)
                csvFile.writerows(results)

                # Message stating export successful.
                print("Data export successful.")

            except psycopg2.DatabaseError as e:

                # Message stating export unsuccessful.
                print("Data export unsuccessful.")
                quit()

        else:

            # Message stating file path does not exist.
            print("File path does not exist.")

    def button_back(self):
        customerScreen = CustomerScreen()
        widget.addWidget(customerScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_exit(self):
        loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)


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
