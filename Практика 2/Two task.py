# -*- coding: utf-8 -*-

# Задание номер два-2
def areaOfTriangle():
    print("Введите входные данные (2 числа)")
    firstSide = int(input("Длина первой стороны - "))
    secondSide = int(input("Длина второй стороны - "))
    print("Ответ:")
    return firstSide * secondSide * 0.5

print("Второе задание: ")
print(areaOfTriangle())
print("\n")