from turtle import *
k=20
tracer(0)
screensize (1000,1000)
for i in range(2):
    forward(17*k)
    right(90)
    forward(10*k)
    right(90)
penup ()
forward(7*k)
right(90)
pendown()
for i in range(2):
    forward(20*k)
    right(90)
    forward(14*k)
    right(90)
penup()
for x in range (-50,50):
    for y in range(-50, 50):
        setpos (x*k, y*k)
        dot (5)
done()
