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


#