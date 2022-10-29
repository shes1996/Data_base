import view
import filter
import change


def actions():
    print({'1': 'Вывести всех сотрудников', '2': 'Отфильтровать по лаборатории'})
    print({'3': 'Отфильтровать по должности', '4': 'Уволить сотрудника'})
    print({'5': 'Нанять сотрудника', '6': 'Перевести сотрудника в другую лабораторию'})
    print({'7': 'Перевести сотрудника на другую должность'})


    action = input('Выберите действие, которое необходимо выполнить'
                   'с базой данных сотрудников института: ')

    match action:
                case "1":
                    view.read_sqlite_table()
                case "2":
                    filter.filter_department_sqlite_table()
                case "3":
                    filter.filter_title_sqlite_table()
                case "4":
                    change.delete_sqlite_table()
                case "5":
                    change.add_sqlite_table()
                case "6":
                    change.employee_transfer_sqlite_table()
                case "7":
                    change.employee_title_sqlite_table()
                case _:
                    print("department not found")
