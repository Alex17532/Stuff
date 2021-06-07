import turtle
import random

pen = turtle.Turtle()

x = pen.xcor()
y = pen.ycor()

for i in range(94):
    x += 10
    y += 10
    pen.seth(random.randint(90, 180))