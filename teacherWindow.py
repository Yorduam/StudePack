import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtSql, QtWidgets, QtCore
from PyQt5.QtGui import *
from appConnection import dbConnection

class TeacherWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Преподаватели')
        self.resize(700, 700)

        self.initUI()
    
    def initUI(self):
        self.w = QtWidgets.QWidget()
        self.w.setWindowTitle('Преподаватели')

        dbConnection()

        self.stm = QtSql.QSqlTableModel(parent=self.w)
        self.stm.setTable('Teacher')
        self.stm.select()
        
        self.stm.setHeaderData(0, QtCore.Qt.Orientation.Horizontal,'teacher_id')
        self.stm.setHeaderData(1, QtCore.Qt.Orientation.Horizontal,'teacher_name')
        self.stm.setHeaderData(2, QtCore.Qt.Orientation.Horizontal,'teacher_date')
        self.stm.setHeaderData(3, QtCore.Qt.Orientation.Horizontal,'teacher_number')
        self.stm.setHeaderData(4, QtCore.Qt.Orientation.Horizontal,'teacher_email')

        vbox = QtWidgets.QVBoxLayout()
        self.tv = QtWidgets.QTableView()
        self.tv.setModel(self.stm)
        self.tv.hideColumn(0)
        vbox.addWidget(self.tv)
        self.btnAdd = QtWidgets.QPushButton('Добавить запись')
        self.btnDel = QtWidgets.QPushButton('Удалить запись')
        self.btnAdd.clicked.connect(self.addRecord)
        vbox.addWidget(self.btnAdd)
        self.btnDel.clicked.connect(self.delRecord)
        vbox.addWidget(self.btnDel)
        self.setLayout(vbox)
        self.w.resize(500, 500)
        self.w.show

    def addRecord(self):
        self.stm.insertRow(self.stm.rowCount())

    def delRecord(self):
        self.stm.removeRow(self.tv.currentIndex().row())
        self.stm.select()