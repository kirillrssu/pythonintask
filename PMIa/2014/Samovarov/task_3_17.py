﻿#Задача №3, Вариант 7
#Напишите программу, которая выводит имя "Симона Руссель", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

#Samovarov K.
#25.05.2016

print("Герой нашей сегодняшней программы - Симона Руссель")
psev=input("Под каким же именем мы знаем этого человека? Ваш ответ:")
if (psev)==("Мишель Морган"):
	print ("Все верно: Симона Руссель - "+psev)
else:
	print("Вы ошиблись, это не его псевдоним.")
input(" Нажмите Enter для выхода")