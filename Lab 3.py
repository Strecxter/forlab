# Матасов Илья.
# Quicksort и numpy.sort().

from random import randint
import numpy as n
from time import perf_counter

# Формирование массива.

def gen_mass(count):
    arr = []
    for i in range(count):
        arr.append(randint(0,count*3))
    return arr

# Быстрая сортировка.

def qSort(v,l,r):
    i = l;
    j = r;
    q = v[(l+r) // 2];
    while i <= j:
        while v[i] < q: i+=1
        while q < v[j]: j-=1
        if i <= j:
            v[j],v[i] = v[i],v[j]
            i += 1
            j -= 1
    if l < j: qSort(v,l,j);
    if i < r: qSort(v,i,r);

# Время для быстрой сортировки.

def Time_Quick(array):
    a = perf_counter()
    qSort(array,0,len(array)-1)
    a = perf_counter() - a
    return a

# Время для numpy.sort().

def Time_Numpy(array):
    a = perf_counter()
    array = n.sort(array)
    a = perf_counter() - a
    return a

# Вывод таблицы

def print_table():
    line = 34*'-'
    print(line)
    print('{:6d}|{:7f}|{:7f}|{:7f}|'.format(cur,t1,t2,t3))

def Timess(array):
    a = perf_counter()
    array.sort()
    a = perf_counter() - a
    return a
# Тело программы.
# Проверка работоспособности.
xx = []
qqq = int(input('Введите число элементов для теста:'))
print('Введите ',qqq,' элементов:')
for i in range(qqq):
    xx.append(int(input()))
xx1 = xx[:]
xx2 = xx[:]
print('После сортировки:')
qSort(xx1,0,len(xx1)-1)
xx2 = n.sort(xx2)
print('NumPy.Sort:',xx2)
print('QuickSort:',xx1)

# Таблица.
print('{:6s}|{:8s}|{:8s}|{:8s}|'.format('Кол-во','Quick','Numpy','sort'))
cur = 10  # Начальная длина массива.
maxx = 100000 # Максимальная длина массива.
while cur <= maxx:
    arr = gen_mass(cur)
    arr1 = arr[:]
    arr2 = arr[:]
    arr3 = arr[:]
    t1 = Time_Quick(arr1)
    t2 = Time_Numpy(arr2)
    t3 = Timess(arr3)
    dt = abs(t1-t2)
    print_table()
    cur *= 10
    
    
