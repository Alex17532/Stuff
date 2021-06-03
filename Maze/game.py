import turtle as t
wn = t.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700, 700)
class Pen(t.Turtle):
    def __init__(self):
        t.Turtle.__init__(self)