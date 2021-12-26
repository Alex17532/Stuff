import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Zebra Crossing Light")

light1 = turtle.Turtle()
light1.speed(0)
light1.shape("circle")
light1.color("orange")
light1.penup()
light1.goto(50, 0)

light2 = turtle.Turtle()
light2.speed(0)
light2.shape("circle")
light2.color("orange")
light2.penup()
light2.goto(-50, 0)

while True:
    light1.color("yellow")
    time.sleep(1)
    light1.color("orange")

    light2.color("yellow")
    time.sleep(1)
    light2.color("orange")
wn.mainloop()