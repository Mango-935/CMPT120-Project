# Chris Danyluk & Jeremy Gargana
# Basics of our final game project


def main():
    print("Welcome to Super Duper Mario!\nThis game was inspired by Adventure "
          "& Zork.\n"
          "The game begins with you waking up after a rough night of sleep.\n"
          "You rub your eyes and blink a few times, only to realize you are "
          "not in your room.\n"
          "As you look around, you notice that you are infact in a Mall.\n")
    curLoc = 0
    curPoints = 0
    loc1 = "You find yourself in a dimly lit mall. The walls are bare, "
    "revealing cracked bricks and sheetrock."
    loc2 = "You find yourself in a trench. Dirt, grime, and rocks tumble into "
    "the center path as you stand there."
    loc3 = "You find yourself in an air balloon. The fabric seems strained, "
    "as if it could rip any moment."
    loc4 = "You find yourself in a pitch black room. There is a single green "
    "and red light in the center, dangling from the city."
    for i in range(4):
        if (curLoc == 0):
            print(loc1)
        elif (curLoc == 1):
            print(loc2)
        elif (curLoc == 2):
            print(loc3)
        elif (curLoc == 3):
            print(loc4)
        print("Score: ", curPoints)
        input("Please press 'Enter' to continue!")
        curPoints += 5
        curLoc += 1
    print("You walk over and pull both lights at the same time, because you "
          "can and no one's stopping you. The green light goes dark as a door"
          " begins to open, releasing you from this game. The red light, on"
          " the other hand, glows brighter, and brighter. Eventually, it"
          " explodes... into confetti! You Win!\n")
    print("Game designed and programmed by Jeremy Gargana & Chris Danyluk. A"
          "ll rights belong to thus and you now owe us $20 for pirating our "
          "life's work :)")


main()
