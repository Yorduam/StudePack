import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtSql, QtWidgets, QtCore
from PyQt5.QtGui import *
from appConnection import dbConnection

class StudentsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Студенты')
        self.resize(700, 700)

        self.initUI()
    
    def initUI(self):
        self.w = QtWidgets.QWidget()
        self.w.setWindowTitle('Студенты')

        dbConnection()

        self.stm = QtSql.QSqlTableModel(parent=self.w)
        self.stm.setTable('Students')
        self.stm.select()
        
        self.stm.setHeaderData(0, QtCore.Qt.Orientation.Horizontal,'student_id')
        self.stm.setHeaderData(1, QtCore.Qt.Orientation.Horizontal,'student_name')
        self.stm.setHeaderData(2, QtCore.Qt.Orientation.Horizontal,'student_date')
        self.stm.setHeaderData(3, QtCore.Qt.Orientation.Horizontal,'student_group')
        self.stm.setHeaderData(4, QtCore.Qt.Orientation.Horizontal,'student_number')
        self.stm.setHeaderData(5, QtCore.Qt.Orientation.Horizontal,'student_email')
        self.stm.setHeaderData(6, QtCore.Qt.Orientation.Horizontal,'student_passport')
        self.stm.setHeaderData(7, QtCore.Qt.Orientation.Horizontal,'student_snils')
        self.stm.setHeaderData(8, QtCore.Qt.Orientation.Horizontal,'student_inn')
        self.stm.setHeaderData(9, QtCore.Qt.Orientation.Horizontal,'student_gto')
        self.stm.setHeaderData(10, QtCore.Qt.Orientation.Horizontal,'student_motherName')
        self.stm.setHeaderData(11, QtCore.Qt.Orientation.Horizontal,'student_motherNumber')
        self.stm.setHeaderData(12, QtCore.Qt.Orientation.Horizontal,'student_motherEmail')
        self.stm.setHeaderData(13, QtCore.Qt.Orientation.Horizontal,'student_fatherName')
        self.stm.setHeaderData(14, QtCore.Qt.Orientation.Horizontal,'student_fatherNumber')
        self.stm.setHeaderData(15, QtCore.Qt.Orientation.Horizontal,'student_fatherEmail')

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