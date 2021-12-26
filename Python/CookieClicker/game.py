# [|\\]__Cookie Clicker__[\\|]
# Win by getting 1000 clicks
# Press 'Space' to SUPER click (7 clicks in one)
# Press 'O' to EPIC click (50 clicks in one).
# Press 'R' to reset your score.
# Press 'Q' to quit.
# When you reach 10000 (10k) clicks
# The terminal will print "YOU WIN!" 10 times
# And the Window will close after 1 second.
# Have fun!

import turtle
import time

wn = turtle.Screen()
wn.title("Cookie Clicker")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

wn.register_shape("/Users/alexanderlongfellow/Desktop/Stuff/CookieClicker/cookie.gif")

cookie = turtle.Turtle()
cookie.shape("/Users/alexanderlongfellow/Desktop/Stuff/CookieClicker/cookie.gif")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 250)
pen.write(f"Clicks: { clicks }", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: { clicks }", align="center", font=("Courier New", 32, "normal"))
    print(f"{ clicks }")

def SUPER_CLICK():
    global clicks
    clicks += 7
    pen.clear()
    pen.write(f"Clicks: { clicks }", align="center", font=("Courier New", 32, "normal"))
    print(f"{ clicks }")

def reset():
    global clicks
    clicks = 0
    pen.clear()
    pen.write(f"Clicks: { clicks }", align="center", font=("Courier New", 32, "normal"))
    print(f"{ clicks }")

def EPIC_CLICK():
    global clicks
    clicks += 20
    pen.clear()
    pen.color("white")
    pen.write(f"Clicks: { clicks }", align="center", font=("Courier New", 32, "normal"))
    print(f"{ clicks }")
    wn.bgcolor("black")

def quit():
    global running
    running = False


wn.listen()
wn.onkeypress(SUPER_CLICK, "space")
wn.onkeypress(reset, "r")
wn.onkeypress(reset, "R") # If Caps Lock is on
wn.onkeypress(EPIC_CLICK, "o")
wn.onkeypress(EPIC_CLICK, "O") # If Caps Lock is on
wn.onkeypress(quit, "q")
wn.onkeypress(quit, "Q")

running = True

    
while running:
    wn.update()
    
    cookie.onclick(clicked)

    if clicks >= 10000:
        for i in range(10):
            print("YOU WIN!")
        time.sleep(1)
        wn.bye() # Closes the Window because the 'Break' Command doesn't compile with programs using a window