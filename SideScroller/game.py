import turtle
import random
colours = ["red", "orange", "yellow", "light green", "blue", "violet", "magenta"]


wn = turtle.Screen()
wn.setup(800, 600)
wn.bgcolor("black")
wn.title("Side-scrolling Shooter")
wn.tracer(0)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("green")
        self.width(2)
        self.speed(0)
        self.setheading(0)

    def health_meter(self):
        if player:
            self.goto(player.xcor() - 20, player.ycor() + 15)
            self.pendown()
            self.fd(40 * (player.health / player.max_health))
            self.penup()
            self.hideturtle()

        if enemies:
            self.goto(enemy.xcor() - 15, enemy.ycor() + 15)
            self.pendown()
            self.fd(30 * (enemy.health / enemy.max_health))
            self.penup()
            self.hideturtle()

    def ammo_counter(self):
        ammo = 0
        for missile in missiles:
            if missile.state == "ready":
                ammo += 1

            for x in range(ammo):
                self.goto(300 + 30 * x, 280)
                self.shape("circle")
                self.stamp()

    def draw_score(self):
        self.goto(-80, 270)
        self.write(f"Score: {player.score}  Kills: {player.kills}", font=("Comic sans", 16, "normal"))
        print(f"Your score is { player.score }")


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("green")
        self.penup()
        self.speed(0)
        self.goto(-350, 0)
        self.dy = 0
        self.dx = 0
        self.score = 0
        self.max_health = 20
        self.health = self.max_health
        self.kills = 0

    def up(self):
        self.dy = 1.75

    def down(self):
        self.dy = -1.75

    def move_left(self):
        self.dx = -1.75

    def move_right(self):
        self.dx = 1.75

    def move(self):
        self.sety(self.ycor() + self.dy)
        self.setx(self.xcor() + self.dx)

        
        if self.ycor() > 280:
            self.sety(280)
            self.dy = 0

        elif self.ycor() < -280:
            self.sety(-280)
            self.dy = 0

        if self.xcor() < -380:
            self.setx(-380)
            self.dx = 0

        elif self.xcor() > -180:
            self.setx(-180)
            self.dx = 0


class Missile(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(0, 1000)
        self.dx = 0
        self.state = "ready"

    def fire(self):
        self.state = "firing"
        self.goto(player.xcor(), player.ycor())
        self.dx = 2.5

    def move(self):
        if self.state == "firing":
            self.setx(self.xcor() + self.dx)

        if self.xcor() > 400:
            self.state = "ready"
            self.sety(1000)


class Enemy(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.color("yellow")
        self.speed(0)
        self.goto(random.randint(400, 480), random.randint(-280, 280))
        self.dx = random.randint(1, 5) / -3
        self.dy = 0
        self.max_health = random.randint(5, 15)
        self.health = self.max_health
        self.type = "enemy"

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        if self.xcor() < -400:
            self.goto(random.randint(400, 480), random.randint(-280, 280))

        if self.ycor() < -280:
            self.sety(-280)
            self.dy *= -1

        elif self.ycor() > 280:
            self.sety(280)
            self.dy *= -1

    def boss_spawn(self):
        self.shape("square")
        self.color("red")
        self.max_health = 50
        self.health = self.max_health
        self.dy = random.randint(-5, 5) / 3

    def enemy_respawn(self):
        self.dy = 0
        self.shape("square")
        self.color("yellow")
        self.max_health = random.randint(5, 15)
        self.health = self.max_health


class Star(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        star_images = ["circle", "square", "triangle"]
        self.color(random.choice(colours))
        self.shape(random.choice(star_images))
        self.penup()
        self.speed(0)
        self.goto(random.randint(-400, 400), random.randint(-290, 290))
        self.dx = random.randint(1, 5) / -20

    def move(self):
        self.setx(self.xcor() + self.dx)

        if self.xcor() < -400:
            self.goto(random.randint(400, 480), random.randint(-290, 290))


pen = Pen()
player = Player()
missiles = [Missile(), Missile(), Missile(), Missile(), Missile()]

enemies = []
for _ in range(5):
    enemies.append(Enemy())

stars = []
for _ in range(30):
    stars.append(Star())


def fire_missile():
    for missile in missiles:
        if missile.state == "ready":
            missile.fire()
            break


def quit_game():
    global running
    running = False


wn.listen()
wn.onkeypress(quit_game, "q")
wn.onkeypress(quit_game, "Q")
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")
wn.onkeypress(fire_missile, "space")

running = True
while running:
    player.setheading(random.randint(0, 360))
    wn.update()
    pen.clear()

    player.move()

    for missile in missiles:
        missile.move()

    for star in stars:
        star.move()

    for enemy in enemies:
        enemy.move()

        pen.health_meter()

        pen.ammo_counter()

        for missile in missiles:
            if enemy.distance(missile) < 20:
                enemy.health -= 4
                if enemy.health <= 0:
                    enemy.goto(random.randint(400, 480), random.randint(-280, 280))

                    player.kills += 1
                    if player.kills % 10 == 0:
                        enemy.boss_spawn()
                    else:
                        enemy.enemy_respawn()

                else:
                    enemy.setx(enemy.xcor() + 20)

                missile.dx = 0
                missile.goto(0, 1000)
                missile.state = "ready"

                player.score += 10

        if enemy.distance(player) < 20:
            player.health -= random.randint(5, 10)
            enemy.health -= random.randint(5, 10)
            enemy.goto(random.randint(400, 480), random.randint(-280, 280))

            if player.health <= 0:
                print("yuo ded gaem oevr")
                exit()

    pen.draw_score()