import tkinter as t
import random as r

root = t.Tk()
root.title("Rock, Paper, Scissors!")
root.geometry("400x500")
root.configure(bg="teal")

#Translating the computer's choice to Rock, Paper or Scissors
random_number = r.randint(1, 3)
if random_number == 1:
    computer_choice = "R"
elif random_number == 2:
    computer_choice = "P"
elif random_number == 3:
    computer_choice = "S"

# ASCII ART
#Rock
rock_image = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

#Paper
paper_image = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)"""

#Scissors
scissors_image = """
    _______
---'   ____)____
          ______)
       __________)   
      (____)
---.__(___)"""


# Create functions
def rock():
    label_user_choice['text'] = rock_image
    
    # Deal with the choices
    if computer_choice == "R":
        label_result['text'] = "Tie!"
        label_computer_choice['text'] = rock_image
    elif computer_choice == "P":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = paper_image
    elif computer_choice == "S":
        label_result['text'] = "Player wins!"
        label_computer_choice['text'] = scissors_image
    
def paper():
    label_user_choice['text'] = paper_image
    
    # Deal with the choices
    if computer_choice == "P":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = paper_image
    elif computer_choice == "S":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = scissors_image
    elif computer_choice == "R":
        label_result['text'] = "Player wins!"
        label_computer_choice['text'] = rock_image
    
def scissors():
    label_user_choice['text'] = scissors_image
    
    # Deal with the choices
    if computer_choice == "S":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = scissors_image
    elif computer_choice == "R":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = rock_image
    elif computer_choice == "P":
        label_result['text'] = "Player wins!"
        label_computer_choice['text'] = paper_image
    
def reset():
    global computer_choice
    random_number = r.randint(1, 3)
    if random_number == 1:
        computer_choice = "R"
    elif random_number == 2:
        computer_choice = "P"
    elif random_number == 3:
        computer_choice = "S"
        
    label_computer_choice['text'] = ""
    label_user_choice['text'] = ""
    label_result['text'] = "Choose..."


# Create widgets
button_rock = t.Button(root, text="Rock", command = rock)
button_rock.pack()

button_paper = t.Button(root, text="Paper", command = paper)
button_paper.pack()

button_scissors = t.Button(root, text="Scissors", command = scissors)
button_scissors.pack()

label_computer_choice = t.Label(root, justify=t.LEFT, font="Courier", text="")
label_computer_choice.pack()

label_user_choice = t.Label(root, justify=t.LEFT, font="Courier", text="")
label_user_choice.pack()

label_result = t.Label(root, text="Choose...")
label_result.pack()

button_reset = t.Button(root, text="Reset", command = reset)
button_reset.pack()

a = t.Label(root, text="")
a.pack()

label_tips = t.Label(root, text="Yes, The Computer does Play Randomly")
label_tips.pack()

root.mainloop()