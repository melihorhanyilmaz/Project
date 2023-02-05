from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import sys
#from customerpage import CustomerScreen
#from loginpage import LoginScreen

class WithdrawScreen(QMainWindow):
    def __init__(self):
        super(WithdrawScreen, self).__init__()
        loadUi("withdrawpage.ui", self)
        self.show()
        #self.go_to_loginscreen = LoginScreen()
        #self.go_to_customerscreen = CustomerScreen()
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
        self.go_to_customerscreen.show()
        self.hide()
        """customerScreen = CustomerScreen()
        widget.addWidget(customerScreen)
        widget.setCurrentIndex(widget.currentIndex()-1)"""
        
    #go to previous screen

    def button_exit(self):
        """loginScreen = LoginScreen()
        widget.addWidget(loginScreen)
        widget.setCurrentIndex(widget.currentIndex()-1)"""
        self.go_to_loginscreen.show()
        self.hide()
    
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
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "10")
    
    def action20(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "20")

    def action50(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "50")

    def action100(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "100")

    def action200(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "200")

    def action500(self):
        # appending label text
        text = self.li_amount_withdraw.text()
        self.li_amount_withdraw.setText(text + "500")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WithdrawScreen()
    widget = QStackedWidget()
    #widget.show()
    window.show()
    sys.exit(app.exec())
    