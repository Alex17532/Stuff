import turtle
import random

screen = turtle.Screen()
screen.title("Drawing Game")
screen.bgcolor("black")
screen.tracer()
t = turtle.Turtle()
t.color("white")
t.shape("circle")

def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickright():
    t.clear()

def main():
    screen.listen()
    t.ondrag(dragging)

    screen.onscreenclick(clickright(), 3)

    screen.mainloop()
    screen.update()

main()