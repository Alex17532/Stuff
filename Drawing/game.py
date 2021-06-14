import numpy
import turtle, random

running = True

wn_name = ["Drawing Game"]
colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'gray', 'white']
# colours2 = ["red", "green", "blue"]
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
        print(event.x, event.y)
        self.x = event.x
        self.y = event.y
    def run(self):
        while True:
            self.t.left(60)
            def func(event):
                print(event.x, event.y)
                pen.goto(event.x, event.y)
            self.t.pensize(5)
            self.t.shape("triangle")
            self.t.color(random.choice(colours))
            self.t.setposition(self.x-300, (self.y*-1)+300)
m = Main()