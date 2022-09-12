# Реализуйте алгоритм перемешивания списка.

import random 

my_list = [1, 5, 3, 4, 7, 6]
print(f'Исходный список: {my_list}')
random.shuffle(my_list)
print(my_list)
def shuffle1(my_list):

    new_list = list(range(len(my_list)))
    for i in range(len(my_list)):
        rand_i = random.randint(0, len(my_list) - 1)
        temp = my_list[rand_i]
        my_list[rand_i] = my_list[i]
        my_list[i] = temp
    return my_list
print(f' Перемешанный список: {shuffle1(my_list)}')

# Или так:
# random.shuffle(my_list)
# print(f'Перемешанный список: {my_list}')


