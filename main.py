from datetime import datetime
from application import salary
from application.db import people

if __name__ == '__main__':
    salary.calculate_salary()
    print(datetime.now())
    people.get_employees()
    print(datetime.now())
