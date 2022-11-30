# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

N = int(input('Введите число \n'))

my_list = list(range(-N, N + 1))
print(my_list)

c = [int(i) for i in input('Введите позицию элемента через пробел ').split(' ')]
print(c)

prod = 1
for i in range(len(c)):
    prod *= c[i]
print(f'Произведение элементов на указанных через пробел позициях - {prod}')

# Или:

n = int(input('Enter a number \n'))
numbers = []
for i in range(-n, n + 1):
    numbers.append(i)
print(f'Список элементов от -n до n: \n {numbers}')

array_indexes = input('Enter indexes: ').split(' ')
for i in range(len(array_indexes)):
    array_indexes[i] = int(array_indexes[i])
print(f'Список индексов для умножения: \n {array_indexes}')

product = 1
for i in array_indexes:
    product *= numbers[i]
print(f'Произведение элементов на указанных пользователем через пробел позициях: {product}')
























