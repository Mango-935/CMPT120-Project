# Chris Danyluk & Jeremy Gargana
# Basics of our final game project


def main():
    print("Welcome to Super Duper Mario!\nThis game was inspired by Adventure "
          "& Zork.\n"
          "The game begins with you waking up after a rough night of sleep.\n"
          "You rub your eyes and blink a few times, only to realize you are "
          "not in your room.\n"
          "As you look around, you notice that you are infact in a Mall.\n")
    # Gives user title and background info
    curLoc = 0  # Initializes current location
    curPoints = 0  # Initializes current score
    loc_mall = "You find yourself in a dimly lit mall. The walls are bare, "
    loc_mall += "revealing cracked bricks and sheetrock."
    loc_trench = "You find yourself in a trench. Dirt, grime, and rocks tumble"
    loc_trench += " into the center path as you stand there."
    loc_balloon = "You find yourself in an air balloon. The fabric seems "
    loc_balloon += "strained, as if it could rip any moment."
    loc_darkRoom = "You find yourself in a pitch black room. There is a single "
    loc_darkRoom += "green and red light in the center, dangling from the"
    loc_darkRoom += " ceiling."
    loc_school = "You find yourself in an abandoned classroom of your old "
    loc_school += "school. There are old books and backpacks laying"
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
        print("Score: ", curPoints)  # Prints Score
        input("Please press 'Enter' to continue!")  # Gets the enter key input
        curPoints += 5  # Increments the score up by 5
        curLoc += 1  # Goes to next location
    print("You walk over and pull both lights at the same time, because you "
          "can and no one's stopping you.\n"
          "The green light goes dark as a door begins to open, releasing you "
          "from this game.\nThe red light, on the other hand, glows "
          "brighter, and brighter. Eventually, it explodes... into confetti! "
          "You Win!\n")  # Gives user conclusion
    print("Game designed and programmed by Jeremy Gargana & Chris Danyluk.\n"
          "All rights belong to thus and you now owe us $20 for pirating our "
          "life's work :)")  # Credits


main()
