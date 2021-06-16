import tkinter
import random

computer_guess = random.randint(1, 10)

root = tkinter.Tk()
root.title("Guessing Game")
root.configure(bg="grey")


def check():
    user_guess = int(txt_guess.get())
    if user_guess < computer_guess:
        msg = "Higher!"
    elif user_guess > computer_guess:
        msg = "Lower!"
    elif user_guess == computer_guess:
        msg = "Correct!"
    else:
        msg = "Something went wrong..."
    
    lbl_result["text"] = msg

    txt_guess.delete(0, 49484746)

def reset():
    global computer_guess
    computer_guess = random.randint(1, 10)
    lbl_result["text"] = "Game reset. Guess again!"

lbl_title = tkinter.Label(root, text="Welcome to the guessing game!", bg="grey", fg="white")
lbl_title.pack()

lbl_result = tkinter.Label(root, text="Good Luck!", bg="grey", fg="white")
lbl_result.pack()

btn_check = tkinter.Button(root, text="Check", fg="green", command = check, bg="grey", relief="raised")
btn_check.pack(side="left")

btn_reset = tkinter.Button(root, text="Reset", fg="red", command = reset, bg="grey", relief="raised")
btn_reset.pack(side="right")

txt_guess = tkinter.Entry(root, width=3, bg="grey", fg="white")
txt_guess.pack()


root.mainloop()