import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Analogue Clock")
wn.tracer(0)

pen = turtle.Turtle()
pen.ht()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s, pen):
    pen.pu()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("grey")
    pen.pd()
    pen.circle(210)

    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pd()
        pen.fd(20)
        pen.pu()
        pen.goto(0, 0)
        pen.rt(30)

    pen.pu()
    pen.goto(0, 0)
    pen.color("grey")
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pd()
    pen.fd(100)
    
    pen.pu()
    pen.goto(0, 0)
    pen.color("grey")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pd()
    pen.fd(125)
    
    pen.pu()
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pd()
    pen.fd(150)

while True:

    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%s"))

    draw_clock(h, m, s, pen)
    wn.update()

    time.sleep(1)

    pen.clear()

wn.mainloop()