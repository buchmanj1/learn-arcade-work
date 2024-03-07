#Game Variables
thirst=0
camel=0
natives=-20
canteen=3
player=0
DESERT_SIZE = 200

import random
#Game Functions
def move_natives(min_val, max_val):
    global natives
    natives += random.randint(min_val, max_val)
def rest_for_the_night():
    global camel
    print("You've stopped for the night.  Your camel lays down by your fire and is fully rested.")
    camel = 0
    move_natives(7,14)
def move_player(min_val, max_val):
    global player
    random_val = random.randint(min_val, max_val)
    player += random_val
def go_full_speed():
    global thirst, camel
    move_player(10, 20)
    thirst += 1
    camel += random.randint(1, 3)
    move_natives(7, 14)
    print(f"You have traveled {player} miles.")
def go_moderate_speed():
    global thirst, camel
    move_player(5, 12)
    thirst += 1
    camel += 1
    move_natives(7, 14)
    print(f"You have traveled {player} miles.")
def drink_from_canteen():
    global canteen, thirst
    if canteen > 0:
        canteen -= 1
        thirst = 0
    else:
        print("Oh No! Your canteen is empty!")

#Main Game
def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.")
    done=False
    while not done:
        print("""A. Drink from your canteen.\nB. Ahead moderate speed.\nC. Ahead full speed.\nD. Stop for the night.\nE. Status check.\nQ. Quit.""")
        choice = input("What is your choice? ")
        if choice.upper() == 'Q':
            done=True
            print("Thanks for playing!")
        elif choice.upper() == 'E':
            print(f"Miles traveled: {player}")
            print(f"Drinks remaining: {canteen}")
            print(f"The natives are {natives} miles away.")
        elif choice.upper() == 'D':
            rest_for_the_night()
        elif choice.upper() == 'C':
            go_full_speed()
        elif choice.upper() == 'B':
            go_moderate_speed()
        elif choice.upper() == 'A':
            drink_from_canteen()
    #Game Check
    if thirst>=6:
        done=True
        print("You've died of thirst!")
    elif thirst>4:
        print("You are thirst.")
    if camel>=8:
        done=True
        print("Your camel is dead.")
    if camel>=5:
        print("Your camel is getting tired.")
    if natives>=player:
        done=True
        print("The natives have caught you!")
    elif(natives-player)<15:
        print("The natives are getting close!")
    if player>200:
        done=True
        print("You've made it across the desert!  You won!")

main()