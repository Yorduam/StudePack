import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtSql, QtWidgets, QtCore
from PyQt5.QtGui import *
from appConnection import dbConnection, dbRequest

class GroupWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Учебные группы')
        self.resize(700, 700)

        self.initUI()
    
    def initUI(self):
        self.w = QtWidgets.QWidget()
        self.w.setWindowTitle('Учебные группы')

        dbConnection()

        self.stm = QtSql.QSqlTableModel(parent=self.w)
        self.stm.setTable('StudyGroup')
        self.stm.select()
        
        self.stm.setHeaderData(0, QtCore.Qt.Orientation.Horizontal,'group_id')
        self.stm.setHeaderData(1, QtCore.Qt.Orientation.Horizontal,'group_name')
        self.stm.setHeaderData(2, QtCore.Qt.Orientation.Horizontal,'group_specialization')
        self.stm.setHeaderData(3, QtCore.Qt.Orientation.Horizontal,'group_teacher')

        vbox = QtWidgets.QVBoxLayout()
        self.tv = QtWidgets.QTableView()
        self.tv.setModel(self.stm)
        self.tv.hideColumn(0)
        vbox.addWidget(self.tv)
        self.btnAdd = QtWidgets.QPushButton('Добавить запись')
        self.btnDel = QtWidgets.QPushButton('Удалить запись')
        self.btnExp = QtWidgets.QPushButton('Печать')
        self.btnAdd.clicked.connect(self.addRecord)
        vbox.addWidget(self.btnAdd)
        self.btnDel.clicked.connect(self.delRecord)
        vbox.addWidget(self.btnDel)
        self.btnExp.clicked.connect(self.expRecord)
        vbox.addWidget(self.btnExp)
        self.setLayout(vbox)
        self.w.resize(500, 500)
        self.w.show

    def addRecord(self):
        self.stm.insertRow(self.stm.rowCount())

    def delRecord(self):
        self.stm.removeRow(self.tv.currentIndex().row())
        self.stm.select()

    def expRecord(self):
        dbRequest.expStudyGroup()