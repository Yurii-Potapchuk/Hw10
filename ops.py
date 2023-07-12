from collections import UserDict


class AddressBook(UserDict):
    def addRecord(self, record):
        if record.name.value not in self.keys():
            self.data[record.name.value] = record
        else:
            print("Name already exist. Try add phone command for add extra phone.")


class Field:
    def __init__(self, value):
        self.value = value
    

class Name(Field):
    pass
        



class Phone(Field):    
    def __repr__(self):
        return str(self.value)


class Record(UserDict):
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)


    def add_phone(self, phone: Phone):
        if phone.value not in [phone.value for phone in self.phones]:
            self.phones.append(phone)
        else:
            print("This phone already added.")


    def del_phone(self, phone: Phone):
        for number in self.phones:
            if number.value == phone.value:
                self.phones.remove(number)


    def change_phone(self,old_phone: Phone, new_phone: Phone):
        if old_phone.value == new_phone.value or new_phone.value in [phone.value for phone in self.phones]:
            print("This phone alredy exist!")
        elif old_phone.value not in [phone.value for phone in self.phones]:
            print("This phone not found!")
        else:
            self.del_phone(old_phone)
            self.add_phone(new_phone)
            print("Contact phone succesfully changed.")
        