# Парсер вакансии из 10 заранее выбранных компаний с HH.ru

1. Код собирает вакансии из 10 заранее выбранных компаний, сохраняет список вакансий в таблицы БД. 
- Список компаний прописан в коде main.py -> employees
- Данные с сайта собираются через публичный API hh.ru и библиотеку requests
- ***Обязательно*** перед тем как начать работу с кодом в PostgreSQL создать пустую БД "hh"
- Для работы с БД используется библиотека psycopg2

2. Создан класс DBManager для работы с данными в БД, который подключается к БД PostgreSQL и имеет следующие методы:
- **get_companies_and_vacancies_count()** — получает список всех компаний и количество вакансий у каждой компании.
- **get_all_vacancies()** — получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
- **get_avg_salary()** — получает среднюю зарплату по вакансиям.
- **get_vacancies_with_higher_salary()** — получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
- **get_vacancies_with_keyword()** — получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.

3. Запуск кода из файла ***main.py***
   
