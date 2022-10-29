import sqlite3


def delete_sqlite_table():
    try:
        name = input('Какого сотрудника вы хотите уволить? ')
        sqlite_connection = sqlite3.connect("data_base.db")
        c = sqlite_connection.cursor()
        print("Подключен к SQLite")
        c.execute('DELETE FROM employees WHERE name = (?)', (name,))
        sqlite_connection.commit()
        sqlite_connection.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

#delete_sqlite_table()

def employee_transfer_sqlite_table():
    try:
        id_of_human = input('Какого сотрудника Вы хотите перевести?(введите ID) ')
        department = {'1': 'lab_100', '2': 'lab_101', '3': 'lab_102'}
        print(department)
        department_select = input('Выберите лабораторию? ')
        sqlite_connection = sqlite3.connect('data_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = ("""UPDATE employees set department_of_human = '{}' where id_of_human = '{}'""".format(department_select, id_of_human))
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


#employee_transfer_sqlite_table()


def employee_title_sqlite_table():
    try:
        id_of_human = input('Какому сотруднику Вы хотите изменить должность?(введите ID) ')
        print({'1': 'engineer', '2': 'senior_researcher', '3': 'junior_researcher', '4': 'head_of_laboratory'})
        title_select = input('Выберите должность: ')
        sqlite_connection = sqlite3.connect('data_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = ("""UPDATE employees set title_of_human = '{}' where id_of_human = '{}'""".format(title_select, id_of_human))
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


#employee_title_sqlite_table()


def add_sqlite_table():
    try:
        name = input('Введите данные сотрудника: Имя Фамилия: ')
        address = input('адрес: ')
        date_of_birth = input('дата рождения(гггг-мм-дд): ')
        print({'1': 'lab_100', '2': 'lab_101', '3': 'lab_102'})
        department_select = input('Выберите лабораторию: ')
        print({'1': 'engineer', '2': 'senior_researcher', '3': 'junior_researcher', '4': 'head_of_laboratory'})
        title_select = input('Выберите должность: ')
        sqlite_connection = sqlite3.connect('data_base.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        if title_select in ['1', '2', '3'] and department_select in ['1', '2', '3', '4']:
            print("Title not found")
            sqlite_insert_query = f"""INSERT INTO employees
                          (id_of_human, name, address, date_of_birth, department_of_human, title_of_human)
                          VALUES
                          (NULL, '{name}', '{address}', '{date_of_birth}', 
                          '{department_select}', '{title_select}')"""
        else:
            print("Title  or department not found")

        cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print("Запись успешно вставлена в таблицу employees ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


#add_sqlite_table()
