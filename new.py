# Рекурсивная функция - возвращает сумму чисел во входящем наборе
def CalcSumNumbers(A):
    if A == []:
        # если набор пуст, возвратить 0
        return 0
    else:
        # Вычислить сумму - прибавить первый элемент набора
        summ = CalcSumNumbers(A[1:]) # рекурсивный вызов этой же функции
        print(A[1:])

        # Прибавить к общей сумме первый элемент
        summ = summ + A[0]

        return summ

# Демонстрация использования функции CalcSumNumbers()
# 1. Создать набор чисел
my_list = [int(input('элемент массива: ')) for i in range(int(input('длина массива: ')))]

# 2. Вызвать функцию
summ = CalcSumNumbers(my_list)

# 3. Распечатать сумму
print("summ = ", summ)
