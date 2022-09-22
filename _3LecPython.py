#Ускоренная
#обработка данных:
#lambda, filter, map,
# zip, enumerate, List
#Comprehension
#Простое и любопытное

#Анонимные, lambda функции
#Идея: часто описывать функцию
#некогда и незачем

from colorsys import yiq_to_rgb
from tkinter import Y
from turtle import ycor


def sum(x):
 return x+10

def mult(x):
 return x**2

sum(mult(2))

def sum1(x):
 return x+22

def mult2(x):
 return x**3

sum1(mult2(2))

def sum3(x):
 return x+242

def mult4(x):
 return x**5

sum3(mult2(2))

def f(x):
    x**2

g = f
print(f(1))
print(g(1))

def f(x):
    return x**2

print(f(2))

def f(x):
    return x**2

g = f
print(type(f))
print(type(g))

print(f(4))
print(g(4))


def calc1(x):
    return x+10

def calc2(x):
    return x*10

def math(op, x):
    print(op(x))

math(calc2, 10)
math(calc1, 10)

#def sum(x, y):
#    return x+y 

def mult(x, y):
    return x*y 

def calc(op, a, b):
    print(op(a, b))
    #return op(a, b))

calc(lambda x, y: x+y, 4, 5)

sum = lambda x: x+10
mult = lambda x: x**2

sum(mult(2))

sum1 = lambda x: x+22
mult2 = lambda x: x**3

sum1(mult2(2))

sum4 = lambda x: x+242
mult4 = lambda x: x**5

sum3(mult2(2))

#f(g(x))
#def h(f, g, x): return f(g(x))h = lambda f, g, x: f(g(x)) подчеркивает красным
#h(sum, mult, 5)
#h(lambda x: x+10, lambda x: x**2, 5)

#List comprehension

#list[]

#for i in range(1, 21):
#      if(%2 == 0):
#    list.append(1);

#print(list)

#list = [for i in range(1,21) if i % 2 == 0]
print(list)


#К чему это всё?
#В файле хранятся числа, нужно выбрать четные и
#составить список пар (число; квадрат числа).
#Пример:
#1 2 3 5 8 15 23 38
#Получить:
#[(2, 4), (8, 64), (38, 1444)]

def select(f, col):
    return[f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 18 23 38'.split()

res = select(int, data)
res  = where(lambda x: not x % 2, res)
res  = select(lambda x: (x, x**2), res) #лямбда +кортеж
print(res)

#Функия map

#Функция map() применяет указанную функцию к
#каждому элементу итерируемого объекта и
#возвращает итератор с новыми объектами.
#f(x) ⇒ x + 10
#map(f, [ 1, 2, 3, 4, 5])
# ↓ ↓ ↓ ↓ ↓
# [ 11, 12, 13, 14, 15]
#Нельзя пройтись дважды

li = [x for x in range(1,20)]

li = list(map(lambda x:x+10, li))

print(li)

data = list(map(int, input().split()))
print(data)

data = map(int, input().split())

for e in data:
    print(e)

def where(f, col):
    return[x for x in col if f(x)]

data = '1 2 3 5 18 23 38'.split()

res = map(int, data)
res  = where(lambda x: not x % 2, res)
res  = list(map(lambda x: (x, x**2), res))
print(res)

#Функция Filter
#Помогает избавиться от функции where

#Функция filter() применяет указанную функцию к
#каждому элементу итерируемого объекта и
#возвращает итератор с теми объектами, для
#которых функция вернула True.
#f(x) ⇒ x - чётное
#filter(f, [ 1, 2, 3, 4,5])
# ↓
# [ 2, 4 ]
#Нельзя пройтись дважды

data = [x for x in range(10)]
res = list(filter(lambda x: not x%2, data)) #лямбда аргумент, ктр проверяет явл ли число четным
print(res)#результат работы будет свой обьект типа filter result

#Функция Zip
#Функция zip() применяется к набору итерируемых
#объектов и возвращает итератор с кортежами из
#элементов входных данных.
#Количество элементов в результате равно минимальному количеству элементов входного набора
#zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
# ↓
#[(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
#Нельзя пройтись дважды

users = ['users1', 'users2', 'users3', 'users4', 'users5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids, salary))
print(data)

#Функция Enumerate
#Функция enumerate() применяется к итерируемому
#объекту и возвращает новый итератор с кортежами
#из индекса и элементов входных данных.
#enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
# ↓
#[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
#Нельзя пройтись дважды

users = ['users1', 'users2', 'users3', 'users4', 'users5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(enumerate(users))
print(data)