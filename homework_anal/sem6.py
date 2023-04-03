# num_1 = int(input('Введите количество элементов в первом массиве: '))
# list_1 = list()

# for i in range(num_1):
#     x = int(input('введите элемент массива: '))
#     list_1.append(x)
# print(list_1)
# num_2 = int(input('Введите количество элементов во втором массиве: '))
# list_2 = list()

# for i in range(num_2):
#     x = int(input('введите элемент массива: '))
#     list_2.append(x)
# print(list_2)
# list_new = list()

# def result (list_1, list_2, list_new):
#     for i in list_1:
#         if i not in list_2:
#             list_new.append(i)
#         # for j in list_2:
#         #     if i == j:
#         #         list_new.append(i)

#     return list_new



# print(result(list_1, list_2, list_new))


# num_1 = int(input('Введите количество элементов в первом массиве: '))
# list = list()

# for i in range(num_1):
#     x = int(input('введите элемент массива: '))
#     list.append(x)
# print(list)

# count = 0
#                                 #   0 1 2 3 4
# def summ (list, count):         # [ 6 5 1 5 1]
#     for i in range(1, len(list)-1):
#         if list[i-1]<list[i]>list[i+1]:
#             count +=1

#     return count

# print(summ(list, count))

# sum_1 = int(input('Введите количество элементов в первом массиве: '))
# list = list()

# for i in range(num_1):
#     x = int(input('введите элемент массива: '))
#     list.append(x)
# print(list)

# count = 0
#                                 #   0 1 2 3 4 5 6
# def para (list, count):         # [ 1 2 3 2 3 2 2]
#     for i in range(len(list)):
#         for j in range(i+1, len(list)):
#             if list[i] == list[j]:
#                 count +=1
#     return count

# print(para(list, count))