import sys, random, datetime, csv, re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import psycopg2
from PyQt5.QtSql import *

class StatementScreen(QDialog):
    def __init__(self):
        super(StatementScreen,self).__init__() 
        loadUi('accountstatementpage.ui', self)
        self.tableWidget.setColumnWidth(0,125)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,75)
        self.tableWidget.setColumnWidth(4,100)
        self.tableWidget.setHorizontalHeaderLabels(["Customer Action ID", "Customer ID", "Action", "Amount", "Date"])
        """db = QSqlDatabase.addDatabase("QPSQL")
        db.setHostName("localhost")
        db.setPort(5432)
        db.setDatabaseName("atm_proje")
        db.setUserName("postgres")
        db.setPassword("12345")
        if (db.open() == False):
            QMessageBox.critical(None, "Database Error", db.lastError().text())"""
        db =  psycopg2.connect("dbname=atm_proje user = postgres password=12345")
        cur = db.cursor() 
        self.db = db
        self.model = QSqlTableModel(self.db)
        self.model.setTable("customer_actions")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.view = QTableView(self)
        self.view.setModel(self.model)

    """def loaddata(self):
        connection = sqlite3.connect("data.sqlite")
        cur = connection.cursor()
        sqlquery = "SELECT * FROM """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StatementScreen()
    widget = QStackedWidget()
    widget.addWidget(window)
    widget.setFixedHeight(1000)
    widget.setFixedWidth(1000)
    widget.show()
    try:
        sys.exit(app.exec_())

    except:
        print("Closing")
