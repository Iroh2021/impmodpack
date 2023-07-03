from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
from snake.snake import *

current_date = datetime.date.today()

if __name__ == '__main__':
    print(get_employees(), calculate_salary())
    print("Текущая дата:", current_date)
    gameLoop()