import turtle, random

wn = turtle.Screen()
wn.title("")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#66ffff")

def follow_cursor(x, y):
    pen.goto(x, y)

while True:
    

wn.mainloop()