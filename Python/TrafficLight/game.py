import turtle
import time

wn = turtle.Screen()
wn.title("Traffic Light")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.color("yellow")
pen.speed(0)
pen.ht()
pen.width(3)
pen.pu()
pen.goto(-30, 60)
pen.pd()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

red_light = turtle.Turtle()
red_light.speed(0)
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0, 40)

yellow_light = turtle.Turtle()
yellow_light.speed(0)
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0, 0)

green_light = turtle.Turtle()
green_light.speed(0)
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0, -40)


while True:
    red_light.color("red")
    time.sleep(2)
    red_light.color("grey")

    yellow_light.color("yellow")
    time.sleep(2)
    yellow_light.color("grey")

    green_light.color("green")
    time.sleep(2)
    green_light.color("grey")


wn.mainloop()