
from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте YYYY-MM-DD"
print (get_days_from_today("2025-05-28"))
