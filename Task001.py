# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
a = int(input("Веедите целое число от 1 до 7: "))
if a < 1 or a > 7 : print("Вы ввели не верное число")
elif a == 6  or a == 7: print(a, " - это рабочий день")
else: print(a, " - это рабочий день")