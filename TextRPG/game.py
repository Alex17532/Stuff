print(f"Welcome to the text based RPG.")
continue_yes_or_no = input("Would you like to continue? (Y/N) ")

if continue_yes_or_no == "N":
    exit()

if continue_yes_or_no == "Y":
    name = input("What is your name? > ")
    print(f"Hello, {name}!\n")

    tarantula = input(("You have a basic sword and shield. You come across a tarantula, what do you do? > (Fight/Run) "))

    if tarantula == "Fight":
        print(f"You hid the tarantula with your sword but it climbed up your sword and but you, you died!\n")
        exit()

    if tarantula == "Run":
        print(f"You ran from the tarantula, it chased you for a couple of minutes until it gave up.\n")

    poison_water = input("You are thirsty after running for minutes away from a tarantula. You see a stream with muddy water in it, what do you do? > (Drink/Leave) ")
    if poison_water == "Drink":
        print(f"Too bad, the water poisoned you and you died!")
        exit()
    if poison_water == "Leave":
        print(f"You leave the chance of drinking muddy water, an old lady sees you and offers you water, you say yes and drink it. You're not thirsty anymore! \n")

    rabbit = input("You see a rabbit, you are hungry. What do you do? > (Kill/Ignore) ")

    if rabbit == "Kill":
        print(f"You kill the rabbit and cook it over a fire, you enjoy it as the sun goes down. You are not hungry anymore!\n")

    if rabbit == "Ignore":
        print(f"You ignore the rabbit and carry on walking, you feel very hungry and you cant find any food. You die of starvation!\n")
        exit()

    dove = input("You see a dove, it looks like it's flying somewhere, do you follow it? > (Y/N) ")
    
    if dove == "Y":
        print(f"You follow the dove and it takes you to your house, the place you've been looking for this whole time!\n")
        bossfight = input("This is an event for winners, would you like to take part in a boss fight? > (Y/N) ")
        if bossfight == "Y":
            fight = input("Do you hit the boss or stand back? > (Hit/Stand) ")
            if fight == "Hit":
                print(f"Success! You hit the boss by 13 HP. The boss now has 87/100 HP!\n")

            if fight == "Stand":
                print(f"The boss swoops down and grabs you, you try to escape but you get killed!\n")

            fight2 = input("Do you hit the boss or stand back? > (Hit/Stand) ")

            if fight2 == "Hit":
                print(f"Success! You hit the boss in it's weakspot by 87 HP. The boss now has 0/100 HP!\n")
                print(f"You killed the boss!")
                print(f"Good job {name}, you earned yourself the EPIC ending!")

            if fight2 == "Stand":
                print(f"The boss swoops down and grabs you, you try to escape but you get killed!\n")

            if bossfight == "N":
                print(f"You chose not to take part in the event (it doesn't matter if you did or didn't).\n")
                print(f"Well done {name}, you earned yourself the Good ending!")
                exit()

    if dove == "N":
        print(f"You chose not to follow the dove, you get lost and cant find any food or water, you die!\n")
        print(f"Next time think more {name}, you earned yourself the Bad ending!")
        exit()