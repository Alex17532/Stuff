import numpy
import turtle, random

running = True

wn_names = [". dRaWiNg GaMe °", "° DrAwInG gAmE ."]
colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'gray', 'white']

wn = turtle.Screen()
wn.title("Drawing game")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color(random.choice(colours))

def draw(x, y):
    pen.goto(x, y)

def draw_square():
    for i in range(4):
        pen.forward(100)
        pen.right(90)

def close_window():
    global running
    running = False
    wn._destroy()

def clear_drawing():
    pen.clear()


wn.listen()
wn.onkeypress(draw_square, "s")
wn.onkeypress(clear_drawing, "c")
wn.onkeypress(close_window, "q")

wn.onclick(draw)

while running:
    draw_square()
    pen.color(random.choice(colours))
    pen.seth(random.randint(0, 360))
    wn.title(random.choice(wn_names))

wn.mainloop()