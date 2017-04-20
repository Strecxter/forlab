# Матасов Илья.

from tkinter import *

'''
---------------------------------Отрисовка--------------------------------------
'''
def print_axis():
    canv.create_line(d,size,d,0,width=2,arrow=LAST) # Ось у.
    canv.create_line(0,d,size,d,width=2,arrow=LAST) # Ось х.
    canv.pack()

def print_lines():
    for i in lines:
        x1,y1,x2,y2 = coords(i)
        canv.create_line(x1+d,-y1+d,x2+d,-y2+d,width=2,fill = 'red')
    x1 = points[max_i][0]
    y1 = points[max_i][1]
    x2 = points[max_j][0]
    y2 = points[max_j][1]
    canv.create_line(x1+d,-y1+d,x2+d,-y2+d,width=2,fill = 'gray')
    canv.pack()

def print_points():
    for i in points:
        x = i[0]
        y = i[1]
        canv.create_oval(x-1+d, -y+d-1, x+1+d, -y+d+1,fill = 'yellow')
    canv.pack()

def print_graph():
    print_axis()
    print_lines()
    print_points()
'''
---------------------------------Объявление-------------------------------------
'''
points = []    # Массив точек.
lines = []     # Массив прямых.
k = []         # Массив углов наклона.
size = 500     # Размер окна.
d = size // 2  # Середина окна.
max_i = 0      # Первая точка.
max_j = 0      # Вторая точка.
root = Tk()    
canv = Canvas(root, width = size,
                  height = size, bg = "white", cursor = "pencil")
'''
---------------------------------Ввод-данных------------------------------------
'''
def add_point():
    global point
    x,y = map(float,input('Введите координаты точки: ').split())
    points.append((x,y))
    
def add_line():
    global lines
    x,y = map(float,input('Введите координаты 1 точки прямой: ').split())
    z,w = map(float,input('Введите координаты 2 точки прямой: ').split())
    lines.append(((x,y),(z,w)))

def input_points():
    n = int(input('Введите количество точек: '))
    if n > 1:
        for i in range(n):
            print('Для',i+1,'точки:')
            add_point()
    else:
        print('Необходимо ввести больше 2 точек!')
        input_points()
def input_lines():
    n = int(input('Введите количество прямых: '))
    if n > 0:
        for i in range(n):
            print('Для',i+1,'прямой:')
            add_line()
    else:
        print('Необходимо ввести хотя бы одну прямую!')
        input_lines()
def input_data():
    input_points()
    input_lines()

'''
-------------------------Определение-угла-наклона-прямых------------------------
'''

def coords(array_lines):
    x1 = array_lines[0][0]
    y1 = array_lines[0][1]
    x2 = array_lines[1][0]
    y2 = array_lines[1][1]
    return x1,y1,x2,y2
    
def coefficient(x1,y1,x2,y2):
    if x1 - x2 != 0:
        coeff = (y1 - y2)/(x1 - x2)
    else:
        coeff = '+'
    return coeff
    
def all_coefficient():
    for i in lines:
        x1,y1,x2,y2 = coords(i)
        k.append(coefficient(x1,y1,x2,y2))

'''
------------Определение-максимального-количества-параллельных-прямых------------
'''
def max_line_count():
    global max_i
    global max_j
    max_count = 0
    for i in range(len(points)-1):
        for j in range(i+1,len(points)):
            count = 0
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            current_k = coefficient(x1,y1,x2,y2)
            for g in k:
                if current_k == g:
                    count += 1
            if count > max_count:
                max_i = i
                max_j = j
                max_count = count
    return max_count
            
'''
--------------------------Основное-тело-программы-------------------------------
'''


def main():
    input_data()                      # Ввод данных.
    all_coefficient()                 # Расчет коэффициентов наклона.
    max_count = max_line_count()      # Определение максимального числа прямых.
    print('Для прямой проведенной через точки:')
    print(points[max_i],'и через',points[max_j])
    print('Максимальное количество прямых -', max_count)
    print_graph()                     # Отрисовка.
    root.mainloop()                   # Вывод формы.

    
if __name__ == '__main__':
    main()
