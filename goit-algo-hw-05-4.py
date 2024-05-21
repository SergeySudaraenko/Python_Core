def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError as e:
            return f"Contact {str(e)} not found."
        except IndexError:
            return "Invalid command. Usage: <command> <arguments>"

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} changed."
    else:
        raise KeyError(name)


@input_error
def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}."
    else:
        raise KeyError(name)


@input_error
def show_all_contacts(args, contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts available."


def parse_input(user_input):
    parts = user_input.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args


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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
