# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму

n = int(input('Введите число N: '))

list_numbers = []
sum = 0

for i in range(1, n + 1):
    result = round((1 + 1/i)**i, 2)
    sum += result
    list_numbers.append(result)

print(f'Сумма последовательности {list_numbers} равна {sum}')