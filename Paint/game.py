import tkinter as tk
import random as r
import time as t
  
root = tk.Tk()
root.geometry("400x400")
root.title("Paint!")
root.configure(bg = "white")
frame = tk.Frame(root, height=100, width=100)
  
colours = ["red", "orange", "yellow", "light green", "blue", "violet", "magenta"]

def change_bg():
        frame.config(background = r.choice(colours))
        print("Background changed!")

def reset_bg():
        frame.config(background = "white")
        print("Background reset!")


close_window = input(str("Start? > (Y/N) "))

if close_window == "Y":
        pass

elif close_window == "N":
        root.destroy()

if close_window == "y":
        pass

elif close_window == "n":
        root.destroy()

      
  
button = tk.Button(frame, text="›› Paint ‹‹",command=change_bg)


   
  

button.pack()
frame.pack(fill='both', expand=True)
root.mainloop()