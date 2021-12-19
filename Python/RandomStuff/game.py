import tkinter as tk
import random as r
import time as t

dc = [1, 2, 3, 4, 5, 6]

root = tk.Tk()
root.title(" ")
root.configure(bg="white")
root.geometry("500x600")

colours = ["red", "orange", "yellow", "light green", "blue", "violet", "magenta"]

def change():
    root.title(r.choice(colours))
    root.configure(bg = r.choice(colours))

def reset():
    root.title(" ")
    root.configure(bg="white")

def create_function(input):
    def defenition():
        print(f"`input = {input}`")

def close():
    root.destroy()

def dice():
        root.title(r.choice(dc))

def base():
    root.title("1 2 3 4 5 6 7 8 9 10")

create_function(82.7)

change = tk.Button(root, text="Change the background and title of the window. (random colours)", command = change)
change.pack()

gap = tk.Label(root, text="                                                                                  ")
gap.pack()

reset = tk.Button(root, text="Reset", command = reset)
reset.pack()

gap2 = tk.Label(root, text="                                                                                  ")
gap2.pack()

close = tk.Button(root, text="Close window", command = close)
close.pack()

gap3 = tk.Label(root, text="                                                                                  ")
gap3.pack()

dice = tk.Button(root, text="Roll a dice (changes the window title to a random number from 1 - 6)", command = dice)
dice.pack()

gap4 = tk.Label(root, text="                                                                                  ")
gap4.pack()

base = tk.Button(root, text="Shows the windows name as base 10", command = base)
base.pack()

root.mainloop()

for i in range (75):
    print("-")
    
for i in range(150):
    print("_")
    
for i in range(300):
    print("|")
    
for i in range(600):
    print("+")