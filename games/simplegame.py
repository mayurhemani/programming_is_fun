import random
import sys

current_position = 0

def clear_screen():
    for _ in range(80):
        print(" ")

def show_graphics(n_spaces, n_stars):
    print(" " * n_spaces + "*" * n_stars)
    #sys.stdout.flush()

def game_state(action):
    global current_position
    current_position = current_position + action
    n_stars = 9
    for i in range(5):
        n_spaces = 5 - i + current_position
        n_stars = 2*i - 1
        show_graphics(n_spaces, n_stars)
        
        
def do_action(left_or_right):
    if left_or_right == "left":
        game_state(-1)
    elif left_or_right == "right":
        game_state(1)
    else:
        game_state(0)
      
for clock in range(10000000):
    x = input(' ')
    clear_screen()
    if x == 'a':
        do_action("left")
    elif x == 'b':
        do_action("right")
    else:
        do_action(None)
    
