# Задайте список из N элементов, заполненных числами из промежутка [-N, N]
# Найдите произведение элементов на указанных позициях
# Позиции хранятся в файле file.txt в одной строке одно число

n = int(input('Введите число N: '))
list_numbers = []
mult_list = []

for i in range(-n, n + 1):
    list_numbers.append(i)
print(list_numbers)

# открываем файл и создаем лист построчно
input_file = open('D:\Code\PY_Analytics\PY_HM_Analytics\Task_204.txt')
input_file_list = input_file.readlines()

# переносим номера элементов в другой список, чтобы убрать \n
for i in range(len(input_file_list)):
    mult_list.append(input_file_list[i].replace('\n', ''))

result = 1
for i in range(len(mult_list)):
    result *= list_numbers[int(mult_list[i])]

print(f'Произведение элементов списка на позициях {mult_list} равно {result}')
