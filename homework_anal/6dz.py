# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# list_1= []
# def inPUT (a1, d, n):
#     for i in range (n):
#         a=a1+(i-1)*d
#         list_1.append(a)
#     return list_1
# a1= int(input("Введите число: "))
# d= int(input("Введите число: "))
# n= int(input("Введите число: "))
# print(inPUT(a1,d,n))

# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не болше заданного максимума)

# import random
# list_1=[]
# n= int(input("Введите число: "))
# for i in range (n):
#     list_1.append(random.randint(0,10))
# print(list_1)
# max1= int(input("Введите max число: "))
# min1= int(input("Введите min число: "))
# for i in range(len(list_1)):
#     if min1<list_1[i]<max1:
#         print(i)

