# Матасов Илья. ИУ7-21.
# Простые иттерации с подбором.
import math as m
from math import log,sin,cos

def f(x):
    return sin(2*x)*x+1

def deriv(x):
    dx = 1e-5
    return (f(dx+x)-f(x))/dx

def c(a,d):
    array=[]
    step=(d-a)/10
    x=a
    c=0
    while x<=d:
        array.append(deriv(x))
        x+=step
    c=1/max(array)
    return c

a = float(input('Введите начало отрезка: '))
b = float(input('Введите конец отрезка: '))
a1=a
a11= a
b11= b
h=float(input('Введите шаг: '))
eps1=float(input('Введите эпсилон для двух соседних значений Х: '))
eps2=float(input('Введите эпсилон для значения функции: '))
maxiter=int(input('Введите максимальное число итераций: '))

print()
print('f(x)=Sin(x)')
print('  №    |       |        |        |            |реальное число| код')
print('корня  |   Xn  |  Xn+1  |   X    |     f(x)   |   итераций   |ошибки')

roots=[]
d=a+h
i=1
while d<=b:
    if f(a)*f(d)<0:
        k=1
        x1=(a+d)/2
        x2=x1-c(a,d)*f(x1)
        while (abs(x2-x1)>eps1 or abs(f(x2)>eps2)) and k<=maxiter:
            l=x2
            x2=x2-c(a,d)*f(x2)
            x1=l
            k+=1
        roots.append(x2)
        if k<=maxiter:
            er=0
        else:
            er=1
        print('{:^7d}|{:6.2f} |{:6.2f}  |{:7.3f} |{:11.3e} |'.format(i,a,d,x2,f(x2))+' '*5,k,' '*5+' |  ',er,'  ')
        i+=1
    a=d
    d=d+h
if i==1:
    er=2
    print('_______|_______|________|________|____________|______________|  ',er)


# 2 часть лабораторной работы, график функции

import matplotlib.pyplot as plt
import numpy as np

def deriv2(x):
    dx = 1e-5
    return (deriv(dx+x)-deriv(x))/dx

def deriv3(x):
    dx = 1e-5
    return (deriv2(dx+x)-deriv2(x))/dx

def c2(a,d):
    array=[]
    step=(d-a)/10
    x=a
    c=0
    while x<=d:
        array.append(deriv2(x))
        x+=step
    c=1/max(array)
    return c

x=np.linspace(a11,b11,500)
y=[]
for i in x:
    y.append(f(i))
plt.title('Graphic points $Sin(x)$')
plt.plot(x,y)
a=a1
d=a+h
rootes = []
while d<=b:
    if deriv(a)*deriv(d)<0:
        x1=(a+d)/2
        x2=x1-c2(a,d)*deriv(x1)
        while abs(x2-x1)>eps1 or abs(deriv(x2)>eps2):
            l=x2
            x2=x2-c2(a,d)*deriv(x2)
            x1=l
        rootes.append(x2)   
    a=d
    d=d+h

def c3(a,d):
    array=[]
    step=(d-a)/10
    x=a
    c=0
    while x<=d:
        array.append(deriv3(x))
        x+=step
    c=1/max(array)
    return c

a=a1
d=a+h
rootess = []
while d<=b:
    if deriv2(a)*deriv2(d)<0:
        x1=(a+d)/2
        x2=x1-c3(a,d)*deriv2(x1)
        while abs(x2-x1)>eps1 or abs(deriv2(x2)>eps2):
            l=x2
            x2=x2-c3(a,d)*deriv2(x2)
            x1=l
        rootess.append(x2)   
    a=d
    d=d+h

r1 = []
r2 = []
r3 = []
for root in roots:
    r1.append(f(root))
plt.plot(roots,r1,'kh',color = 'r')
for root in rootes:
    r2.append(f(root))
plt.plot(rootes,r2,'kh',color = 'y')
for root in rootess:
    r3.append(f(root))
plt.plot(rootess,r3,'kh',color = 'g')
l1 = u'График'
l2 = u'Корни'
l3 = u'Точки экстремума'
l4 = u'Точки перегиба'
plt.xlabel('x')
plt.ylabel('y $f(x)$')
plt.legend((l1,l2,l3,l4))
plt.grid(True)
plt.show()
