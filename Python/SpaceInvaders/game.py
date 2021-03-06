import turtle
import os
import math
import random

# set up the screen
window = turtle.Screen()
window.bgcolor("black")
window.bgpic("/Users/alexanderlongfellow/Desktop/Stuff/SpaceInvaders/space_invaders_background.gif")
window.title("Space Invaders")
window.setup(width=700, height=700)

turtle.register_shape("/Users/alexanderlongfellow/Desktop/Stuff/SpaceInvaders/invader.gif")
turtle.register_shape("/Users/alexanderlongfellow/Desktop/Stuff/SpaceInvaders/player.gif")

# draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.down()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("/Users/alexanderlongfellow/Desktop/Stuff/SpaceInvaders/player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 0

# choose number of enemies
number_of_enemies = 5
# create an empty list of enemies
enemies = []

# add enemies to the list
for i in range(number_of_enemies):
    # create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("/Users/alexanderlongfellow/Desktop/Stuff/SpaceInvaders/invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.pu()
score_pen.goto(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.ht()

# player weapon
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# define bullet state
# ready - ready to fire
# fire - firing
bulletstate = "ready" 


# move the player left and right
def move_left():
    global playerspeed
    playerspeed = -5
    
def move_right():
    global playerspeed
    playerspeed = 5

def fire_bullet():
    # declare bullet as a global if it needs changed
    
    global bulletstate
    if bulletstate == "ready":
        os.system("afplay /Users/alexanderlongfellow/Desktop/Stuff/SpaceInvaders/laser.wav&")
        bulletstate = "fire"
        
        # move the bullet to just above player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
    
# create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# main game loop
while True:
    player.setx(player.xcor() + playerspeed)
    
    for enemy in enemies:
        # move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # move the enemy back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y) 
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        for enemy in enemies:
            if isCollision(bullet, enemy):
                os.system("afplay /Users/alexanderlongfellow/Desktop/Stuff/SpaceInvaders/explosion.wav&")
                # reset bullet
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0, -400)
                # reset enemy
                enemy.setposition(-200, 250)
                score += 10
                score_pen.clear()
                scorestring = "Score: %s" %score
                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

            if isCollision(player, enemy):
                os.system("afplay /Users/alexanderlongfellow/Desktop/Stuff/SpaceInvaders/explosion.wav&")
                player.hideturtle()
                enemy.hideturtle()
                print("game over")
                break

    # move the bullet
    if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

    # check to see if bullet has reached top
    if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"