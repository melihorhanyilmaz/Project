import sys, os, csv
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
        self.tableWidget.setColumnWidth(0,400)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,250)
        self.loaddata()
    
    def loaddata(self):
        pass


