import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5 import QtSql
from appConnection import dbConnection

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Главное меню')
        self.resize(640, 350)

        work_layout = QGridLayout()

        label_name = QLabel('<font size="18"> StudentPack </font>')
        work_layout.addWidget(label_name, 0, 0)
        
        label_first = QLabel('<font size="8"> Данные I уровня </font>')
        button_user = QPushButton('Пользователи')
        # button_user.clicked.connect(self.to_User)
        work_layout.addWidget(label_first, 1, 0)
        work_layout.addWidget(button_user, 2, 0)

        label_second = QLabel('<font size="8"> Данные II уровня </font>')
        work_layout.addWidget(label_second, 3, 0)
        
        label_third = QLabel('<font size="8"> Данные III уровня </font>')
        work_layout.addWidget(label_third, 5, 0)
        
        self.setLayout(work_layout)

if __name__ == '__main__':
    dbConnection()