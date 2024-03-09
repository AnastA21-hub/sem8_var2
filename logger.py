from data_create import name_data, surname_data, phone_data, address_data # импортируем функции из другого файла


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
                    f"1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 Вариант: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))
    while var != 1 and var != 2:
        print("Неправильный ввод!")
        var = int(input('Введите число: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def print_data():
    print('Вывожу данные из первого файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f: # открываем файл на режиме чтения
        data_first = f.readlines() #читаем все строки
        data_first_list = [] # создаем список для хранения итогового результата
        j = 0 #счетчик
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i])) #в список добавляем новую запись
                j = i
        print([''.join(data_first_list)])
        
    print('Вывожу данные из второго файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f: # открываем файл на режиме чтения
        data_second = f.readlines() #читаем все строки
        print(data_second)


def option_file(): #функция выбора файла
    print("Выберете файл: \n 1 - Вариант 1 \n 2 - Вариант 2")
    var = int(input('Введите число: '))    
    while var != 1 and var != 2:
        print("Неправильный ввод!")
        var = int(input('Введите число: '))
    return var

  
def redact_data(op, num):
      
    if op == 1:    
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f: 
            data_first = f.read() #читаем все строки
            data_first_list = data_first.rstrip().split('\n\n')
            old_data = input('Введите данные, которые хотите изменить: ')
            new_data = input('Введите новые данные: ')
            data_first_list[num - 1] = data_first_list[num - 1].replace(old_data, new_data)
            new_data_first = '\n\n'.join(data_first_list)
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.write(new_data_first)  
            
                  
    elif op == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f: 
            data_second = f.read()
            data_second_list = data_second.rstrip().split('\n')
            old_data = input('Введите данные, которые хотите изменить: ')
            new_data = input('Введите новые данные: ')
            data_second_list[num - 1] = data_second_list[num - 1].replace(old_data, new_data)
            new_data_second = '\n'.join(data_second_list)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.write(new_data_second)
        
       

def delete_data(op, num):
       
    if op == 1:    
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f: 
            data_first = f.read() #читаем все строки
            data_first_list = data_first.rstrip().split('\n\n')
            
            if num == 1:
                data_first_list = data_first_list[1:]
            elif num <= len(data_first_list):
                i = num - 1
                data_first_list = data_first_list[:i] + data_first_list[i+1:]
            
            new_data_first = '\n\n'.join(data_first_list)
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.write(new_data_first)
          
    elif op == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.read() #читаем все строки
            data_second_list = data_second.rstrip().split('\n')
            
            if num == 1:
                data_second_list = data_second_list[1:]
            elif num <= len(data_second_list):
                i = num - 1
                data_second_list = data_second_list[:i] + data_second_list[i+1:]
            
            new_data_second = '\n'.join(data_second_list)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.write(new_data_second)
                   

def search_data():
    op = option_file()# в каком файле будем искать
    search = input('Введите данные для поиска: ')
    if op == 1:    
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f: 
            data_first = f.read() #читаем все строки
            data_first_list = data_first.rstrip().split('\n\n')
            for n, element in enumerate(data_first_list, 1): #добавляем нумерацию контактов, 1 - это начало нумерации
                if search in element:
                    print(n, element)
            num = int(input('Введите номер контакта: ')) 
            
    elif op == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f: 
            data_second = f.read()
            data_second_list = data_second.rstrip().split('\n')
            for n, element in enumerate(data_second_list, 1): #добавляем нумерацию контактов, 1 - это начало нумерации
                if search in element:
                    print(n, element)
            num = int(input('Введите номер контакта: '))
            
    print('Выберете действие:\n'
          '1. Изменить данные контакта\n'
          '2. Удалить контакт')
    step = int(input('Введите число: '))
    if step == 1:
        redact_data(op, num)
    elif step == 2:
        delete_data(op, num)
    while step != 1 and step != 2:
        print("Неправильный ввод!")
        step = int(input('Введите число: '))
    
    
    
    
    
    
            




#search_data()

#redact_data()
#delete_data()


# def redact_data(op, num):
#     print('Выберете данные, которые хотите изменить:\n'
#           '1. Имя\n'
#           '2. Фамилия\n'
#           '3. Номер телефона\n'
#           '4. Адрес\n')
#     var = input('Введите число: ')
#     match var:#действия после выбора варианта, math заменяет if или if-else 
#             case '1':#пользователь выбрал вариант 1, тогда
#                 name = name_data()
#             case '2':#пользователь выбрал вариант 2, тогда
#                 surname = surname_data()
#             case '3':#пользователь выбрал вариант 3, тогда
#                 phone = phone_data()
#             case '4':
#                 address = address_data()
              
#     if op == 1:    
#         with open('data_first_variant.csv', 'r', encoding='utf-8') as f: 
#             data_first = f.read() #читаем все строки
#             data_first_list = data_first.rstrip().split('\n\n')
            



