# -*- coding: utf-8 -*-
# Задание номер три-3 
def powFinder():
    i = 2
    powContainer = 2
    counter = 1
    N = int(input("Введите число - "))

    while powContainer * i < N:
        powContainer *= i
        counter+=1
    print(powContainer)
    print(counter)

powFinder()