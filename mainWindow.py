import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtSql, QtGui
from PyQt5.QtCore import Qt
import studentsWindow, userWindow, teacherWindow, groupWindow
from appConnection import configConnection

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Главное меню')
        self.resize(640, 350)

        work_layout = QGridLayout()

        name = configConnection('name')
        version = configConnection('version')

        label_name = QLabel(f'<font size="18"> {name} </font>')
        work_layout.addWidget(label_name, 0, 1)
        
        label_first = QLabel('<font size="6"> Данные I уровня </font>')
        work_layout.addWidget(label_first, 1, 1)
        button_user = QPushButton('Пользователи')
        button_user.clicked.connect(self.open_userWindow)
        button_teacher = QPushButton('Преподаватели')
        button_teacher.clicked.connect(self.open_teacherWindow)
        work_layout.addWidget(button_user, 2, 0)
        work_layout.addWidget(button_teacher, 2, 2)

        label_second = QLabel('<font size="6"> Данные II уровня </font>')
        work_layout.addWidget(label_second, 3, 1)
        button_group = QPushButton('Группы')
        button_group.clicked.connect(self.open_groupWindow)
        work_layout.addWidget(button_group, 4, 1)
        
        label_third = QLabel('<font size="6"> Данные III уровня </font>')
        work_layout.addWidget(label_third, 5, 1)
        button_student = QPushButton('Студенты')
        button_student.clicked.connect(self.open_studentWindow)
        work_layout.addWidget(button_student, 6, 1)
        

        label_about = QLabel(f'<font size="4"> @Yordu v.{version}</font>')
        work_layout.addWidget(label_about, 7, 0)
        self.setLayout(work_layout)

    def open_userWindow(self):
        self.sf = userWindow.UsersWindow()
        self.sf.show()
        
    def open_teacherWindow(self):
        self.sf = teacherWindow.TeacherWindow()
        self.sf.show()
        
    def open_groupWindow(self):
        self.sf = groupWindow.GroupWindow()
        self.sf.show()

    def open_studentWindow(self):
        self.sf = studentsWindow.StudentsWindow()
        self.sf.show()