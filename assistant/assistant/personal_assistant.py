# from collections import UserDict
# from datetime import datetime, timedelta
# import pickle
# import re
# import shutil
# import os
# import zipfile
# import tarfile
# import gzip
# from pathlib import Path


# POLISH_LETTERS = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ż': 'z', 'ź': 'z'}

# IMAGE_EXTENSIONS = ['JPEG', 'PNG', 'JPG', 'SVG']
# VIDEO_EXTENSIONS = ['AVI', 'MP4', 'MOV', 'MKV', 'GIF']
# DOCUMENTS_EXTENSIONS = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'PY']
# AUDIO_EXTENSIONS = ['MP3', 'OGG', 'WAV', 'AMR']
# APLICATIONS_EXTENSIONS = ['EXE']
# ARCHIVES_EXTENSIONS = ['ZIP', 'GZ', 'TAR']


# class Field:
#     def __init__(self, value=None):
#         self.value = value

#     def __str__(self):
#         return str(self.value)


# class Name(Field):
#     def __init__(self, name):
#         super().__init__(name)


# class Phone(Field):
#     def __init__(self, phone):
#         normalized_phone = ''.join(filter(str.isdigit, str(phone)))
#         if len(normalized_phone) == 9:
#             self.phone = normalized_phone
#         else:
#             raise ValueError("Phone number must contain exactly 9 digits.")
#         super().__init__(phone)

#     def __str__(self):
#         return f'{self.phone}'
    
#     def __repr__(self):
#         return f'{self.phone}'


# class Birthday(Field):
#     def __init__(self, birthday=None):
#         if birthday is not None:
#             try:
#                 birthday = datetime.strptime(birthday, "%d-%m-%Y")
#             except ValueError:
#                 raise ValueError("Birthday must be in 'dd-mm-yyyy' format.")
#         super().__init__(birthday)


# class Address(Field):
#     def __init__(self, value=None):
#         self.value = value


# class Email(Field):
#     def __init__(self, email):
#         if email is not None:
#             check = re.findall(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email)
#             if len(check) == 1:
#                 self.value = email
#             else:
#                 raise ValueError('dupa')
#         else:
#             self.value = None


# class Tag(Field):
#     def __init__(self, value=None):
#         self.value = value


# class Note(Field):
#     def __init__(self, value=None):
#         self.value = value


# class Record:
#     def __init__(self, name, phone=[], birthday=None, address=None, email=None):
#         self.name = Name(name)
#         self.birthday = Birthday(birthday)
#         self.phones = []
#         # self.note = {}
#         self.address = address
#         self.email = email

#     def remove_phone(self, phone):
#         phone_to_remove = str(phone)
#         if phone_to_remove in [str(p) for p in self.phones]:
#             self.phones = [p for p in self.phones if str(p) != phone_to_remove]

#     def add_birthday(self, birthday):
#         self.birthday = Birthday(birthday)

#     def remove_birthday(self):
#         self.birthday = Birthday()

#     def add_address(self, address):
#         self.address = Address(address)

#     def edit_address(self, new_address):
#         self.address = Address(new_address)


#     # def days_to_birthday(self):
#     #     if self.birthday.value is None:
#     #         return None
#     #     now = datetime.now()
#     #     next_birthday = datetime(now.year, self.birthday.value.month, self.birthday.value.day)
#     #     if now > next_birthday:
#     #         next_birthday = datetime(now.year + 1, self.birthday.value.month, self.birthday.value.day)
#     #     return (next_birthday - now).days

#     def add_note(self, tag, new_note):
#         self.note[tag] = new_note

#     def remove_note(self, tag):
#         if tag in self.note:
#             del self.note[tag]
#             print(f"Success:  note with tag {tag} has been removed successfully. \n")


#     def edit_note(self, tag, new_note):
#         if tag in self.note:
#             self.note[tag] = new_note

#     def __str__(self):
#         try:
#             return f"Name: {self.name}, Phones: {', '.join(map(str, self.phones))}, Birthday: {self.birthday.value.date()}, Email: {self.email}, Address: {self.address}"
#         except AttributeError:
#             return f"Name: {self.name}, Phones: {', '.join(map(str, self.phones))}, Birthday: {self.birthday}, Email: {self.email}, Address: {self.address}"
        
# class AddressBook(UserDict):
#     def add_record(self):
#         name = input("Enter name: ")
#         if not name.strip():
#             print("Error: Name cannot be empty.\n")
            

#         existing_records = self.find_records(name)
#         if existing_records:
#             print(f"Error: Record: {name} already exists in the address book. Please choose a different name.\n")
            

#         else:
#             record = Record(name)                
#             phone = input("Enter phone number: ")
#             phone_str = ''
#             if phone.strip():
#                 try:
#                     phone = Phone(phone)
#                     record.phones.append(phone)
#                     phone_str = phone
#                 except ValueError as e:
#                     print(f"Incorrect phone number: {e}")

#             birthday = input("Enter birthday (dd-mm-yyyy): ")
#             birthday_str = ''
#             if not birthday.strip():
#                 record.birthday = None    
#             if birthday.strip():
#                 record.add_birthday(birthday)
#                 birthday_str = birthday
                

#             email = input("If you don't want to add email address just press enter. \nEnter email (example@dummy.com):")
#             email_str = ''
#             if email.strip():
#                 try:
#                     record.email.value = email
#                     email_str = email
#                 except ValueError:
#                     print('Invalid email address')

#             address = input('Enter address: ')
#             if address.strip():
#                 try:
#                     record.add_address(address)
#                 except ValueError:
#                     print('Failure during adding an address')

#         self.data[record.name.value] = record
#         print(f"Success: Record: \n Name: {name} \n Numbers: {phone_str}\n Birthday: {record.birthday}\n Email: {record.email}\n Address: {record.address}\n")
        
#     def add_phone(self):
#         while True:
#             name = input('Enter name: ')
#             if not name.strip():
#                 print('Name cannot be empty.')
#                 break
#             existing_records = self.find_records(name)
#             if not existing_records:
#                 print('No record found')
#                 continue
#             record = existing_records[0]
#             new_phone = input('Enter new phone: ')
#             record.phones.append(new_phone)
#             break

#     def add_email(self):
#         while True:
#             name = input("Enter name: ")
#             if not name.strip():
#                 print("Error: Name cannot be empty. Please enter a valid name.\n")
#                 break

#             existing_records = self.find_records(name)
#             if not existing_records:
#                 print(f"Error: This name: {name} does not exist in the address book. Please add a new record first.\n")
#                 continue
#             else:
#                 email = input('Enter email address: ')
#                 if email.strip():
#                     record = existing_records[0]
#                     new_email = Email(email)
#                     record.email = new_email
#                     print('done', record.name, ':', record.email)
#                     break
    
#     def add_address(self):
#         while True:
#             name = input("Enter name: ")
#             if not name.strip():
#                 print("Error: Name cannot be empty. Please enter a valid name.\n")
#                 break

#             existing_records = self.find_records(name)
#             if not existing_records:
#                 print(f"Error: This name: {name} does not exist in the address book. Please add a new record first.\n")
#                 pass
#             else:
#                 address = input('Enter address: ')
#                 if address.strip():
#                     record = existing_records[0]
#                     new_address = Address(address)
#                     record.address = new_address
#                     print('done', record.name, ':', record.address)
#                     break

#     def remove_address(self):
#         while True:
#             name = input('Enter name: ')
#             if not name.strip():
#                 print('Name cannot be empty.')
#                 break
#             existing = self.find_records(name)
#             if not existing:
#                 print('No record found.')
#                 pass
#             record = existing[0]
#             record.address = Address()
#             print('Done', record.name, 'address removed')
#             break

#     def edit_phone(self):
#         while True:
#             name = input('Enter name: ')
#             if not name.strip():
#                 print('Name cannot be empty')
#                 break
#             existing = self.find_records(name)
#             if not existing:
#                 print('No record found')
#                 pass
#             record = existing[0]
#             print(f'Current {record.name} phones:')
#             for i in record.phones:
#                 print(i)
#             choice = input('Select phone to remove (by index starting from 1)')
#             if not choice.strip():
#                 print('No number selected')
#                 break
#             try:
#                 record.phones.pop(int(choice) - 1)
#             except IndexError:
#                 print('Wrong index')
#                 pass
#             print('Phone removed')
#             number = input('Enter new phone: ')
#             if not number.strip():
#                 print('No number added')
#                 break
#             new_phone = Phone(number)
#             record.phones.append(new_phone)
#             print('Phone changed succesfuly', record.phones)
#             break

#     def remove_contact(self):
#         while True:
#             name = input('Enter name to remove: ')
#             if not name.strip():
#                 print('Name cannot be empty')
#                 break
#             existing = self.find_records(name)
#             if not existing:
#                 print(f'Record to {name} not found')
#                 pass
#             record = existing[0]
#             self.data.pop(record.name.value)
#             break

#     def add_birthday(self):
#         while True:
#             name = input('Enter name: ')
#             if not name.strip():
#                 print('Name cannot be empty')
#                 break
            
#             existing = self.find_records(name)
#             if not existing:
#                 print(f'No record with {name} found')
#                 pass

#             record = existing[0]
#             if record.birthday == None:
#                 birthday = input('Enter date of birth (dd-mm-yyyy): ')
#                 record.add_birthday(birthday)
#                 break

#     def edit_birthday(self):
#         while True:
#             name = input('Enter name: ')
#             if not name.strip():
#                 print('Name cannot be empty')
#                 break
            
#             existing = self.find_records(name)
#             if not existing:
#                 print(f'No record with {name} found')
#                 pass

#             record = existing[0]
#             if record.birthday != None:
#                 print(f'Current birthday date: {record.birthday}')
#                 birthday = input('Press enter if you do not want to change birth date\nEnter new date of birth (dd-mm-yyyy): ')
#                 if not birthday:
#                     print('Birthday not changed')
#                     break
#                 record.add_birthday(birthday)
#                 print(f'Success, new birthday {record.birthday}')
#                 break
    
#     def remove_birthday(self):
#         while True:
#             name = input('Enter name: ')
#             if not name.strip():
#                 print('Name cannot be empty')
#                 break
#             existing = self.find_records(name)
#             if not existing:
#                 print('No record found')
#                 pass
#             record = existing[0]
#             record.birthday = None
#             print('Success', record.birthday)
#             break

#     def find_records(self, keyword):
#         results = []
#         keyword_lower = keyword.lower()
#         for record in self.data.values():
#             if keyword_lower == record.name.value.lower():
#                 results.append(record)
#             else:
#                 for phone in record.phones:
#                     if keyword_lower == str(phone).lower():
#                         results.append(record)
#                         break  
#         return results

#     def find_partial_records(self):
#         while True:
#             search_char = input("Enter the character by which you want to search for users: ").strip().lower()
#             if not search_char:
#                 print("Error: The character you searched for cannot be empty.")
#                 break

#             results = []
#             keyword_lower = search_char.lower()
#             for record in self.data.values():
#                 if keyword_lower in record.name.value.lower() or any(keyword_lower in str(phone).lower() for phone in record.phones):
#                     results.append(record)
#             if results:
#                 print("Success: Records found:")
#                 N = 5
#                 for i in range(0, len(results), N):
#                     for record in results[i:i+N]:
#                         print(record)
#                     if i + N < len(results):
#                         input("Press enter to see the next page...\n")
#                 break
#             else:
#                 print("Error: No matching records found.")

#     def phone_exists(self, name, phone):
#         existing_records = self.find_records(name)
#         if existing_records:
#             record = existing_records[0]
#             return str(phone) in [str(phone_obj) for phone_obj in record.phones]
#         return False
    
#     def days_to_birthday(self):
#         name = input('Enter name: ')
#         if not name.strip():
#             print('Name cannot be empty')
#             pass
#         existing = self.find_records(name)
#         if existing:                
#                 record = existing[0]
#                 today = datetime.now()
#                 days = (datetime(today.year, record.birthday.value.month, record.birthday.value.day) - today).days
#                 if days:
#                     print(f"Success: There are {days} days until {name}'s next birthday.\n")
#                 else:
#                     print(f"Error: No birthday found for {name}.\n")
#         else:
#             print(f"Error: Name: {name} not found in the address book.\n")


#     def upcoming_birthdays(self):
#         while True:
#             try:
#                 days = int(input("Enter the number of days to search for upcoming birthdays: "))
#                 if not days:
#                     print('Days cannot be empty')
#                     pass
#                 upcoming_bdays = []
#                 today = datetime.now().date()
#                 for record in self.data.values():
#                     if record.birthday.value:
#                         bday_this_year = datetime(today.year, record.birthday.value.month, record.birthday.value.day).date()
#                         if (bday_this_year - today).days <= days:
#                             upcoming_bdays.append(record)
#                 if days < 0:
#                     print("Error: Please enter a non-negative number of days.\n")
#                     pass
#                 if days == 0:
#                     upcoming_bdays_today = [record for record in upcoming_bdays if datetime(today.year, record.birthday.value.month, record.birthday.value.day).date() == today]
#                     if upcoming_bdays_today:
#                         print(f"Success: Found contacts with birthdays today:")
#                         for record in upcoming_bdays_today:
#                             print(record)
#                         break
#                     else:
#                         print("No upcoming birthdays found for today.\n")
#                         break
#                 else:
#                     upcoming_bdays_future = [record for record in upcoming_bdays if (record.birthday.value.month > today.month) or (record.birthday.value.month == today.month and record.birthday.value.day >= today.day)]
#                     if upcoming_bdays_future:
#                         print(f"Success: Found contacts with upcoming birthdays within {days} days:")
#                         for record in upcoming_bdays_future:
#                             print(record)
#                         break
#                     else:
#                         print("No upcoming birthdays found.\n")
#                         break
#             except ValueError:
#                 print("Error: Please enter a valid number of days for upcoming birthdays search.\n")
            

#     def __iter__(self):
#         self._current = 0
#         self._records = list(self.data.values())
#         return self

#     def __next__(self):
#         if self._current >= len(self._records):
#             raise StopIteration
#         result = self._records[self._current]
#         self._current += 1
#         return result

#     def save_to_file(self, filename):
#         home_folder = os.path.expanduser("~")
#         file_path = os.path.join(home_folder, filename)
        
#         with open(file_path, 'wb') as fh:
#             pickle.dump(self, fh)

#     def load_from_file(filename):
#         home_folder = os.path.expanduser("~")
#         file_path = os.path.join(home_folder, filename)
        
#         with open(file_path, 'rb') as fh:
#             content = pickle.load(fh)
#         return content



# class CleanFolder:
#     def __init__(self, path):
#         self.path = path
#         self.all_existing_extentions = set()
#         self.unrecognized_extensions = set()



#     def normalize(self, some_string):  
#         result = ""
#         for char in some_string:
#             if char.lower() in POLISH_LETTERS:
#                 result += POLISH_LETTERS[char.lower()]
#             elif char.isspace() or char.isalnum():
#                 result += char
#             else:
#                 result += "_"
#         return result 

#     def move_and_normalize_files(self, file_path, new_folder_name):
#         normalized_name = self.normalize(Path(file_path).stem)
#         move_file = os.path.join(os.path.dirname(file_path), new_folder_name)
#         move_to = os.path.join(move_file, f"{normalized_name}.{file_path.split('.')[-1]}")

#         os.makedirs(move_file, exist_ok= True)
#         shutil.move(file_path, move_to)

#     def archive_folder_and_move(self, path, arch_name, new_folder_name):
#         arch_path = os.path.join(path, arch_name)
#         extracted_archive = os.path.join(path, arch_name.split('.')[0])
#         move_file = os.path.join(os.path.dirname(arch_path), new_folder_name)
#         move_to = os.path.join(move_file, arch_name.split('.')[0])

#         if arch_name.split('.')[-1].upper() == 'ZIP':
#             with zipfile.ZipFile(arch_path, 'r') as zip:
#                 zip.extractall(extracted_archive)

#         elif arch_name.split('.')[-1].upper() == 'TAR':
#             with tarfile.open(arch_path, 'r') as tar:
#                 tar.extractall(extracted_archive)

#         elif arch_name.split('.')[-1].upper() == 'GZ':
#             with gzip.open(arch_path, 'rb') as f_in, open(extracted_archive, 'wb') as f_out:
#                 shutil.copyfileobj(f_in, f_out)

#         os.remove(arch_path)
#         os.makedirs(move_file, exist_ok = True)
#         shutil.move(extracted_archive, move_to)      

#     def process_folder(self):
#         for root, dirs, files in os.walk(self.path):

#             for file in files:
#                 file_path = os.path.join(root, file)
#                 extension = file.split('.')[-1].upper()


#                 if any(folder in root for folder in ["Pictures", "Video", "Documents", "Music", "Aplications", "Unrecognized extensions"]):
#                     continue
#                 if extension in IMAGE_EXTENSIONS:
#                     self.all_existing_extentions.add(extension)
#                     self.move_and_normalize_files(file_path, "Pictures")
#                 elif extension in VIDEO_EXTENSIONS:
#                     self.all_existing_extentions.add(extension)
#                     self.move_and_normalize_files(file_path, "Video")
#                 elif extension in DOCUMENTS_EXTENSIONS:
#                     self.all_existing_extentions.add(extension)
#                     self.move_and_normalize_files(file_path, "Documents")
#                 elif extension in AUDIO_EXTENSIONS:
#                     self.all_existing_extentions.add(extension)
#                     self.move_and_normalize_files(file_path, "Music")
#                 elif extension in APLICATIONS_EXTENSIONS:
#                     self.all_existing_extentions.add(extension)
#                     self.move_and_normalize_files(file_path, "Aplications")
#                 elif extension in ARCHIVES_EXTENSIONS:
#                     self.all_existing_extentions.add(extension)
#                     self.archive_folder_and_move(root, file, "Archive")
#                 else:
#                     self.unrecognized_extensions.add(extension)
#                     continue

#             for dir in dirs:
#                 dir_path = os.path.join(root, dir)
#                 new_dir_path = os.path.join(root, self.normalize(dir))
#                 if not os.listdir(dir_path):
#                     os.rmdir(dir_path)
#                 else:
#                     os.rename(dir_path ,new_dir_path)
#         print(self.all_existing_extentions)
#         print(self.unrecognized_extensions)


# def main():
#     """
#     The main() function is responsible for managing user interaction with the phone book.
#     Users can perform various operations on entries in the phone book, such as adding,
#     editing, removing, searching, and displaying entries, and calculating the number of 
#     days to birthdays. The phonebook can be saved as well as loaded after restarting the 
#     program.

#     Commands:
#     - '.' - End the program.
#     - 'good bye', 'close', 'exit' - Terminate the program with the message "Good bye!".
#     - 'hello' - Display a greeting.
#     - 'add' - Add a new entry to the address book.
#     - 'remove contact' - Removes whole existing record in address book.
#     - 'add phone' - Add a new phone number to an existing entry.
#     - 'edit phone' - Edit an existing phone number.
#     - 'remove phone' - Remove a phone number from an existing entry.
#     - 'add address' - Adding address to an existing entry.
#     - 'edit address' - Editing address of an existing entry.
#     - 'remove address' - Removing address of an existing entry.
#     - 'add birthday' - Add a birthday to an existing entry.
#     - 'edit birthday' - Changes EXISTING birthday in entry.
#     - 'remove birthday' - Remove the birthday from an existing entry.
#     - 'add email' - Add an email address to en existing entry.
#     - 'edit email' - Edit email of an existing entry
#     - 'add note' - adds a new note with tag to contact.
#     - 'remove note' - removes a note from contact.
#     - 'edit note' - edits a note in contact.
#     - 'clean' - sorts files in chosen folder by file type.
#     - 'find' - Search for entries in the address book.
#     - 'days to birthday' - Calculate the number of days until the next birthday.
#     - 'upcoming birthdays' - Displays a list of contacts whose birthdays are a specified number of days from the current date;
#     - 'show all' - Display all entries in the address book.
#     - 'save' - Save the address book to a file.
#     - 'load address book' - Load the address book from a file.
#     - 'search and sort notes' - Search and sort notes by a specific tag.
#     """
#     address_book = AddressBook()

#     while True:
#         command = input("Enter command: ").lower()

#         if '.' in command:
#             break

#         elif command in ['good bye', 'close', 'exit']:
#             print("Good bye!")
#             break

#         elif command == "hello":
#             print("How can I help you?")

#         elif command == "add":
#             address_book.add_record()

#         elif command == "add phone":
#             address_book.add_phone()

#         elif command == 'add email':
#             address_book.add_email()

#         elif command == 'add address':
#             address_book.add_address()
            
#         elif command == "edit address":
#             address_book.add_address()

#         elif command == "remove address":
#             address_book.remove_address()

#         elif command == "edit phone":
#             address_book.edit_phone()

#         elif command == "edit email":
#             address_book.add_email()

#         elif command == 'remove contact':
#             address_book.remove_contact()
            
#         elif command == "find":
#             address_book.find_partial_records()

#         elif command == "add birthday":
#             address_book.add_birthday()
            
#         elif command == "edit birthday":
#             address_book.edit_birthday()

#         elif command == "remove birthday":
#             address_book.remove_birthday()

#         elif command == "clean":
#             path = input("Enter Path to folder:")
#             cleanfolder = CleanFolder(path)
#             try:
#                 cleanfolder.process_folder()
#             except TypeError:
#                 print("Error: Chosen path is incorrect.")

#         elif command == "days to birthday":
#             address_book.days_to_birthday()


#         elif command == "upcoming birthdays":
#             address_book.upcoming_birthdays()

#         elif command == "show all":
#             if address_book:
#                 print("Success: All Contacts:")
#                 N = 5
#                 records = list(address_book.data.values())
#                 for i in range(0, len(records), N):
#                     for record in records[i:i+N]:
#                         print(record)
#                     if i + N < len(records):
#                         input("Press enter to see the next page...\n")
#                 print()
#             else:
#                 print("Error: Address book is empty.\n")


#         elif command == "save":
#             filename = input("Enter the filename to save the address book: ")
#             address_book.save_to_file(filename)
#             print(f"Success: Address book saved to {filename}.\n")


#         elif command == "load address book":
#             filename = input("Enter the filename to load the address book from: ")
#             try:
#                 address_book = AddressBook.load_from_file(filename)
#                 print(f"Success: Address book loaded from {filename}.\n")
#             except FileNotFoundError:
#                 print(f"Error: File {filename} not found.\n")


#         else:
#             print("Error: Invalid command. Enter the correct command.\n")

# if __name__ == "__main__":
#     main()