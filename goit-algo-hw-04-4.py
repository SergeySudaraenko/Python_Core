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


def get_phone(username, contacts):
    if username in contacts:
        return f"The phone number for {username} is {contacts[username]}."
    else:
        return f"Contact {username} not found."


def show_all_contacts(contacts):
    if contacts:
        return "\n".join(
            [f"{username}: {phone}" for username, phone in contacts.items()]
        )
    else:
        return "No contacts available."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                print(add_contact(args[0], args[1], contacts))
            else:
                print("Invalid command. Usage: add <username> <phone>")
        elif command == "change":
            if len(args) == 2:
                print(change_contact(args[0], args[1], contacts))
            else:
                print("Invalid command. Usage: change <username> <new_phone>")
        elif command == "phone":
            if len(args) == 1:
                print(get_phone(args[0], contacts))
            else:
                print("Invalid command. Usage: phone <username>")
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
