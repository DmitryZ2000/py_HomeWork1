# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

from math import sqrt

def distance(aX, aY, bX, bY):
    return round(sqrt((bX - aX)**2 + (bY-aY)**2), 2)

aX = int(input("Введите координату x точки A: "))
aY = int(input("Введите координату y точки A: "))
bX = int(input("Введите координату x точки B: "))
bY = int(input("Введите координату y точки B: "))
print(distance(aX, aY, bX, bY))
