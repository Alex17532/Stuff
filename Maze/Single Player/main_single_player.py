import ursina
from start_menu import *

app = Ursina()


ursina.Text.default_font = 'consola.ttf'
ursina.Text.size = 0.03

start_game()

app.run()