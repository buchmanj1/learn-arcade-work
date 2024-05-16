import random


# Game Functions
def intro():
    # Starts the game
    print(
        "You are part of an elite counter terrorism task force, responsible for bringing down some of the most "
        "dangerous people in the world.")
    print("For weeks now, you have been tracking an unidentified target.")
    print("All you know is that whoever this individual is, dozens of terrorist attacks can be traced back to them.")
    print(
        "For a moment you finally had them cornered. However, right before your team could apprehend them, "
        "the got away.")
    print("You followed them into a hidden underground bunker. You've seen something like this before.")
    print("There is a locked door on the far end of this dark room.")

    input("Press any button to continue")

    print("")
    print("A prerecorded voice begins to fill the room.")
    print("Dear Failed Agent,")

    print("You may have tracked me here, but you will never catch me now. ")
    print("I wish you the best of luck with your failure. ")
    print("That's when you notice a lock on the dor with three numbers. "
          "He may have escaped but he doesn't have to get away. "
          "The clues to open it could be in this room.")
    print("")
    print("You examine the room and see:")


# Function which builds a menu which will be called later
def menu(list, questions):
    # Function which builds a menu which will be called later
    for item in list:
        print(list.index(item), item)

    result = input(questions)

    try:

        result = int(result)

    except:

        print("Selection must be a whole number between 0-9")

    return result


def door(code):
    # Wound up following a tutorial and using try and break to simplify the overall
    # code https://www.geeksforgeeks.org/python-try-except/ and https://www.geeksforgeeks.org/python-try-except/.
    # This helped solve the issue of the game not ending.  Used return instead of true, so it was easier to send the
    # loop back to the caller code
    # https://realpython.com/python-return-statement/#:~:text=You%20can%20use%20the%20return,further%20computation%20in%20your%20programs.
    print("You walk to the door. The rotary padlock contains three digits. You enter a code")

    while True:

        try:

            option1 = int(input("Digit one: "))

            break

        except:

            print("Digit one must be a whole number between 0-9:")

    while True:

        try:

            option2 = int(input("Digit two: "))

            break

        except:

            print("Digit two must be a whole number between 0-9:")

    while True:

        try:

            option3 = int(input("Digit three: "))

            break

        except:

            print("Digit three must be a whole number between 0-9:")

    chosenCode = int(str(option1) + str(option2) + str(option3))

    print("")

    if chosenCode == code:

        print("As the door clicks open you see him cowering in the corner. You take out your cuffs, a smile"
              "spreading across your face as your team moves in.  The good guys won today.")

        return 1

    else:

        print("You jiggle the padlock, but to no avail. The code is incorrect.")

        return 0


def window(choice, codeLocation, codeValue):
    print("")
    print("You look at the window. It's dark, and damp. "
          "Mold grows along the edges and you cannot see through its musty panes.")

    if choice == codeLocation:
        print("Carved into the edging, you see the number " + str(codeValue) + ".")

        print("")

    else:

        print("You find no code.")

        print("")


def briefcase(choice, codeLocation, codeValue):
    print("")

    print("The backpack was on the suspects back during the chase.  Maybe it still contains intel.")

    if choice == codeLocation:
        print("Within the front pocket, you see the number " + str(codeValue) + " written on a crumpled note.")

        print("")

    else:

        print("You find no code.")

        print("")


def ashtray(choice, codeLocation, codeValue):
    print("")

    print("A cracked ash tray holds the remains of a cigar.")

    if choice == codeLocation:

        print("On the base, you see the number " + str(codeValue) + ".")

    else:

        print("You find no code.")

        print("")


def bucket(choice, codeLocation, codeValue):
    print("")

    print("The bucket sits in the middle of the floor. It seems to "
          "hold "
          "bullet casings")

    if choice == codeLocation:

        print("Within, you see exactly " + str(codeValue) + " stones.")

        print("")

    else:

        print("You find no code.")

        print("")


def painting(choice, codeLocation, codeValue):
    print("")

    print("A gruesome scene depicting atrocities this monster has committed. "
          "This fate will fall on many others if you can't crack the code.")

    if choice == codeLocation:

        print("Painted in the corner, you see the number " + str(codeValue) + ".")

        print("")

    else:

        print("You find no code.")

        print("")


def gemcase(choice, codeLocation, codeValue):
    print("")

    print("Thousands of dollars in stollen gems line the inside of this simple box.")

    if choice == codeLocation:

        print("Etched inside the lid, you see the number " + str(codeValue) + ".")

        print("")

    else:

        print("You find no code.")

        print("")


def rug(choice, codeLocation, codeValue):
    print("")

    print("A dusty woven rug adorns the otherwise ragged wooden floor, you notice a corner is turned up.")

    if choice == codeLocation:

        print("Carved onto the floor beneath, you see the number " + str(codeValue) + ".")

        print("")

    else:

        print("You find no code.")

        print("")


def mirror(choice, codeLocation, codeValue):
    print("")

    print("The mirror is grimy and unpleasant. "
          "The unnatural reflection leers back at you. But you notice it isn't reflecting every detail of the room.")

    if choice == codeLocation:

        print("As you study your reflection, you notice the number " + str(codeValue) + " painted onto your shirt in "
                                                                                        "the reflection.")

        print("")

    else:

        print("You find no code.")

        print("")


def bookshelf(choice, codeLocation, codeValue):
    print("")

    print("A bookshelf filled with old catches your attention, something is off about them.")

    if choice == codeLocation:

        print("You notice the books are all the same volume. The volume number is " + str(codeValue) + ".")

        print("")

    else:

        print("You find no code.")

        print("")


def main():
    # Main game loop
    codeSegment1 = random.randint(0, 9)

    codeSegment2 = random.randint(0, 9)

    codeSegment3 = random.randint(0, 9)

    code = int(str(codeSegment1) + str(codeSegment2) + str(codeSegment3))

    items = ["Door", "Window", "Briefcase", "Ashtray", "Bucket", "Painting", "Jewelry Box", "Rug", "Mirror", "Bookshelf"]

    code1Location = random.randint(1, 3)

    code2Location = random.randint(4, 6)

    code3Location = random.randint(7, 9)

    intro()
    done = False
    while not done:
        choice = menu(items, "What do you want to inspect? ")

        if choice == 1:

            window(choice, code1Location, codeSegment1)

        elif choice == 2:

            briefcase(choice, code1Location, codeSegment1)

        elif choice == 3:

            ashtray(choice, code1Location, codeSegment1)

        elif choice == 4:

            bucket(choice, code2Location, codeSegment2)

        elif choice == 5:

            painting(choice, code2Location, codeSegment2)

        elif choice == 6:

            gemcase(choice, code2Location, codeSegment2)

        elif choice == 7:

            rug(choice, code3Location, codeSegment3)

        elif choice == 8:

            mirror(choice, code3Location, codeSegment3)

        elif choice == 9:

            bookshelf(choice, code3Location, codeSegment3)

        elif choice == 0:

            result = Door(code)

            if result == 1:
                break


main()
