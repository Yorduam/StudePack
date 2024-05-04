import sqlite3
from PyQt5 import QtSql

class dbCreate():
    def __init__(self):
        print('🔁 Инициализация базы данных SQLite3')
        connection = sqlite3.connect('students.db') #Подключение или создание БД
        cursor = connection.cursor() #Выполнение SQL-запросов

        try:
            # Таблица пользователей
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS User (
                        user_id INTEGER PRIMARY KEY,
                        user_login TEXT NOT NULL,
                        user_password TEXT NOT NULL
            )
            ''')

            # Таблица специальностей
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Specialization (
                        specialization_id INTEGER PRIMARY KEY,
                        specialization_name TEXT NOT NULL
            )
            ''')

            # Таблица преподавателей
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Teacher (
                        teacher_id INTEGER PRIMARY KEY,
                        teacher_name TEXT NOT NULL,
                        teacher_date INTEGER,
                        teacher_number INTEGER NOT NULL,
                        teacher_email TEXT NOT NULL
            )
            ''')

            # Таблица учебных групп
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS StudyGroup (
                        group_id INTEGER PRIMARY KEY,
                        group_name TEXT NOT NULL,
                        group_specialization INTEGER,
                        group_teacher INTEGER,
                        FOREIGN KEY(group_specialization) REFERENCES Specialization(specialization_id),
                        FOREIGN KEY(group_teacher) REFERENCES Teacher(teacher_id)
            )
            ''')

            # Таблица студентов
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                        student_id INTEGER PRIMARY KEY,
                        student_name TEXT NOT NULL,
                        student_date TEXT NOT NULL,
                        student_group INTEGER NOT NULL,
                        student_number INTEGER NOT NULL,
                        student_email TEXT,
                        student_passport TEXT NOT NULL,
                        student_snils TEXT NOT NULL,
                        student_inn TEXT NOT NULL,
                        student_gto INTEGER,
                        student_motherName TEXT,
                        student_motherNumber INTEGER,
                        student_motherEmail TEXT,
                        student_fatherName TEXT,
                        student_fatherNumber INTEGER,
                        student_fatherEmail TEXT,
                        FOREIGN KEY(student_group) REFERENCES StudyGroup(group_id)
            )
            ''')

            connection.commit()
            connection.close()
            print('✅ База данных students.db инициализирована')
        except Exception:
            print('⚠️ Ошибка: ', Exception)
            connection.close()

class dbConnection():
    dbConnect = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    dbConnect.setDatabaseName('students.db')
    try:
        dbConnect.open()
    except:
        print('⚠️ Неопределенная ошибка Ошибка!')