# Chris Danyluk & Jeremy Gargana
# Basics of our final game project


def change(location, score):
    print("Score: ", score)  # Prints Score
    return (location + 1, score + 5)  # Returns new location and new score


def intro():
    print("Welcome to Super Duper Mario!\nThis game was inspired by Adventure "
          "& Zork.\n"
          "The game begins with you waking up after a rough night of sleep.\n"
          "You rub your eyes and blink a few times, only to realize you are "
          "not in your room.\n"
          "As you look around, you notice that you are infact in a Mall.\n")
    # Gives user title and background info
    player = input("You have to think hard, but eventually you remember your "
                   "own name(If you did not remember your name, life would be"
                   " easier. Trust me on this one): ")
    return (player)
    # Gets user name for further messages and returns it


def game_loop(player):
    curLoc = 0  # Initializes current location
    curPoints = 0  # Initializes current score
    loc_mall = player + ", you find yourself in a dimly lit mall. The walls "
    loc_mall += "are bare, revealing cracked bricks and sheetrock."
    loc_trench = "You find yourself in a trench. Dirt, grime, and rocks tumble"
    loc_trench += " into the center path as you stand there."
    loc_balloon = player + ", you find yourself in an air balloon. The "
    loc_balloon += "fabric seems strained, as if it could rip any moment."
    loc_darkRoom = "You find yourself in a pitch black room. There is a "
    loc_darkRoom += "single green and red light in the center, dangling from "
    loc_darkRoom += "the ceiling."
    loc_school = player + " you find yourself in an abandoned classroom of "
    loc_school += "your old school. There are old books and backpacks laying"
    loc_school += " about the room."
    loc_helipad = "You find yourself on a helipad in the dead of night."
    loc_helipad += " The wind batters against you, disturbing your focus."
    # Descriptions of each location given to the user.

    for i in range(6):
        if (curLoc == 0):
            print(loc_mall)
        elif (curLoc == 1):
            print(loc_trench)
        elif (curLoc == 2):
            print(loc_balloon)
        elif (curLoc == 3):
            print(loc_helipad)
        elif (curLoc == 4):
            print(loc_school)
        elif (curLoc == 5):
            print(loc_darkRoom)
        input("Please press 'Enter' to continue!")  # Gets the enter key input
        curLoc, curPoints = change(curLoc, curPoints)
        # Changes location and score


def outro():
    print("You walk over and pull both lights at the same time, because you "
          "can and no one's stopping you.\n"
          "The green light goes dark as a door begins to open, releasing you "
          "from this game.\nThe red light, on the other hand, glows "
          "brighter, and brighter. Eventually, it explodes... into confetti! "
          "You Win!\n")  # Gives user conclusion
    print("Game designed and programmed by Jeremy Gargana & Chris Danyluk.\n"
          "All rights belong to thus and you now owe us $20 for pirating our "
          "life's work :)")  # Credits


def main():
    player = intro()
    game_loop(player)
    outro()


main()
