import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5 import QtSql
from appConnection import dbCreate, dbConnection
import mainWindow

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Авторизация')
        self.resize(500, 120)

        auth_layout = QGridLayout()

        label_title = QLabel('<font size="4"> Авторизация </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Введите логин')
        auth_layout.addWidget(label_title, 0, 0)
        auth_layout.addWidget(self.lineEdit_username, 0, 1)
        
        label_password = QLabel('<font size="4"> Пароль </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Введите пароль')
        auth_layout.addWidget(label_password, 1, 0)
        auth_layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Войти')
        button_login.clicked.connect(self.login_check)
        auth_layout.addWidget(button_login, 2, 0, 1, 2)
        auth_layout.setRowMinimumHeight(2, 75)
        
        self.setLayout(auth_layout)

    def login_check(self):
        login = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        msg = QMessageBox()

        query = QtSql.QSqlQuery()

        query.prepare('SELECT COUNT(*) FROM User WHERE user_login=? AND user_password=?')
        query.bindValue(0, login)
        query.bindValue(1, password)
        query.exec()
        if query.first():
            if int(query.value(0)) > 0:
                print(f'Ⓜ️ Пользователь {login} авторизовался!')
                msg.setText('Вход выполнен успешно!')
                msg.exec_()
                formWork.show()
                form.close()
            else:
                msg.setText('Данный пользователь не найден!')
                msg.exec_()
        else:
            print('⚠️ Ошибка при проверке пользователя!')

if __name__ == '__main__':
    dbCreate()
    dbConnection()
    app = QApplication(sys.argv)

    form = LoginForm()
    formWork = mainWindow.MainWindow()
    form.show()

    sys.exit(app.exec_())