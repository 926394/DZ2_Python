from show_data import *
from find_data import *
from delet_data import *
from editing_data import *
from index_strings import *

def menuHello():
    print("1.Добавить")
    print("2.Вывести всех")
    print("3.Поиск по фамилии")
    print("4.Выход")
    print("5.Редактирование данных")
    print("6.Удаление данных")
    print("7.Удаление данных по фамилии")
    print("8.Поиск № по фамилии")

    print('\n')
    userInput = int(input("Выберите номер действия: "))

    if userInput == 1:
        addData()
        return True
    if userInput == 2:
        printAll()
        return True
    if userInput == 3:
        print('\n'*1)
        find(input("Введите фамилию: "))
        return True
    if userInput == 4:
        return False
    if userInput == 5:
        print('\n'*1)
        findZ(input("Введите фамилию: "))
        return True
    if userInput == 6:
        Delet()
        return True
    if userInput == 7:
        Delet1(input("Введите фамилию: "))
        return True
    if userInput == 8:
        index_string(input("Введите слово: ")) 
        return True

def addData():
    data = open('Zfile.txt', 'a')
    print('\n'*1)
    second_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    mid_name = input("Введите отчество: ")
    number = input("Введите номер телефона: ")
    item = [second_name, first_name, mid_name, number]
    s = ' '
    data.writelines(s.join(item) + '\n')
    data.close()
    print('\n'*1)