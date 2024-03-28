from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
           
            if birthday_this_year.weekday() >= 5:
            
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users_list = [
    {"name": "John", "birthday": "1990.02.15"},
    {"name": "Alice", "birthday": "1985.09.30"},
    {"name": "Bob", "birthday": "1995.11.22"}
]

result = get_upcoming_birthdays(users_list)
print(result)