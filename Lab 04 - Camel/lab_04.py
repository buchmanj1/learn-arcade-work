miles=0
thirst=0
camel=0
natives=-20
canteen=3
player=0
# This is a comment
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
        elif choice.upper == 'E':
            print("Miles traveled:{miles}")
            print("Drinks remaining:{canteen}")
            print("The natives are {natives} miles away.")
main()