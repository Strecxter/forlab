# Матасов Илья. ИУ7-21.
# Создать меню для работы с файлом. Записи вида <Марка> <Страна>. 
menu_point = 5
sub_menu_point = 5

def menu():
    print('''
1) Создает файл / Выбрать уже существующий.
2) Добавляет запись.
3) Выполнить поиск по полю.
4) Вывести содержимое файла.
5) Выход.
''')

def sub_menu():
    print('''
1) Поиск по марке.
2) Поиск по стране.
3) Поиск всех марок, страна которых начинается с "A".
4) Поиск всех стран , в марках которых есть cлово "so".
5) Назад к меню.
''')

def take_choose(max_value):
    global choose
    choose = input()
    choose = isCorrect(choose)
    if (choose == None) or (int(choose) > max_value) or (int(choose) < 1):
        print('Неизвестный пункт в меню. Повторbте ввод: ',end = '')
        take_choose(max_value);

def isCorrect(value):
    if (value == None) or (not value.isdigit()) or (value == ''):
        value = input('Введено некорректное значение. Повторите ввод: ')
        value = isCorrect(value)
    return value

def print_File():
    f = open(file_name)
    for line in f.readlines():
        print(line,end = '')

def find_a():
    f = open(file_name)
    mark = input('По какой марке искать? ')
    for line in f.readlines():
        p_line = line.split()
        if p_line[0].lower() == mark.lower():
            print(line,end = '')
    f.close()
        
def find_b():
    f = open(file_name)
    country = input('По какой стране искать? ')
    for line in f.readlines():
        p_line = line.split()
        if p_line[1].lower() == country.lower():
            print(line,end = '')
    f.close()
    
def find_c():
    f = open(file_name)
    for line in f.readlines():
        p_line = line.split()
        if p_line[1][0].lower() == 'а':
            print(line,end = '')
    f.close()

def find_d():
    f = open(file_name)
    for line in f.readlines():
        p_line = line.split()
        if 'so' in p_line[0].lower():
            print(line,end = '')
    f.close()

choose = None
my_file = None
last = None
file_name = None

while choose != str(menu_point):
    menu()
    print('Выберите пункт меню: ',end = '')
    take_choose(menu_point)
    if choose == '1':
        file_name = input('Введите имя файла: ')
        if last == file_name:
            my_file = open(file_name,"a+")
        elif last != None:
            my_file.close()
            my_file = open(file_name,"a+")
        my_file = open(file_name, "a+")
        last = file_name
    elif choose == '2' and my_file != None:
        p1 = input('Введите марку: ')
        p2 = input('Введите страну: ')
        p = p1 + ' ' + p2
        my_file.write(p + '\n')
        my_file.close()
        my_file = open(file_name, "a+")
    elif choose == '3' and my_file != None:
        sub_menu()
        print('Выберите пункт меню: ',end = '')
        take_choose(sub_menu_point)
        if choose == '1':
            find_a()
        if choose == '2':
            find_b()
        if choose == '3':
            find_c()
        if choose == '4':
            find_d()
        choose = None
    elif choose == '4' and my_file != None:
        print_File()
    elif choose == str(menu_point):
        pass
    else:
        print('Необходимо выбрать файл.')
if my_file != None: my_file.close()


        
    
    
