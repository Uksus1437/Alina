'''Черепахе был дан для исполнения следующий алгоритм:

Повтори 2 [Повтори 2 [Вперёд 180 Направо 120] Направо 120]

Направо 150 Вперёд 15 Направо 90 Вперёд 360 Направо 90 Вперёд 15

Направо 30 Вперёд 74

Определите периметр фигуры, полученной в результате выполнения алгоритма.'''

from turtle import *
k = 1
# tracer(0)
for i in range(2):
    for j in range(2):
        forward(180*k)
        right(120)
    right(120)
right(150)
forward(15*k)
right(90)
forward(360*k)
right(90)
forward(15*k)
right(30)
forward(74*k)

penup()

# for x in range(-50, 50):
#     for y in range(-50, 50):
#         setpos(x*k, y*k)
#         dot(3)

done()

