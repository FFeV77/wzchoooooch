from applications.db.people import get_employees
from applications.salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    today = datetime.today()
    print(today)
    
    get_employees()
    calculate_salary()

