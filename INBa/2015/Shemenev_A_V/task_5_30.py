# Задача 4. Вариант 30.
#Напишите программу, которая бы при запуске случайным образом отображала имя одного из трех племянников Скруджа МакДака.
# Shemenev A.V
# 28.03.16

import random
print("Программа случайным образом отображает имя одного из трех племянников Скруджа МакДака.")
x = int (random.randint(1,3))
print("Имя племянника")
if x == 1:
    print ('Билли')
elif x == 2:
    print ('Вилли')
else:
    print (' Дилли')

input("Для выхода нажмите Enter.")


