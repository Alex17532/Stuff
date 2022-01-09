import turtle, random, os

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Tennis (sort of sort of not)")
wn.bgpic("/Users/alexanderlongfellow/Desktop/code/Python/Tennis/court.gif")
wn.setup(800, 600)
wn.tracer(0)
wn.register_shape('/Users/alexanderlongfellow/Desktop/code/Python/Tennis/racket.gif')
wn.register_shape('/Users/alexanderlongfellow/Desktop/code/Python/Tennis/racket2.gif')

score_a = 0
score_b = 0

player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("/Users/alexanderlongfellow/Desktop/code/Python/Tennis/racket.gif")
player_a.color("blue")
player_a.pu()
player_a.goto(-350, 0)
player_a.shapesize(stretch_wid=2, stretch_len=1)

player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("/Users/alexanderlongfellow/Desktop/code/Python/Tennis/racket2.gif")
player_b.color("purple")
player_b.pu()
player_b.goto(350, 0)
player_b.shapesize(stretch_wid=2, stretch_len=1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.pu()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

playerspeed = 0
player2speed = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.pu()
pen.ht()
pen.goto(0, 260)
pen.pd()
pen.write("Player A: 0          Player B: 0", align="center", font=("Courier", 24, "normal"))

def player_a_up():
    global playerspeed
    playerspeed = 2

def player_a_down():
    global playerspeed
    playerspeed = -2

def player_b_up():
    global player2speed
    player2speed = 2

def player_b_down():
    global player2speed
    player2speed = -2

wn.listen()
wn.onkeypress(player_a_up, "w")
wn.onkeypress(player_a_down, "s")
wn.onkeypress(player_b_up, "Up")
wn.onkeypress(player_b_down, "Down")

while True:
    wn.update()

    player_a.sety(player_a.ycor() + playerspeed)
    player_b.sety(player_b.ycor() + player2speed)

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}      Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}      Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < player_b.ycor() + 40 and ball.ycor() > player_b.ycor() - 40):
        os.system("afplay /Users/alexanderlongfellow/Desktop/code/Python/Tennis/clap.wav&")
        ball.setx(340)
        ball.dx *= -1.1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < player_a.ycor() + 40 and ball.ycor() > player_a.ycor() - 40):
        os.system("afplay /Users/alexanderlongfellow/Desktop/code/Python/Tennis/clap.wav&")
        ball.setx(-340)
        ball.dx *= -1.1

    # AI
    # if player_b.ycor() < ball.ycor() and abs(player_b.ycor() - ball.ycor()) > 10:
    #     player_b_up()

    # elif player_b.ycor() > ball.ycor() and abs(player_b.ycor() - ball.ycor()) > 10:
    #     player_b_down()