# Матасов Илья. ИУ7-21.
# gui + integral.

def f(arg):
    return arg * arg

def isCorrect(value):
    if (value == None) or (not value.isdigit()) or (value == ''):
        value = input('Введено некорректное значение. Повторите ввод: ')
        value = isCorrect(value)
    return value
    
def take_choose():
    global choose
    choose = input()
    choose = isCorrect(choose)
    if (choose == None) or (int(choose) > 7) or (int(choose) < 1):
        print('Неизвестный пункт в меню. Повторbте ввод: ',end = '')
        take_choose();

def method(start,end,parts = None,eps_def = None):
    if eps_def == None:
        integ = f(start) + f(end)
        local_n = 0
        h = (end - start) / parts
        while local_n < parts - 1:
            start += h
            local_n += 1
            if local_n % 2 !=  0:
                integ += 4 * f(start)
            else:
                integ += 2 * f(start)
        return h/3 * integ
    if parts == None:
        local_n = 2
        while abs(method(start,end,parts = 2*local_n)
                  - method(start,end,parts = local_n)) > eps_def:
            local_n *= 2
        integ = method(start,end,parts = local_n / 2)
        return integ
def menu():
    print('''
1) Задать начальное значение интервала.
2) Задать конечное значение интервала.
3) Задать число разбиений.
4) Задать точность вычисления.
5) Вычислить интеграл с количеством разбиений.
6) Вычислить интеграл с точностью.
7) Выход.
''')    
print('''
Вычисление определенного интерграла методом парабол для функции x^2
''')
choose = None
a = None
b = None
n = None
eps = None
while choose != '7':    
    menu()
    print('Выберите действие:',end = ' ')
    take_choose()
    if choose =='1':
        a = float(input('Введите начальное значение интервала: '))
    if choose == '2':
        b = float(input('Введите конечное значение интервала: '))
    if choose == '3':
        n = int(input('Введите число разбиений: '))
        if n % 2 != 0:
            n = None
            print('''Для метода парабол количество разбений
должно быть кратно 2''')
    if choose == '4':
        eps = float(input('Введите точность: '))
    if (choose == '5') and (a != None) and (b != None) and (n != None):
        result_A = method(a,b,parts = n)
        print('При ',n,'разбиениях интеграл равен:')
        print('{:<3.6f}'.format(result_A))
    elif choose == '5':
        if a == None: print('Необходимо указать начальное значение интервала')
        if b == None: print('Необходимо указать конечное значение интервала')
        if n == None: print('Необходимо указать число разбиений')
    if (choose == '6') and (a != None) and (b != None) and (eps != None):
        result_B = method(a,b,eps_def = eps)
        print('С точностью ',eps,' интеграл равен: ','{:<3.6f}'.format(result_B))
    elif choose == '6':
        if a == None: print('Необходимо указать начальное значение интервала')
        if b == None: print('Необходимо указать конечное значение интервала')
        if eps == None: print('Необходимо указать точность')    
