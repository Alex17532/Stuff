import numpy, turtle, random
colours = ["yellow", "light green", "light blue"]
seq=["0", "O"]
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
        self.t.pu()
        self.t.speed(0)
        self.t.color("green")
        self.t.shape("circle")
        self.t.pensize(5)
        wn.bgcolor("black")
        screen.bind('<Motion>', self.set_coords)
        screen.bind('Space', self.t.pd())
        self.run()
    def set_coords(self, event):
        print("[", event.x, "] [", event.y, "]")
        self.x = event.x
        self.y = event.y
    def run(self):
        while True:
            self.t.circle(5)
            self.t.seth(random.randint(0, 360))
            self.t.color(random.choice(colours))
            def func(event):
                print(event.x, event.y)
                pen.goto(event.x, event.y)
            self.t.setposition(self.x-300, (self.y*-1)+300)
m = Main()