import numpy
import turtle, random
running = True
class Main():
    def __init__(self):
        wn = turtle.Screen()
        wn.setup(600, 600)
        screen = wn.getcanvas()
        self.t = turtle.Turtle()
        self.t.shapesize(stretch_wid=1, stretch_len=1, outline=2)
        self.x = 300
        self.y = 300
        self.t.speed(0)
        self.t.color("green")
        self.t.shape("triangle")
        self.t.setheading(135)
        self.t.pensize(5)
        wn.bgcolor("black")
        screen.bind('<Motion>', self.set_coords)
        self.run()
    def set_coords(self, event):
        print("X: [", event.x, "] Y:[", event.y, "]")
        self.x = event.x
        self.y = event.y
    def run(self):
        while True:
            def func(event):
                print(event.x, event.y)
                pen.goto(event.x, event.y)
            self.t.setposition(self.x-300, (self.y*-1)+300)
m = Main()