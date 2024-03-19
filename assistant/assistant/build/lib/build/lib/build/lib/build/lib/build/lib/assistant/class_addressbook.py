from . import classes
import datetime
from collections import UserDict
import os
import shutil
import pickle

class AddressBook(UserDict):
    def add_record(self):
        name = input("Enter name: ")
        if not name.strip():
            print("Error: Name cannot be empty.\n")
            

        existing_records = self.find_records(name)
        if existing_records:
            print(f"Error: Record: {name} already exists in the address book. Please choose a different name.\n")
            

        else:
            record = classes.Record(name)                
            phone = input("Enter phone number: ")
            phone_str = ''
            if phone.strip():
                try:
                    phone = classes.Phone(phone)
                    record.phones.append(phone)
                    phone_str = phone
                except ValueError as e:
                    print(f"Incorrect phone number: {e}")

            birthday = input("Enter birthday (dd-mm-yyyy): ")
            birthday_str = ''
            if not birthday.strip():
                record.birthday = None    
            if birthday.strip():
                try:
                    record.add_birthday(birthday)
                except ValueError:
                    print('chuja tam')
                birthday_str = birthday
                

            email = input("If you don't want to add email address just press enter. \nEnter email (example@dummy.com):")
            email_str = ''
            if email.strip():
                try:
                    record.add_email(email)
                    email_str = email
                except ValueError:
                    print('Invalid email address')

            address = input('Enter address: ')
            if address.strip():
                try:
                    record.add_address(address)
                except ValueError:
                    print('Failure during adding an address')

        self.data[record.name.value] = record
        print(f"Success: Record: \n Name: {name} \n Numbers: {phone_str}\n Birthday: {record.birthday}\n Email: {record.email}\n Address: {record.address}\n")
        
    def add_phone(self):
        while True:
            name = input('Enter name: ')
            if not name.strip():
                print('Name cannot be empty.')
                break
            existing_records = self.find_records(name)
            if not existing_records:
                print('No record found')
                continue
            record = existing_records[0]
            new_phone = input('Enter new phone: ')
            record.phones.append(new_phone)
            break

    def add_email(self):
        while True:
            name = input("Enter name: ")
            if not name.strip():
                print("Error: Name cannot be empty. Please enter a valid name.\n")
                break

            existing_records = self.find_records(name)
            if not existing_records:
                print(f"Error: This name: {name} does not exist in the address book. Please add a new record first.\n")
                continue
            else:
                email = input('Enter email address: ')
                if email.strip():
                    record = existing_records[0]
                    new_email = classes.Email(email)
                    record.email = new_email
                    print('done', record.name, ':', record.email)
                    break
    
    def add_address(self):
        while True:
            name = input("Enter name: ")
            if not name.strip():
                print("Error: Name cannot be empty. Please enter a valid name.\n")
                break

            existing_records = self.find_records(name)
            if not existing_records:
                print(f"Error: This name: {name} does not exist in the address book. Please add a new record first.\n")
                pass
            else:
                address = input('Enter address: ')
                if address.strip():
                    record = existing_records[0]
                    new_address = classes.Address(address)
                    record.address = new_address
                    print('done', record.name, ':', record.address)
                    break

    def remove_address(self):
        while True:
            name = input('Enter name: ')
            if not name.strip():
                print('Name cannot be empty.')
                break
            existing = self.find_records(name)
            if not existing:
                print('No record found.')
                pass
            record = existing[0]
            record.address = classes.Address()
            print('Done', record.name, 'address removed')
            break

    def edit_phone(self):
        while True:
            name = input('Enter name: ')
            if not name.strip():
                print('Name cannot be empty')
                break
            existing = self.find_records(name)
            if not existing:
                print('No record found')
                pass
            record = existing[0]
            print(f'Current {record.name} phones:')
            for i in record.phones:
                print(i)
            choice = input('Select phone to remove (by index starting from 1)')
            if not choice.strip():
                print('No number selected')
                break
            try:
                record.phones.pop(int(choice) - 1)
            except IndexError:
                print('Wrong index')
                pass
            print('Phone removed')
            number = input('Enter new phone: ')
            if not number.strip():
                print('No number added')
                break
            new_phone = classes.Phone(number)
            record.phones.append(new_phone)
            print('Phone changed succesfuly', record.phones)
            break

    def remove_contact(self):
        while True:
            name = input('Enter name to remove: ')
            if not name.strip():
                print('Name cannot be empty')
                break
            existing = self.find_records(name)
            if not existing:
                print(f'Record to {name} not found')
                pass
            record = existing[0]
            self.data.pop(record.name.value)
            break

    def add_birthday(self):
        while True:
            name = input('Enter name: ')
            if not name.strip():
                print('Name cannot be empty')
                break
            
            existing = self.find_records(name)
            if not existing:
                print(f'No record with {name} found')
                pass

            record = existing[0]
            if record.birthday == None:
                birthday = input('Enter date of birth (dd-mm-yyyy): ')
                record.add_birthday(birthday)
                break

    def edit_birthday(self):
        while True:
            name = input('Enter name: ')
            if not name.strip():
                print('Name cannot be empty')
                break
            
            existing = self.find_records(name)
            if not existing:
                print(f'No record with {name} found')
                pass

            record = existing[0]
            if record.birthday != None:
                print(f'Current birthday date: {record.birthday}')
                birthday = input('Press enter if you do not want to change birth date\nEnter new date of birth (dd-mm-yyyy): ')
                if not birthday:
                    print('Birthday not changed')
                    break
                record.add_birthday(birthday)
                print(f'Success, new birthday {record.birthday}')
                break
    
    def remove_birthday(self):
        while True:
            name = input('Enter name: ')
            if not name.strip():
                print('Name cannot be empty')
                break
            existing = self.find_records(name)
            if not existing:
                print('No record found')
                pass
            record = existing[0]
            record.birthday = None
            print('Success', record.birthday)
            break

    def find_records(self, keyword):
        results = []
        keyword_lower = keyword.lower()
        for record in self.data.values():
            if keyword_lower == record.name.value.lower():
                results.append(record)
            else:
                for phone in record.phones:
                    if keyword_lower == str(phone).lower():
                        results.append(record)
                        break  
        return results

    def find_partial_records(self):
        while True:
            search_char = input("Enter the character by which you want to search for users: ").strip().lower()
            if not search_char:
                print("Error: The character you searched for cannot be empty.")
                break

            results = []
            keyword_lower = search_char.lower()
            for record in self.data.values():
                if keyword_lower in record.name.value.lower() or any(keyword_lower in str(phone).lower() for phone in record.phones):
                    results.append(record)
            if results:
                print("Success: Records found:")
                N = 5
                for i in range(0, len(results), N):
                    for record in results[i:i+N]:
                        print(record)
                    if i + N < len(results):
                        input("Press enter to see the next page...\n")
                break
            else:
                print("Error: No matching records found.")

    def phone_exists(self, name, phone):
        existing_records = self.find_records(name)
        if existing_records:
            record = existing_records[0]
            return str(phone) in [str(phone_obj) for phone_obj in record.phones]
        return False
    
    def days_to_birthday(self):
        name = input('Enter name: ')
        if not name.strip():
            print('Name cannot be empty')
            pass
        existing = self.find_records(name)
        if existing:                
                record = existing[0]
                today = datetime.now()
                days = (datetime(today.year, record.birthday.value.month, record.birthday.value.day) - today).days
                if days:
                    print(f"Success: There are {days} days until {name}'s next birthday.\n")
                else:
                    print(f"Error: No birthday found for {name}.\n")
        else:
            print(f"Error: Name: {name} not found in the address book.\n")


    def upcoming_birthdays(self):
        while True:
            try:
                days = int(input("Enter the number of days to search for upcoming birthdays: "))
                if not days:
                    print('Days cannot be empty')
                    pass
                upcoming_bdays = []
                today = datetime.now().date()
                for record in self.data.values():
                    if record.birthday.value:
                        bday_this_year = datetime(today.year, record.birthday.value.month, record.birthday.value.day).date()
                        if (bday_this_year - today).days <= days:
                            upcoming_bdays.append(record)
                if days < 0:
                    print("Error: Please enter a non-negative number of days.\n")
                    pass
                if days == 0:
                    upcoming_bdays_today = [record for record in upcoming_bdays if datetime(today.year, record.birthday.value.month, record.birthday.value.day).date() == today]
                    if upcoming_bdays_today:
                        print(f"Success: Found contacts with birthdays today:")
                        for record in upcoming_bdays_today:
                            print(record)
                        break
                    else:
                        print("No upcoming birthdays found for today.\n")
                        break
                else:
                    upcoming_bdays_future = [record for record in upcoming_bdays if (record.birthday.value.month > today.month) or (record.birthday.value.month == today.month and record.birthday.value.day >= today.day)]
                    if upcoming_bdays_future:
                        print(f"Success: Found contacts with upcoming birthdays within {days} days:")
                        for record in upcoming_bdays_future:
                            print(record)
                        break
                    else:
                        print("No upcoming birthdays found.\n")
                        break
            except ValueError:
                print("Error: Please enter a valid number of days for upcoming birthdays search.\n")
            

    def __iter__(self):
        self._current = 0
        self._records = list(self.data.values())
        return self

    def __next__(self):
        if self._current >= len(self._records):
            raise StopIteration
        result = self._records[self._current]
        self._current += 1
        return result

    def save_to_file(self, filename):
        home_folder = os.path.expanduser("~")
        file_path = os.path.join(home_folder, filename)
        
        with open(file_path, 'wb') as fh:
            pickle.dump(self, fh)

    def load_from_file(filename):
        home_folder = os.path.expanduser("~")
        file_path = os.path.join(home_folder, filename)
        
        with open(file_path, 'rb') as fh:
            content = pickle.load(fh)
        return content
    
    def __repr__(self):
        output = ''
        if self.data:
            output += "Success: All Contacts:\n"
            N = 5
            records = list(self.data.values())
            for i in range(0, len(records), N):
                for record in records[i:i+N]:
                    output += str(record) + '\n'
                if i + N < len(records):
                    output += input("Press enter to see the next page...\n")
            return output
        else:
            return f"Error: Address book is empty.\n"