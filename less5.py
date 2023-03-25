# Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат
# inputExpr = str(input('Введите строку: '))
# def CalculateFunc(sentence):
#     sum = 0
#     m = 1
#     for c in sentence:
#         if c == '-':
#             m = -1
#         elif c == '+':
#             m = 1
#         else:
#             sum += int(c)*m
#     return sum
# print (CalculateFunc(inputExpr))


# Задача 2
# Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)

# inputStr = str(input('Введите строку: '))
# def SplitFunc(expr):
#     newList = []
#     word=''
#     for c in expr:
#      if c == ' ':
#             newList.append(word)
#             word = ''
#      else:
#             word += c
#     if word:
#          newList.append(word)
#     return newList
# print ('\n'.join (SplitFunc(inputStr)))

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# a = int(input('Введите A: '))
# b = int(input('Введите B: '))
# def A_pow_B(a, b):
#     if b == 0:
#         return 1
#     return a * A_pow_B(a, b - 1)
# print(A_pow_B(a, b))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
a = int(input())
b = int(input())
def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)
print(sum(a, b))
