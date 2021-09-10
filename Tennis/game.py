import turtle, random, os

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Tennis (sort of sort of not)")
wn.bgpic("/Users/alexanderlongfellow/Desktop/code/Tennis/court.gif")
wn.setup(800, 600)
wn.tracer(0)

player = "/Users/alexanderlongfellow/Desktop/code/Tennis/invader.gif"

score_a = 0
score_b = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.pu()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=2, stretch_len=1)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.pu()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=2, stretch_len=1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("light green")
ball.pu()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

playerspeed = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.pu()
pen.ht()
pen.goto(0, 260)
pen.pd()
pen.write("Player A: 0      Bot: 0", align="center", font=("Courier", 24, "normal"))

def paddle_a_up():
    global playerspeed
    playerspeed = 1

def paddle_a_down():
    global playerspeed
    playerspeed = -1

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()

    paddle_a.sety(paddle_a.ycor() + playerspeed)

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


    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_up()

    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_down()