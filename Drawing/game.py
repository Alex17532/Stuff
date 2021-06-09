import turtle, random

wn_names = [". dRaWiNg GaMe °", "° DrAwInG gAmE ."]

wn = turtle.Screen()
wn.title("Drawing game")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#66ffff")

def follow_cursor(x, y):
    pen.goto(x, y)

wn.onclick(follow_cursor)

while True:
    pen.seth(random.randint(0, 360))
    wn.title(random.choice(wn_names))

wn.mainloop()