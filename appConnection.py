import sqlite3, os.path, csv
from PyQt5 import QtSql

def dbCreate():
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
                    student_snils TEXT,
                    student_inn TEXT,
                    student_gto TEXT,
                    student_motherName TEXT,
                    student_motherNumber INTEGER,
                    student_motherEmail TEXT,
                    student_fatherName TEXT,
                    student_fatherNumber INTEGER,
                    student_fatherEmail TEXT,
                    FOREIGN KEY(student_group) REFERENCES StudyGroup(group_id)
        )
        ''')

        record_User =[('user', 'user'),
                    ('admin', 'admin'),]

        record_Specialization = [('Информационные системы и программирование',),
                                ('Безопасность компьютерных сетей',)]
        
        record_Teacher =[('Иванов Иван Иванович','01.01.1990','79123456789','ivanov@mail.com'),
                        ('Петров Петр Петрович','02.02.1991','78123456789','petrov@mail.com'),
                        ('Сидоров Сидор Сидорович','03.03.1993','77123456789','sidorov@mail.com'),
                        ('Николаев Николай Николаевич','04.04.1994','76123456789','nikolaev@mail.com'),
                        ('Смирнов Сергей Сергеевич','05.05.1995','75123456789','smirnov@mail.com'),
                        ('Кузнецов Кузьма Кузьмич','06.06.1996','74123456789','kuznetsov@mail.com'),
                        ('Соколов Семён Семёнович','07.07.1997','73123456789','sokolov@mail.com'),
                        ('Лебедев Лев Львович','08.08.1998','72123456789','lebedev@mail.com'),
                        ('Волков Владимир Владимирович','09.09.1999','71123456789','volkov@mail.com'),
                        ('Дмитриев Дмитрий Дмитриевич','02.02.1992','79123456789','dmitriev@mail.com'),]

        record_StudyGroup = [('СИП-113/23', '1', '1'),
                            ('СИП-123/23', '1', '2'),
                            ('СИП-133/23', '1', '3'),
                            ('СИП-143/23', '1', '4'),
                            ('СИП-213/22', '1', '5'),
                            ('СИП-223/22', '1', '6'),
                            ('СОБ-113/23', '2', '7'),
                            ('СОБ-213/22', '2', '8'),
                            ('СОБ-223/22', '2', '9'),
                            ('СОБ-123/23', '2', '10'),]

        record_Student = [('Никита Буянов', '24.01.2005', '1', '88005553535', 'bruh@mail.ru', '1234 567890', '123-456-789 00', '123456789012', '12-34-567890', 'Мамина М.М.', '880012345678', 'bruh@mail.ru', 'Папин П.П.', '880012345678', 'bruh@mail.ru'),
                          ('Алексей Буянов', '24.01.2005', '1', '88005553535', 'bruh@mail.ru', '1234 567890', '123-456-789 00', '123456789012', '12-34-567890', 'Мамина М.М.', '880012345678', 'bruh@mail.ru', 'Папин П.П.', '880012345678', 'bruh@mail.ru'),
                          ('Федор Буянов', '24.01.2005', '1', '88005553535', 'bruh@mail.ru', '1234 567890', '123-456-789 00', '123456789012', '12-34-567890', 'Мамина М.М.', '880012345678', 'bruh@mail.ru', 'Папин П.П.', '880012345678', 'bruh@mail.ru'),
                          ('Антон Буянов', '24.01.2005', '1', '88005553535', 'bruh@mail.ru', '1234 567890', '123-456-789 00', '123456789012', '12-34-567890', 'Мамина М.М.', '880012345678', 'bruh@mail.ru', 'Папин П.П.', '880012345678', 'bruh@mail.ru'),
                          ('Станислав Буянов', '24.01.2005', '1', '88005553535', 'bruh@mail.ru', '1234 567890', '123-456-789 00', '123456789012', '12-34-567890', 'Мамина М.М.', '880012345678', 'bruh@mail.ru', 'Папин П.П.', '880012345678', 'bruh@mail.ru'),
                          ('Илья Буянов', '24.01.2005', '1', '88005553535', 'bruh@mail.ru', '1234 567890', '123-456-789 00', '123456789012', '12-34-567890', 'Мамина М.М.', '880012345678', 'bruh@mail.ru', 'Папин П.П.', '880012345678', 'bruh@mail.ru'),
                          ('Кирилл Буянов', '24.01.2005', '1', '88005553535', 'bruh@mail.ru', '1234 567890', '123-456-789 00', '123456789012', '12-34-567890', 'Мамина М.М.', '880012345678', 'bruh@mail.ru', 'Папин П.П.', '880012345678', 'bruh@mail.ru'),
                          ('Макс Буянов', '24.01.2005', '1', '88005553535', 'bruh@mail.ru', '1234 567890', '123-456-789 00', '123456789012', '12-34-567890', 'Мамина М.М.', '880012345678', 'bruh@mail.ru', 'Папин П.П.', '880012345678', 'bruh@mail.ru'),
                          ('Николай Буянов', '24.01.2005', '1', '88005553535', 'bruh@mail.ru', '1234 567890', '123-456-789 00', '123456789012', '12-34-567890', 'Мамина М.М.', '880012345678', 'bruh@mail.ru', 'Папин П.П.', '880012345678', 'bruh@mail.ru'),
                          ('Вадим Буянов', '24.01.2005', '1', '88005553535', 'bruh@mail.ru', '1234 567890', '123-456-789 00', '123456789012', '12-34-567890', 'Мамина М.М.', '880012345678', 'bruh@mail.ru', 'Папин П.П.', '880012345678', 'bruh@mail.ru')]

        cursor.executemany('''INSERT INTO User
                        (user_login, user_password)
                        VALUES (?, ?)''', record_User)
        
        cursor.executemany('''INSERT INTO Specialization
                        (specialization_name)
                        VALUES (?)''', record_Specialization)
        
        cursor.executemany('''INSERT INTO Teacher
                        (teacher_name, teacher_date, teacher_number, teacher_email)
                        VALUES (?, ?, ?, ?)''', record_Teacher)
        
        cursor.executemany('''INSERT INTO StudyGroup
                        (group_name, group_specialization, group_teacher)
                        VALUES (?, ?, ?)''', record_StudyGroup)
        
        cursor.executemany('''INSERT INTO Students
                           (student_name, student_date, student_group, student_number,
                           student_email, student_passport, student_snils, student_inn,
                           student_gto, student_motherName, student_motherNumber,
                           student_motherEmail, student_fatherName, student_fatherNumber,
                           student_fatherEmail)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', record_Student)

        connection.commit()
        connection.close()
        print('✅ База данных students.db инициализирована')
    except ValueError:
        print('⚠️ Ошибка: ', Exception)
        connection.close()

def dbConnection():
    dbConnect = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    dbConnect.setDatabaseName('students.db')
    try:
        dbConnect.open()
    except:
        print('⚠️ Неопределенная ошибка Ошибка!')

class dbRequest():
    def expStudents():
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("select * from Students;")
        with open("students.csv", 'w',newline='') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description]) 
            csv_writer.writerows(cursor)
        conn.close()

    def expUsers():
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("select * from User;")
        with open("user.csv", 'w',newline='') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description]) 
            csv_writer.writerows(cursor)
        conn.close()

    def expStudyGroup():
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("select * from StudyGroup;")
        with open("studyGroup.csv", 'w',newline='') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description]) 
            csv_writer.writerows(cursor)
        conn.close()
    
    def expTeachers():
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("select * from Teacher;")
        with open("teacher.csv", 'w',newline='') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description]) 
            csv_writer.writerows(cursor)
        conn.close()