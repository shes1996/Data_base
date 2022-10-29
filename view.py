import sqlite3


def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('data_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT id_of_human, name, address, date_of_birth, department, title, salary 
        from employees, department, title WHERE employees.department_of_human=department.id_department AND 
        employees.title_of_human=title.id_title"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print("ID:", row[0])
            print("name:", row[1])
            print("address:", row[2])
            print("date_of_birth:", row[3])
            print("department:", row[4])
            print("title:", row[5])
            print("salary:", row[6], end="\n\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


#read_sqlite_table()
