from datetime import datetime

def get_days_from_today(date):
    try:
        date_object = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        days_difference = (date_object - current_date).days

        return days_difference
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."
date_input = '2020-10-09'
result = get_days_from_today(date_input)

print(f"Різниця в днях між {date_input} і сьогодні: {result}")