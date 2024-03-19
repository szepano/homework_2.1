import classes
import class_addressbook
import sorter


def main():
    """
    The main() function is responsible for managing user interaction with the phone book.
    Users can perform vEnd the prarious operations on entries in the phone book, such as adding,
    editing, removing, searching, and displaying entries, and calculating the number of 
    days to birthdays. The phonebook can be saved as well as loaded after restarting the 
    program.

    Commands:
    - 'help' - Shows available commands with explanations
    - '.' - Close program.
    - 'good bye', 'close', 'exit' - Terminate the program with the message "Good bye!".
    - 'hello' - Display a greeting.
    - 'add' - Add a new entry to the address book.
    - 'remove contact' - Removes whole existing record in address book.
    - 'add phone' - Add a new phone number to an existing entry.
    - 'edit phone' - Edit an existing phone number.
    - 'remove phone' - Remove a phone number from an existing entry.
    - 'add address' - Adding address to an existing entry.
    - 'edit address' - Editing address of an existing entry.
    - 'remove address' - Removing address of an existing entry.
    - 'add birthday' - Add a birthday to an existing entry.
    - 'edit birthday' - Changes EXISTING birthday in entry.
    - 'remove birthday' - Remove the birthday from an existing entry.
    - 'add email' - Add an email address to en existing entry.
    - 'edit email' - Edit email of an existing entry
    - 'clean' - sorts files in chosen folder by file type.
    - 'find' - Search for entries in the address book.
    - 'days to birthday' - Calculate the number of days until the next birthday.
    - 'upcoming birthdays' - Displays a list of contacts whose birthdays are a specified number of days from the current date;
    - 'show all' - Display all entries in the address book.
    - 'save' - Save the address book to a file.
    - 'load address book' - Load the address book from a file.
    """
    address_book = class_addressbook.AddressBook()
    console = classes.ConsoleUserInteraction()
    while True:
        command = input("Enter command: ").lower()

        if '.' in command:
            break

        elif command in ['good bye', 'close', 'exit']:
            print("Good bye!")
            break

        elif command == 'help':
            console.display_commands()

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            address_book.add_record()

        elif command == "add phone":
            address_book.add_phone()

        elif command == 'add email':
            address_book.add_email()

        elif command == 'add address':
            address_book.add_address()
            
        elif command == "edit address":
            address_book.add_address()

        elif command == "remove address":
            address_book.remove_address()

        elif command == "edit phone":
            address_book.edit_phone()

        elif command == "edit email":
            address_book.add_email()

        elif command == 'remove contact':
            address_book.remove_contact()
            
        elif command == "find":
            address_book.find_partial_records()

        elif command == "add birthday":
            address_book.add_birthday()
            
        elif command == "edit birthday":
            address_book.edit_birthday()

        elif command == "remove birthday":
            address_book.remove_birthday()

        elif command == "clean":
            path = input("Enter Path to folder:")
            cleanfolder = sorter.CleanFolder(path)
            try:
                cleanfolder.process_folder()
            except TypeError:
                print("Error: Chosen path is incorrect.")

        elif command == "days to birthday":
            address_book.days_to_birthday()


        elif command == "upcoming birthdays":
            address_book.upcoming_birthdays()

        elif command == "show all":
            console.display_contacts(address_book)
            # if address_book:
            #     print("Success: All Contacts:")
            #     N = 5
            #     records = list(address_book.data.values())
            #     for i in range(0, len(records), N):
            #         for record in records[i:i+N]:
            #             print(record)
            #         if i + N < len(records):
            #             input("Press enter to see the next page...\n")
            #     print()
            # else:
            #     print("Error: Address book is empty.\n")


        elif command == "save":
            filename = input("Enter the filename to save the address book: ")
            address_book.save_to_file(filename)
            print(f"Success: Address book saved to {filename}.\n")


        elif command == "load address book":
            filename = input("Enter the filename to load the address book from: ")
            try:
                address_book = class_addressbook.AddressBook.load_from_file(filename)
                print(f"Success: Address book loaded from {filename}.\n")
            except FileNotFoundError:
                print(f"Error: File {filename} not found.\n")


        else:
            print("Error: Invalid command. Enter the correct command.\n")

if __name__ == "__main__":
    main()