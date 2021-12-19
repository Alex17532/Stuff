import os

os.system("clear")

class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" %s | %s | %s " %(self.cells[0], self.cells[1], self.cells[2]))
        print(" ---------")
        print(" %s | %s | %s " %(self.cells[3], self.cells[4], self.cells[5]))
        print(" ---------")
        print(" %s | %s | %s " %(self.cells[6], self.cells[7], self.cells[8]))

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

board = Board()
board.display()

def print_header():
    print(f"Tic-Tac-Toe!\n")

def refresh_screen():
    os.system("clear")
    print_header()
    board.display()

while True:
    refresh_screen()

    x_choice = int(input("\nX) Choose a number 0 - 8. > "))

    board.update_cell(x_choice, "X")

    refresh_screen()

    o_choice = int(input("\nO) Choose a number 0 - 8. > "))

    board.update_cell(x_choice, "O")