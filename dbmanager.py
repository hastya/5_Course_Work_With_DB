from abc import abstractmethod
import psycopg2


class DBManager():

    @abstractmethod
    def connection(self, rules:str):
        """Подключение к БД"""
        with psycopg2.connect(
                host="localhost",
                database="hh",
                user="postgres",
                password="sql") as conn:
            with conn.cursor() as cur:
                cur.execute(rules)
                records = cur.fetchall()
            return records

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        req = ('SELECT emp_name, COUNT(*) as total_vacancies '
               'FROM vacancies LEFT JOIN employeers USING(id_emp) '
               'GROUP BY emp_name '
               'ORDER BY total_vacancies DESC, emp_name')
        data = self.connection(req)
        for i in data:
            print(f'Название комании: {i[0]} \n Кол-во вакансий: {i[1]}')
            print('__________________________________________________')

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
        req = ('SELECT employeers.emp_name, vac_name, salary, link_vac '
               'FROM vacancies INNER JOIN employeers USING(id_emp) '
               'GROUP BY salary, link_vac, employeers.emp_name, vac_name '
               'ORDER BY employeers.emp_name, salary DESC')
        data = self.connection(req)
        for i in data:
            print(f' Название комании: {i[0]} \n Название вакансии: {i[1]} \n Зарплата: {i[2]} \n Ссылка на вакансию: {i[3]}')
            print('____________________________________________________________________')

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        req = ('SELECT ROUND(AVG(salary)) as avg_salary '
               'FROM vacancies '
               'WHERE salary > 0')
        data = self.connection(req)
        x = str(data[0])
        salary = int(''.join(filter(str.isdigit, x)))
        return salary

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям"""
        req = ('SELECT vac_name, salary, link_vac '
               'FROM vacancies '
               'WHERE salary > (SELECT AVG(salary) '
               '                FROM vacancies '
               '                WHERE salary > 0) '
               'ORDER BY salary DESC, vac_name')
        data = self.connection(req)
        for i in data:
            print(f' Название вакансии: {i[0]} \n Зарплата: {i[1]} \n Ссылка на вакансию: {i[2]}')
            print('____________________________________________________________________')

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова,
        например python"""
        req = (f"SELECT * "
               f"FROM vacancies "
               f"WHERE vac_name ILIKE '%{keyword}%' "
               f"ORDER BY salary DESC")
        data = self.connection(req)
        if data == []:
            print('Такой вакансии нет')
        else:
            for i in data:
                print(f' Название вакансии: {i[1]} \n Зарплата: {i[2]} \n Ссылка на вакансию: {i[4]}')
                print('____________________________________________________________________')
