from turtle import forward, right, left
from turtle import exitonclick, shape, goto, penup, pendown
from math import sqrt
from random import randint
import random



shape('turtle')
penup()
goto(-400, 0)
pendown()

def draw_house(a):

    c = sqrt(2)*a

    left(90)
    forward(a)
    right(135)
    forward(c)
    left(135)
    forward(a)

    left(90)
    forward(a)
    right(135)
    forward(a/2*sqrt(2))
    right(90)
    forward(a/2*sqrt(2))

    right(90)
    forward(c)
    left(135)
    forward(a)
    

for i in range (10):
    draw_house(random.randint(3, 20))


exitonclick
