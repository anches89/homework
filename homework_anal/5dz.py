# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def func_1 (a,b):
#     if b==1:
#         return a
#     else:
#         return (a*func_1(a,b-1))
# a= int (input("Введите число: "))
# b= int (input("Введите его степень: "))
# print (func_1(a,b))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.

# def func_sum(a,b):
#     if a>b:
#         if b==0:
#             return a
#         else:
#             return func_sum(a+1,b-1)
#     else:
#         if a==0:
#             return b
#         else:
#             return func_sum(a-1,b+1)
# print(func_sum(10,5))