from collections import UserDict
from typing import Any

import regex
from colorama import Fore


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        self.value = value
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str):
        super().__init__(value)
        self.value = value


class Record:
    def __int__(self):
        pass

    def __init__(self, name: str):
        self.name = Name(name)
        self.phone = []

    def add_Phone(self, phone: str):
        if phone not in self.phone:
            return self.phone.append(Phone(phone).value)
        else:
            print("your Phone is in address book")

    def edit_Phone(self, oldPhone: str, newPhone: str):
        index = self.phone.index(oldPhone)
        result = self.phone[index] = newPhone
        return f"your new phone : {result}",

    def delete_Phone(self, phone: str):
        self.phone.remove(phone)

    def __str__(self):
        return self.name, self.phone


class AddressBook(UserDict):
    def add_Phone_in_book(self, record: Record):
        res = self.data[record.name.value] = record
        return res

    def find_Phone_by_Name(self, name: str) -> Any | None:
        res = self.get(name)
        if res is not None:
            return res
        else:
            return None
    def delete_Phone_by_Name(self, del_by_name: str):
        if del_by_name in self:
            self.pop(del_by_name)

    def all_name_and_phone(self):
        for k in self.data.keys():
            res = self.find_Phone_by_Name(k)
            print(f"{res.name} {res.phone}")


def check_Phone(phone: str):
    pettern1 = r"\D"
    matches = regex.sub(pettern1, "", phone)
    checkNumber = bool(regex.search(r"^380\d{9}$", matches))
    checkNum = bool(regex.search(r"^0\d{9}$", matches))
    checkN = bool(regex.search(r"^+380\d{9}$", matches))
    if checkNumber:
        number = "+" + matches
        dictNamePhone = number
        return dictNamePhone
    elif checkNum:
        number1 = "+38" + matches
        dictNamePhone1 = number1
        return dictNamePhone1
    elif checkN:
        dictNamePhone2 = matches
        return dictNamePhone2
    else:
        print(f"your phone is not correct : {phone}")


book = AddressBook()

print(F"{Fore.LIGHTBLUE_EX}Hello my Friend")
print("I am assistant bot!")

while True:

    print("select a command", "--->__add_Name_and_Phone<---> add")
    print("select a command", "--->__change_Phone<---> change")
    print("select a command", "--->__show_Name_by_Phone<---> show")
    print("select a command", "--->__all_Name_and_Phone<---> all")
    print("select a command", "--->__all_Name_and_Phone<---> del")
    command = input().__str__().lower().strip()
    if command == "add":
        print(F"{Fore.LIGHTYELLOW_EX}Your name and number Phone")
        name = input(F"{Fore.LIGHTYELLOW_EX}please your name:").strip().lower()
        phone = input(F"{Fore.LIGHTYELLOW_EX}please your phone :").strip().lower()
        record = Record(name)
        check_Phone1 = check_Phone(phone)
        record.add_Phone(check_Phone1)
        book.add_Phone_in_book(record)
        print(f"{record.name}, {record.phone}")
    if command == "change":
        print("Please your name and the new phone and old phone you want to replace")
        name_user = input("your name :").strip().lower()
        phone_Old = input("your old phone :").strip().lower()
        phone_New = input("you new phone :").strip().lower()

        name_this_address = book.find_Phone_by_Name(name_user)

        ch_ph_old = check_Phone(phone_Old)
        ch_ph_new = check_Phone(phone_New)

        result = name_this_address.edit_Phone(str(ch_ph_old), str(ch_ph_new))
        print(result)
    if command == "show":
        namePhoneFind = input("your name: ").strip().lower()
        show_phone_by_name = book.find_Phone_by_Name(namePhoneFind)
        if show_phone_by_name is not None:
            print(f"name: {show_phone_by_name.name}  phone: {show_phone_by_name.phone}")
        else:
            print("your number phone is not address book")
    if command == "all":
        book.all_name_and_phone()
    if command == "del":
        name = input(F"{Fore.LIGHTYELLOW_EX}please your name:").strip().lower()
        book.delete_Phone_by_Name(name)
    if command in ["close", "exit"]:
        print("Good bye my Friend!")
        break
