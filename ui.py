# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в дыух файлах, разных форматов записи.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные
# 3. Использование функций. Ваша программа не должна быть линейной.
from logger import input_data, print_data, search_data


def interface(): # создаем интервейс пользователя 
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n 1 - запись данных \n 2 - вывод данных \n 3 - поиск контакта")
    command = int(input('Введите число: '))
    while command != 1 and command != 2 and command != 3:
        print("Неправильный ввод!")
        command = int(input('Введите число: '))
    
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        search_data()
      
        
