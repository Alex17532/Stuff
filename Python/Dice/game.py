import tkinter
import random

root = tkinter.Tk()
root.geometry('600x600')
root.title('Roll a dice')
root.configure(bg="midnight blue")

label = tkinter.Label(root, text='', font=('Helvetica', 260))

def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')
    label.pack()

def reset():
    label.configure(text=f'')
    label.pack()

button = tkinter.Button(root, text='Roll', foreground='blue', command=roll_dice)
button.pack()
buttonreset = tkinter.Button(root, text = "Reset", command = reset)
buttonreset.pack()
root.mainloop()