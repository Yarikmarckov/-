# -*- coding: utf-8 -*-
# Задание номер два-2
def findDel():
    i = 2
    N = int(input("Введите число больше 2 - "))
    while N % i != 0:
        i += 1
    print(i)
findDel()