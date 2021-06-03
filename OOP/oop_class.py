import os as __

def _():
    __.system("afplay /Users/alexanderlongfellow/Desktop/Stuff/SpaceInvaders/explosion.wav&")
#__()

class Person():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""

bob = Person()
bob.name = "Bob"
bob.age = 41
bob.gender = "male"

sue = Person()
sue.name = "Sue"
sue.age = 17
sue.gender = "female"

jason = Person()
jason.name = "Jason"
jason.age = 46
jason.gender = "male"

print(f"{bob.name} is {bob.age} years old and is {bob.gender}.")
print(f"{sue.name} is {sue.age} years old and is {sue.gender}.")
print(f"{jason.name} is {jason.age} years old and is {jason.gender}.")