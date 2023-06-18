from model import *

phone = Phone_Dict()


def menu():
    while True:
        print("input ZERO for finish: ")
        number = int(input("input 1 for creat|| input 2 for edit|| input 3 for delete|| input 4 for print: "))
        if number == 1:
            phone.cread_data()
        elif number == 2:
            str1 = input("input what you want EDIT(example Anna): ")
            phone.edit_data(str1)
        elif number == 3:
            str1 = input("input what you wand DEL: ")
            phone.delete_Data(str1)
            print("You choice was delete...")
        elif number == 4:
            phone.read_data()
        elif number == 0:
            print("you go out .... ")
            return False
