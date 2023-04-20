from application.salary import calculate_salary
from application.db.people import  get_employees
import datetime

if __name__ == '__main__':
    get_employees(name='Иван')
    calculate_salary(wage=2)
    print(f'Текущая дата: {datetime.date.today()}')