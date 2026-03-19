# Dice Roller Application

import random

def roll_dice():
    return random.randint(1, 6)

while True:
    choice = input("Roll dice? (y/n): ")
    if choice.lower() == 'y':
        print("You rolled:", roll_dice())
    else:
        break
