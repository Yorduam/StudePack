import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5 import QtSql, QtGui
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Главное меню')
        self.resize(640, 350)

        work_layout = QGridLayout()

        label_name = QLabel('<font size="18"> StudentPack </font>')
        work_layout.addWidget(label_name, 0, 1)
        
        label_first = QLabel('<font size="6"> Данные I уровня </font>')
        work_layout.addWidget(label_first, 1, 1)
        button_user = QPushButton('Пользователи')
        button_teacher = QPushButton('Преподаватели')
        # button_user.clicked.connect(self.to_User)
        work_layout.addWidget(button_user, 2, 0)
        work_layout.addWidget(button_teacher, 2, 1)

        label_second = QLabel('<font size="6"> Данные II уровня </font>')
        work_layout.addWidget(label_second, 3, 1)
        button_group = QPushButton('Группы')
        work_layout.addWidget(button_group, 4, 1)
        
        label_third = QLabel('<font size="6"> Данные III уровня </font>')
        work_layout.addWidget(label_third, 5, 1)
        button_student = QPushButton('Студенты')
        work_layout.addWidget(button_student, 6, 1)
        

        label_about = QLabel('<font size="4"> @Yordu v.0.3.0</font>')
        work_layout.addWidget(label_about, 7, 0)
        self.setLayout(work_layout)