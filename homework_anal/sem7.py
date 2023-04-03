#lambda, filter, map, zip, enumerate, list comprehension

#list comprehension
# a = [i if i%2==0 else 0 for i in range(1,10)]
# print(a)

#enumerate
# a = [0, 2, 0, 4, 0, 6, 0, 8, 0]
# for indx,val in enumerate(a):
#     print(indx,val)

#zip
# a = (1,2,4,5,6)
# b = "abcd"
# f = {45:"b",54:"c",87:"fr"}
# for i in zip(a,b,f.values()):
#     print(i)

#lambda

# def summa(x,y):
#     return x+y

# summa = lambda x,y: x+y if x%2==0 else 0
#
# print(summa(8,6))

#map
# def pow(x):
#     if x%2==0:
#         return 1
#     else:
#         return x
# a = [1,2,3,4,5,6]
# a = list(map(pow, a))
# print(a)

#filter
# a = [1, 2, 3, 4, 5, 6]
# a = list(filter(lambda x: x % 2, a))
# print(a)


#сортировка по ключу

# a = [(1,0,5),(3,0,4),(-5,-1,3),(5,-2,2)]
# maxx = max(a,key=lambda x:x[2])
# print(maxx)

# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# orbits = list(filter(lambda x: x[0]!=x[1], orbits))
# print(orbits)
# maxx= max(orbits, key= lambda x: x[0]*x[1])
# print(maxx)

# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# def same_by (values):
#     a = list(filter(lambda x: True if x%2 else False, values))
    
#     if len(a) == 0:
#         return "same"
#     else:
#         return "diff"


# values = [0, 1, 2, 6] 
# print(same_by(values))

# Имеется упорядоченный список:

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# # #
# # # Перебрать все элементы этого списка с помощью функций enumerate и 
# элементы, стоящие на главной диагонали (имеющие равные индексы со списком 
# и индексом элемента внутри списка), превратить в нули.

# a = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]

# for indx,val in enumerate(a):
#     a[indx][indx] = 0

# print(a)
