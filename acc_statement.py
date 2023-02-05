import sys, os, csv, datetime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from customerpage import CustomerScreen

class AccountState(QTableWidget):
    def __init__(self):
        super().__init__()
        loadUi('statementpage.ui',self)
        self.show()
        self.tableWidget.setColumnWidth(0,400)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,250)
        self.loaddata()
        self.now = datetime.datetime.now()
    
    def loaddata(self):
        people = [{"ID Account":9990001, "Date" : self.now, "Action" :self.act_event}]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AccountState()
    window.show()
    sys.exit(app.exec())
    