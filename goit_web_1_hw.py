from datetime import datetime, timedelta

class Birthday:
    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

    def is_within_week(self):
        today = datetime.now()
        birthday_date = datetime(today.year, self.month, self.day)
        next_week = today + timedelta(days=7)
        return today <= birthday_date <= next_week

class UserInterface:
    def show_message(self, message):
        raise NotImplementedError("Subclasses must implement show_message method.")

    def show_contacts(self, contacts):
        raise NotImplementedError("Subclasses must implement show_contacts method.")

    def show_commands_info(self):
        raise NotImplementedError("Subclasses must implement show_commands_info method.")

class ConsoleUserInterface(UserInterface):
    def show_message(self, message):
        print(message)

    def show_contacts(self, contacts):
        if contacts:
            print("Contacts:")
            for username, phone in contacts.items():
                print(f"Username: {username}, Phone: {phone}")
        else:
            print("No contacts available.")

    def show_commands_info(self):
        print("Available commands:")
        print("add <username> <phone>: Add a new contact.")
        print("change <username> <new_phone>: Change phone number of an existing contact.")
        print("phone <username>: Get phone number of a contact.")
        print("all: Show all contacts.")
        print("add-birthday <username> <day> <month> <year>: Add birthday for a contact.")
        print("show-birthday <username>: Show birthday of a contact.")
        print("birthdays: Show upcoming birthdays within the next week.")
        print("exit: Close the program.")

def parse_input(user_input):
    parts = user_input.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def add_contact(username, phone, contacts):
    contacts[username] = phone
    return f"Contact {username} added."

def change_contact(username, new_phone, contacts):
    if username in contacts:
        contacts[username] = new_phone
        return f"Phone number for {username} changed."
    else:
        return f"Contact {username} not found."

def add_birthday(username, birthday, birthdays):
    birthdays[username] = birthday
    return f"Birthday added for {username}."

def show_birthday(username, birthdays):
    if username in birthdays:
        return f"The birthday for {username} is {birthdays[username]}."
    else:
        return f"No birthday found for {username}."

def get_phone(username, contacts):
    if username in contacts:
        return f"The phone number for {username} is {contacts[username]}."
    else:
        return f"Contact {username} not found."

def show_all_contacts(contacts):
    if contacts:
        return "\n".join([f"{username}: {phone}" for username, phone in contacts.items()])
    else:
        return "No contacts available."

def main():
    contacts = {}
    birthdays = {}
    user_interface = ConsoleUserInterface()
    user_interface.show_message("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            user_interface.show_message("Good bye!")
            break
        elif command == "hello":
            user_interface.show_message("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                user_interface.show_message(add_contact(args[0], args[1], contacts))
            else:
                user_interface.show_message("Invalid command. Usage: add <username> <phone>")
        elif command == "change":
            if len(args) == 2:
                user_interface.show_message(change_contact(args[0], args[1], contacts))
            else:
                user_interface.show_message("Invalid command. Usage: change <username> <new_phone>")
        elif command == "phone":
            if len(args) == 1:
                user_interface.show_message(get_phone(args[0], contacts))
            else:
                user_interface.show_message("Invalid command. Usage: phone <username>")
        elif command == "all":
            user_interface.show_contacts(contacts)
        elif command == "add-birthday":
            if len(args) == 3:
                user_interface.show_message(add_birthday(args[0], Birthday(*args[1:]), birthdays))
            else:
                user_interface.show_message("Invalid command. Usage: add-birthday <username> <day> <month> <year>")
        elif command == "show-birthday":
            if len(args) == 1:
                user_interface.show_message(show_birthday(args[0], birthdays))
            else:
                user_interface.show_message("Invalid command. Usage: show-birthday <username>")
        elif command == "birthdays":
            today = datetime.now()
            upcoming_birthdays = [username for username, birthday in birthdays.items() if birthday.is_within_week()]
            if upcoming_birthdays:
                user_interface.show_message("Upcoming birthdays:")
                for username in upcoming_birthdays:
                    user_interface.show_message(f"{username}: {birthdays[username]}")
            else:
                user_interface.show_message("No upcoming birthdays within the next week.")
        elif command == "help":
            user_interface.show_commands_info()
        else:
            user_interface.show_message("Invalid command.")

if __name__ == "__main__":
    main()

