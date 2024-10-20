import sys
def greeting():
    print("How can I help you?")
def farewell():
    print("Good bye!")
    sys.exit(0)
#getting the command and the arguments from the user
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
#converting our dictionary to a string
def get_all_contacts(contacts: dict) -> str:
    if not contacts:
        print('No contacts found')
    else:
        print("\n".join([f"{name}: {phone}" for name, phone in contacts.items()]))
#checking if the key exists in our dic, returning the value
def get_phone(*args, contacts: dict) -> str:
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            print(contacts[name])
        else:
            print("There is no contact with such name")
    else:
        print('Wrong syntax: phone *username*')

    
#changing the value of the existing item in the dictionary
def change_contact(*args, contacts: dict) -> str:
    if len(args) == 2:
        if args[0] in contacts:
            name, phone = args
            contacts[name] = phone
            print("Contact changed.")
        else:
            print("There is no contact with such name.")
    else:
        print("Wrong syntax: change *username* *phone*")   
    


def add_contact(*args, contacts: dict):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        print("Contact added.")
    else:
        print("Invalid input. Usage: add username phone")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:

        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        #our only condition to exit
        if command in ["close", "exit"]:
            farewell()
        elif command == "hello":
            greeting()
        elif command == "add":
            add_contact(*args, contacts=contacts)
        elif command == "change":
            change_contact(*args, contacts=contacts)
        elif command == "phone":
            get_phone(*args, contacts=contacts)
        elif command == "all":
            get_all_contacts(contacts=contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
