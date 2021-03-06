import turtle, random

titles = ["Box", "bOx"]
colours = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]

#Window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Box")
wn.tracer(0)

#Player
player = turtle.Turtle()
player.shape("square")
player.color("white")
player.speed(0)

#Functions
def move_u():
    y = player.ycor() + 50
    player.sety(y)

def move_d():
    y = player.ycor() - 50
    player.sety(y)

def move_l():
    x = player.xcor() - 50
    player.setx(x)

def move_r():
    x = player.xcor() + 50
    player.setx(x)

#Keybinds
wn.listen()
wn.onkeypress(move_u, "Up")
wn.onkeypress(move_d, "Down")
wn.onkeypress(move_l, "Left")
wn.onkeypress(move_r, "Right")

#Main game loop
while True:
    player.circle(5)
    player.color(random.choice(colours))
    player.seth(random.randint(0, 360))
    wn.title(random.choice(titles))
    wn.update()

wn.mainloop()