#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
count = 0    #счетчик попыток
number = np.random.randint(1, 101)    #загаданное число
print('Загадано число от 1 до 100')

def game_core_v3(number):
    #Создаем функцию для поиска числа (input - число, output - количество попыток)
    num_list = [i for i in range(1, 101)]
    #Создаем список с элементами
    min_num = num_list[0] #Наименьший элемент списка
    max_num = num_list[-1] #Наибольший элемент списка
    count = 0
    while min_num <= max_num: #цикл, повторяющийся пока наименьший и наибольший элементы не совпадут
        count += 1
        avg_num = (min_num + max_num)//2  #средний элемент списка
        if avg_num > number:
            max_num = avg_num - 1 #если загаданное число меньше среднего элемента списка, средний элемент становится наибольшим
        elif avg_num < number:
            min_num = avg_num + 1 #если загаданное число больше среднего элемента списка, средний элемент становится наименьшим
        else:
            break #если равно выходим
    return(count)

print('Вы угадали число {} за {} попыток.'.format(number, game_core_v3(count)))


# In[ ]:




