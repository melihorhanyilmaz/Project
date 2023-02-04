from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from withdrawpage import WithdrawScreen
from depositpage import DepositScreen
from atmloginpage import LoginScreen
from acc_statement import AccountState
import sys

class CustomerScreen(QMainWindow):
    def __init__(self):
         super(CustomerScreen, self).__init__()
         loadUi('customerpage.ui', self)
         self.show()
         self.WithdrawScreen_go= WithdrawScreen()
         self.DepositScreen_go = DepositScreen()
         self.LoginScreen_go = LoginScreen()
         self.account_statement_go = AccountState()
         self.B_deposit.clicked.connect(self.button_deposit)
         self.B_withdraw.clicked.connect(self.button_withdraw)
         self.B_exit_cust_menu.clicked.connect(self.button_exit)
         self.B_changePassword.clicked.connect(self.change_password)
         self.B_statement.clicked.connect(self.account_statement)
         #self.w = None 

    def button_deposit(self):
       self.DepositScreen_go.show()
       self.hide()
    #go to screen import(deposit) money

    def button_withdraw(self):
        self.WithdrawScreen_go.show()
        self.hide()
    #go to screen withdraw money

    def change_password(self):
        pass

    def button_exit(self):
        self.LoginScreen_go.show()
        self.hide()
    #go to login screen

    def current_balance(self):
        pass
    #show the current balance(csv)



    def account_statement(self):
        self.account_statement_go.show()
        self.hide()




    

