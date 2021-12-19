# ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
# ◊|\\Snake Game\\|◊
# ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
import os
import turtle as t
import time
import random as r


delay = 0.0668
colours = ["red", "orange", "yellow", "light green", "blue", "violet", "magenta"]
score = 0
high_score = 0

wn = t.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

head = t.Turtle()
head.speed(0)
head.shape("square")
head.penup()
head.color("white")
head.goto(0, 0)
head.direction = "stop"

food = t.Turtle()
food.speed(0)
food.shape("circle")
food.penup()
food.color("white")
food.goto(r.randint(-290, 290), r.randint(-290, 290))

pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.ht()
pen.goto(0, 260)
pen.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))

segments = []

def quit():
    global running
    running = False
    wn._destroy()

def go_up():
    if head.direction != "down":    
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)


    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(quit, "q")
wn.onkeypress(quit, "Q")

running = True

while running:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < - 290:
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "stop"
        score = 0
        pen.clear()
        pen.write(f"Score: { score }    High Score: { high_score }", align="center", font=("Courier", 24, "normal"))

        for segment in segments:
            segment.goto(1000, 1000)
        
        segments.clear()

    if head.distance(food) < 20:
        x = r.randint(-290, 290)
        y = r.randint(-290, 290)
        food.goto(x, y)

        new_segment = t.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        score += 1
        pen.clear()
        if score > high_score:
            high_score = score

        for segment in segments:
            segment.color("white")
            head.color("white")

        pen.write(f"Score: { score }    High Score: { high_score }", align="center", font=("Courier", 24, "normal"))


    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction == "stop"
            score = 0
            pen.clear()
            pen.write(f"Score: { score }    High Score: { high_score }", align="center", font=("Courier", 24, "normal"))

            for segment in segments:
                segment.goto(1000, 1000)
        
            segments.clear()

    time.sleep(delay)

wn.mainloop()