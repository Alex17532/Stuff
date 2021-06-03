# |\\Falling Skies\\|
import turtle
import random
import time as t

score = 0
lives = 3

shapes = ["/Users/alexanderlongfellow/Desktop/Stuff/FallingSkies/background.gif", "/Users/alexanderlongfellow/Desktop/Stuff/FallingSkies/deer.gif", "/Users/alexanderlongfellow/Desktop/Stuff/FallingSkies/hunter.gif", "/Users/alexanderlongfellow/Desktop/Stuff/FallingSkies/nut.gif"]

wn = turtle.Screen()
wn.title("Falling Skies")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

# Player
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("square")
player.color("white")
player.goto(0, -250)
player.direction = ""

good_guys = []

for _ in range(20):
    # Good Guy
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.penup()
    good_guy.shape("circle")
    good_guy.color("blue")
    good_guy.goto(-100, 250)
    good_guy.speed = random.randint(1, 4)
    good_guys.append(good_guy)

bad_guys = []

for _ in range(20):
    # Bad Guy
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.penup()
    bad_guy.shape("circle")
    bad_guy.color("red")
    bad_guy.goto(100, 250)
    bad_guy.speed = random.randint(1, 4)
    bad_guys.append(bad_guy)


pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.ht()
pen.shape("square")
pen.color("white")
pen.goto(0, 250)
pen.write(f"Score: { score }  Lives: { lives }", align="center", font=("Courier New", 24, "normal"))

# Functions
def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"

def quit():
    global running
    running = False

# Keybinds
wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_left, "A")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_right, "D")
wn.onkeypress(quit, "q")
wn.onkeypress(quit, "Q")

running = True

while running:
    wn.update()
    # Move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 1
        player.setx(x)

    if lives == 0:
        if lives >= 0:
            print(f"Your final score was { score }")
        t.sleep(0.6)
        quit()
        print(f"Your final score was { score }")

    if player.direction == "right":
        x = player.xcor()
        x += 1
        player.setx(x)

    # Move the good guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)

        # Check if off the screen
        if y < -300:
            x = random.randint(-390, 390)
            y = random.randint(300, 400)
            good_guy.goto(x, y)

        # Check for a collision with the player
        if good_guy.distance(player) < 20:
            x = random.randint(-390, 390)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write(f"Score: { score }  Lives: { lives }", align="center", font=("Courier New", 24, "normal"))

     # Move the bad guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)

        # Check if off the screen
        if y < -300:
            x = random.randint(-390, 390)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)

        # Check for a collision with the player
        if bad_guy.distance(player) < 20:
            x = random.randint(-390, 390)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            lives -= 1
            score -= 10
            pen.clear()
            pen.write(f"Score: { score }  Lives: { lives }", align="center", font=("Courier New", 24, "normal"))
