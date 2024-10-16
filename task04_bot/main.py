import sys

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def get_all_contacts(contacts: dict) -> str:
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

def get_phone(name, contacts: dict) -> str:
    if name in contacts:
        return contacts[name]
    else:
        return ("There is no contact with such name")

def change_contact(args, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

def add_contact(args, contacts: dict) -> str:
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid input. Usage: add username phone"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            sys.exit(0)
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                print(add_contact(args, contacts))
            else:
                print('Wrong syntax: add *username* *phone*')        
        elif command == "change":
            if len(args) == 2:
                if args[0] in contacts:
                    print(change_contact(args, contacts))
                else:
                    print("There is no contact with such name.")
            else:
                print("Wrong syntax: change *username* *phone*")     
        elif command == "phone":
            if len(args) == 1:
                print(get_phone(args[0], contacts))
            else:
                print('Wrong syntax: phone *username*')
        elif command == "all":
            if len(args) > 0:
                print('Wrong syntax: all')
            elif not contacts:
                print('No contacts found')
            else:
                print(get_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
