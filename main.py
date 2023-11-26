from utils import get_vacancies_in_table, refresh_tables, create_table
from dbmanager import DBManager

"""Создаем таблицу в БД если не было ИЛИ обнуляем и вносим свежие данные"""
create_table()
refresh_tables()
employees = [
    665467, 78638, 41862, 1504670, 6093775,
    389, 4934, 3144945, 42600, 234492
           ]

for employee in employees:
    get_vacancies_in_table(employee)
data = DBManager()

main_exit = True  # ключи для более наглядного завершения программы
menu_exit = True

"""Start взаимодействия с пользователем"""
print('Здравствуйте')

while main_exit is True:
    while menu_exit is True:
        print('____________________________________________________________________')
        print('Выберите пункт меню: ')
        print('1 - показать список компаний и кол-во вакансий относящихся к ним')
        print('2 - показать список всех вакансий')
        print('3 - показать среднею зарплату по имеющимся вакансиям')
        print('4 - показать список всех вакансий у которых зарплата выше средней')
        print('5 - найти вакансию по названию')
        print('0 - для выхода из программы')
        print('____________________________________________________________________')

        option_menu = input()
        if option_menu not in ['1', '2', '3', '4', '5', '0']:
            print('Некорректный вариант действий, выберете корректный!')
            continue

        if option_menu == '1':
            data.get_companies_and_vacancies_count()

        if option_menu == '2':
            data.get_all_vacancies()

        if option_menu == '3':
            print(f'Средняя зарплата: {data.get_avg_salary()}')

        if option_menu == '4':
            data.get_vacancies_with_higher_salary()

        if option_menu == '5':
            print('Введите название:')
            vacancie_name = input()
            data.get_vacancies_with_keyword(vacancie_name)

        if option_menu == '0':
            print('Очень жаль, что Вы уходите... До новых встреч!')
            main_exit = False
            menu_exit = False
