# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

# def fill_float_digit_list(num):
#     lst = []
#     for i in range(num):
#         lst.append(float(input(f'Введите {i + 1}-й элемент списка: ')))
#     return lst

# lst = fill_float_digit_list(int(input('Введите длину списка: ')))
# min, max = lst[0] % 1, lst[0] % 1
# for i in lst:
#     if i % 1 < min:
#         min = i % 1
#     if i % 1> max:
#         max = i % 1
# print(f'Исходный список: {lst}')
# print(f'Разница между максимальным и минимальным значением дробной части = {round(max - min, 2)}')


num = int(input('Введите длину списка: '))
lst = [float(input(f'Введите {i + 1}-й элемент списка: ')) for i in range(num)]
lst = list(map(lambda x: x % 1, lst))
print(f'Разница между максимальным и минимальным значением  = {round(max(lst) - min(lst), 2)}')