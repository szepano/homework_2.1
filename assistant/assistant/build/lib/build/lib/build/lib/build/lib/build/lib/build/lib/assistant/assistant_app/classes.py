import re
from datetime import datetime
from abc import abstractmethod
import class_addressbook

class Commands:
    def __repr__(self):
        return str('''Commands:
        - 'help' - shows available commands with explanations
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
        - 'load address book' - Load the address book from a file.''')

class UserInterface:
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    def display_commands(self, commands):
        pass

    # @abstractmethod
    # def display_notes(self, notes):
    #     pass

class ConsoleUserInteraction(UserInterface):
    def display_contacts(self, address_book):
        print(address_book)
    
    def display_commands(self):
        print(Commands())



class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        normalized_phone = ''.join(filter(str.isdigit, str(phone)))
        if len(normalized_phone) == 9:
            self.phone = normalized_phone
        else:
            raise ValueError("Phone number must contain exactly 9 digits.")
        super().__init__(phone)

    def __str__(self):
        return f'{self.phone}'
    
    def __repr__(self):
        return f'{self.phone}'


class Birthday(Field):
    def __init__(self, birthday=None):
        if birthday is not None:
            try:
                birthday = datetime.strptime(birthday, "%d-%m-%Y")
            except ValueError:
                raise ValueError("Birthday must be in 'dd-mm-yyyy' format.")
        super().__init__(birthday)


class Address(Field):
    def __init__(self, value=None):
        self.value = value


class Email(Field):
    def __init__(self, email):
        if email is not None:
            check = re.findall(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email)
            if len(check) == 1:
                self.value = email
            else:
                raise ValueError('dupa')
        else:
            self.value = None


class Tag(Field):
    def __init__(self, value=None):
        self.value = value


class Note(Field):
    def __init__(self, value=None):
        self.value = value


class Record:
    def __init__(self, name, phone=[], birthday=None, address=None, email=None):
        self.name = Name(name)
        self.birthday = Birthday(birthday)
        self.phones = []
        self.address = address
        self.email = email

    def remove_phone(self, phone):
        phone_to_remove = str(phone)
        if phone_to_remove in [str(p) for p in self.phones]:
            self.phones = [p for p in self.phones if str(p) != phone_to_remove]

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def remove_birthday(self):
        self.birthday = Birthday()

    def add_address(self, address):
        self.address = Address(address)

    def edit_address(self, new_address):
        self.address = Address(new_address)



    def add_email(self, email):
        self.email = Email(email)


    def edit_note(self, tag, new_note):
        if tag in self.note:
            self.note[tag] = new_note

    def __str__(self):
        try:
            return f"Name: {self.name}, Phones: {', '.join(map(str, self.phones))}, Birthday: {self.birthday.value.date()}, Email: {self.email}, Address: {self.address}"
        except AttributeError:
            return f"Name: {self.name}, Phones: {', '.join(map(str, self.phones))}, Birthday: {self.birthday}, Email: {self.email}, Address: {self.address}"