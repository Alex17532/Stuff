import turtle, random

wn_names = [". dRaWiNg GaMe *", "* DrAwInG gAmE ."]
colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'gray', 'white']

wn = turtle.Screen()
wn.title("Drawing game")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#66ffff")

def draw(x, y):
    pen.goto(x, y)

def draw_shape():
    for i in range(4):
        pen.forward(100)
        pen.right(90)

wn.listen()
wn.onkeypress(draw_shape, "q")

wn.onclick(draw)

#sshd-keygen-wrapper
while True:
    draw_shape()
    pen.color(random.choice(colours))
    pen.seth(random.randint(0, 360))
    wn.title(random.choice(wn_names))

wn.mainloop()