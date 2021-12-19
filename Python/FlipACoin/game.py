#flip a coin
import random

faces = ["Heads", "Tails"]

coin_face = random.choice(faces)

y_n = input("Do you wan't to flip a coin? (y/n) > ").upper()

if y_n == "Y":
    print("You flipped a coin... \n")
    print(f"It landed a {coin_face}!")

if y_n == "N":
    pass