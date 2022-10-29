import sqlite3


def filter_title_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('data_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        title = {'1': 'engineer', '2': 'senior_researcher', '3': 'junior_researcher', '4': 'head_of_laboratory'}
        print(title)
        title_select = input('Выберите должность, по которой необходимо отсортировать сотрудников: ')
        match title_select:
            case "1":
                title_select = 'engineer'
            case "2":
                title_select = "senior_researcher"
            case "3":
                title_select = "junior_researcher"
            case "4":
                title_select = "head_of_laboratory"
            case _:
                print("Title not found")

        sqlite_select_query = f"""SELECT id_of_human, name, address, date_of_birth, department, title, salary 
        from employees, department, title WHERE employees.department_of_human=department.id_department AND 
        employees.title_of_human=title.id_title AND title.title='{title_select}'"""

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

#filter_title_sqlite_table()

def filter_department_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('data_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        department = {'1': 'lab_100', '2': 'lab_101', '3': 'lab_102'}
        print(department)
        department_select = input('Выберите лабораторию, по которой необходимо отсортировать сотрудников: ')
        match department_select:
            case "1":
                department_select = 'lab_100'
            case "2":
                department_select = "lab_101"
            case "3":
                department_select = "lab_102"
            case _:
                print("department not found")

        sqlite_select_query = f"""SELECT id_of_human, name, address, date_of_birth, department, title, salary 
        from employees, department, title WHERE employees.department_of_human=department.id_department AND 
        employees.title_of_human=title.id_title AND department.department='{department_select}'"""

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

#filter_department_sqlite_table()