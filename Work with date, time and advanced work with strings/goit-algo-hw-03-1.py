from datetime import datetime


def get_days_from_today(date):
    date_object = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.today()
    days_difference = (current_date - date_object).days
    return days_difference


date_string = "2020-10-09"
result = get_days_from_today(date_string)
print(f"Різниця у днях: {result}")
