import numpy
import turtle, random
running = True
wn_name = ["Drawing Game - Spin Speed Maxed Out"]
colours = ["red", "orange", "yellow", "green", "blue", "magenta", "violet"]
colours2 = ["red", "orange", "yellow"]
shapes = ["square", "arrow", "circle", "turtle", "triangle", "classic"]
class Main():
    def __init__(self):
        wn = turtle.Screen()
        wn.setup(600, 600)
        screen = wn.getcanvas()
        self.t = turtle.Turtle()
        self.t.shapesize(stretch_wid=1, stretch_len=1, outline=5)
        self.x = 300
        self.y = 300
        self.t.speed(0)
        wn.bgcolor("black")
        wn.title(random.choice(wn_name))
        screen.bind('<Motion>', self.set_coords)
        self.run()
    def set_coords(self, event):
        print("X:", event.x, "Y:", event.y)
        self.x = event.x
        self.y = event.y
    def run(self):
        while True:
            self.t.left(540540540540540)
            # self.t.home()
            # self.t.forward(190)
            self.t.circle(10)
            def func(event):
                print(event.x, event.y)
                pen.goto(event.x, event.y)
            self.t.pensize(5)
            self.t.shape("triangle")
            self.t.color(random.choice(colours2))
            self.t.setposition(self.x-300, (self.y*-1)+300)
m = Main()