import ops


bot_on = True

adress_book = ops.AddressBook()
stop_words = ["good bye", "close", "exit"]

def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except UnboundLocalError:
            return  'Enter command'        
        except TypeError:
            return "Require name and phone! Or old and new phone!"
        except KeyError:
            return 'Not name given! Enter name after command...'
        except IndexError:
            return 'Immproper argumets are given! Require name and phone number! Try again...'
    return inner


def helper(*args):
    res = ''
    for key in comands.keys():
        res += f"-{key}\n"
    return  f"\n | Available bot functions:|\n{res}"


def error(*args):
    return "Unknown command. Use function 'help' to show available commands..."


def hello(*args):
    return " How can I help you? To see awailable comands type 'help'"


@input_error
def add(name, phone):
      
    if not name.isalpha():
        return "Name must be alphabetic! Try again..."
    elif not phone.isdigit():
        return "Number must be numerical! Try again..."
    else:
        rec = ops.Record(ops.Name(name), ops.Phone(phone))
        adress_book.addRecord(rec)
        # phone_num = [phone.value for phone in adress_book[rec.name.value].phones]
        return f"New contact {rec.name.value} added in dict. To show contacts use 'show all'...\n"
        

@input_error
def change_phone(name, old_phone, new_phone):
    
    rec = adress_book[name]
    rec.change_phone(ops.Phone(old_phone), ops.Phone(new_phone))
    return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}\n"
    
   
@input_error
def add_phone(name, phone):
    
    rec = adress_book[name]
    rec.add_phone(ops.Phone(phone))
    return f"{rec.name.value} : {[phone.value for phone in rec.phones]}"



@input_error
def delete_phone(name, phone):
    
    rec = adress_book[name]
    rec.del_phone(ops.Phone(phone))
    if phone.isdigit():
        return f"{rec.name.value} : {[ phone.value for phone in rec.phones]}\n"
    else:
        return "Number is not numerical!"




@input_error
def phone(name):
    rec = adress_book[name]
    number = [phone.value for phone in rec.phones]
    return f"{rec.name.value} : {list(number)}\n"



def show_all(*args):
    res = ''

    for name, record in adress_book.items():
        res += f"{name} : {[phone.value for phone in record.phones]}\n"
    return f'\n__________AddressBook:___________\n{res}'


comands =  {'hello':hello,
            'add phone': add_phone,
            'add new': add,
            'change':change_phone,
            'phone':phone,
            'show all':show_all,
            'help':helper,
            'delete phone': delete_phone,
            }

def parser(text):
    for key in comands.keys():          #скрипт знаходить ключ у введеному в консоль повідомленні і підставляє значення у відповідну функцію
            # comand = user_input.lower()
            # user_command = user_input.split()      
        if text.lower().startswith(key):
            func = comands.get(key)
            args = text[len(key):].strip().split()
            return func, args
    return None, None
    


def main():             #Вирішую робити через таку структуру щоб програма одразу оцінювала те що вводиться з консолі, як на мене такий варіант є логічним так як можна в будьякий момент додати нові ключі в команди і записати під кожен ключ нову окрему функцію. Також усі варіанти окрім ключів-функцій одразу відсіюються. А при правильному введені функції скрипт повертає одразу значення з потрібної функції.

    while True:
        user_input = input(">>> ")
        # key_word = user_input.lower().split()
        if user_input in stop_words: # Замінив на список
            print("Good bye!")
            break
        func, args = parser(user_input)
        if func:
            result = func(*args)
        else:
            result = error(user_input) 
        print(result) 
            

if __name__ == "__main__":
    main()