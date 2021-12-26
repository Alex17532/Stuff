import turtle
import random

wn = turtle.Screen()
wn.title('Bouncing Shape Simulator')
wn.bgcolor("black")
wn.tracer(0)

balls = []

for i in range(25):
    balls.append(turtle.Turtle())

colours = ["red", "blue", "yellow", "orange", "green", "white", "purple"]
shapes = ["circle", "triangle", "square"]

for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colours))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    ball.dy = -2
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)

gravity = 0.1 

while True:
    wn.update()

    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        
        ball.setx(ball.xcor() + ball.dx)

        # Check for a bounce
        if ball.ycor() < -300:
            ball.dy *= -1
            ball.da *= -1

        if ball.xcor() > 290:
            ball.dx *= -1
            ball.da *= -1

        if ball.xcor() < -290:
            ball.dx *= -1
            ball.da *= -1
    
    # Check for a collision between the balls
    for i in range(0, len(balls)):
        for j in range(i+1, len(balls)):
            # Check for a collision
            if balls[i].distance(balls[j]) < 20:
                temp_dx = balls[i].dx
                temp_dy = balls[i].dy

                balls[i].dx = balls[j].dx
                balls[i].dy = balls[j].dy

                balls[j].dx = temp_dx
                balls[j].dy = temp_dy


                balls[i].color(random.choice(colours))
                balls[j].color(random.choice(colours))


wn.mainloop()