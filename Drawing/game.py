import turtle, random

wn = turtle.Screen()
wn.title("")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#66ffff")

while True:
    pen.forward(10)
    pen.seth(random.randint(1, 360))

wn.mainloop()