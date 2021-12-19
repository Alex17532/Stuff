import turtle, random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A thing that bounces and moves")
wn.setup(800, 600)
wn.tracer(0)

#Object
player = turtle.Turtle()
player.penup()
player.color("white")
player.shape("square")

#Moving
playerspeed = 0
playerupspeed = 0

def move_left():
    global playerspeed
    playerspeed = -2
    
def move_right():
    global playerspeed
    playerspeed = 2

def move_up():
    global playerupspeed
    playerupspeed = 2

def move_down():
    global playerupspeed
    playerupspeed = -2


#Keybinds
wn.listen()
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")




while True:
    wn.update()
    player.setx(player.xcor() + playerspeed)
    player.sety(player.ycor() + playerupspeed)

    if player.ycor() > 290:
        playerupspeed = -1.8

    if player.ycor() < -290:
        playerupspeed = 1.8

    if player.xcor() > 390:
        playerspeed = -1.8

    if player.xcor() < -390:
        playerspeed = 1.8