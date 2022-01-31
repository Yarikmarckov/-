# -- coding: utf-8 --

""" 
 Задание номер три-3
"""

# Анализатор возраста и имени абитуриента
def ageAndNameAnalysis(age, name):
    if age < 16:
        print("Сначала нужно окончить школу!")
        print("Осталось учиться в школе: " + str(16-age) + " лет / год / года.")
    else:
        print("Поздравляем Вы поступили в ВГУИТ!")

    if age >> 0 and age < 75:
        print("Возраст " + str(age) + " больше 0 и меньше 75.")
    else:
        print("Возраст " + str(age) + " не больше 0 и не меньше 75.")

    if name != "Иван":
        print("Имя " + str(name) + " != Иван.")
    else:
        print("Имя " + str(name) + " == Иван.")

try:
    age = int(input("Введите возраст: "))
    name = input("Введите имя: ")
    ageAndNameAnalysis(age, name)
except ValueError:
    print("Critical error! Exception has occurred: ValueError!")