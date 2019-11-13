# Chris Danyluk & Jeremy Gargana
# Basics of our final game project


def change(score):
    return (score + 5)  # Returns new location and new score


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
                   "\neasier. Trust me on this one): ")
    return (player)
    # Gets user name for further messages and returns it


def game_loop(player):
    curPoints = 0  # Initializes current score
    time_limit = 12 # sets max command limit
    move_num = 0 # sets your current move number
    light = False  # Used for hidden ending
    secret = False  # Used for hidden ending
    curLoc = [player + ", you find yourself in a dimly lit mall. The walls "
              "are bare, revealing cracked bricks and sheetrock.",  # Mall
              "You find yourself in a trench. Dirt, grime, and rocks tumble"
              " into the center path as you stand there.",  # Trench
              player + ", you find yourself in an air balloon. The "
              "fabric seems strained, as if it could rip any moment.",  # Balloon
              player + ", you find yourself",  # Stadium
              "You find yourself on a helipad in the dead of night."
              " The wind batters against you, disturbing your focus.",  # Helipad
              "You find yourself",  # Boat
              player + " you find yourself in an abandoned classroom of "
              "your old school. There are old books and backpacks laying"
              " about the \nroom.",
              "You find yourself in a pitch black room. There is a "
              "single green light and an empty container in the center, "
              "dangling \nfrom the ceiling."]
    # Descriptions of each location given to the user.

    for i in range(len(curLoc)):
        print(curLoc[i])
        # Cycles through locations
        while (True):
            if (move_num >= time_limit):
                    return (2)
            if (i == 0):
                action = input("\nPossible actions:\nInspect Walls\nMove South\nTurn on Lights\nPoints\nMap\nQuit\n").lower()
                if (action == "quit"):
                    return (None)
                elif(action == "inspect walls"):
                    print("You walk over to the walls and make out a few "
                          "pictures etched into the walls. You cannot "
                          "make heads nor tails of them\nthough.")
                elif (action == "turn on lights"):
                    print("You find the circuit breaker and fix the lights. "
                          "You immediately regret doing that as the sudden "
                          "flash blinds before thelights die down again.")
                elif (action == "points"):
                    print("Score: ", curPoints)
                elif (action == "map"):
                    print("Mall -> Trench -> Balloon -> Helipad -> School -> ???")
                elif(action == "move south"):  # Progresses to next area
                    move_num += 1
                    break
                else:
                    move_num -= 1
                    print("\nSorry, didn't quite catch that.")
                move_num += 1

            elif (i == 1):  # Gives valid commands
                action = input("\nPossible actions:\nFollow the trench\nLook Over\nPoints\nMap\nQuit\n").lower()
                if (action == "quit"):
                    return (None)
                elif(action == "look over"):
                    print("You peer over the trench wall to see nothing but "
                          "dust for miles around. It's quiet, too quiet.")
                elif (action == "points"):
                    print("Score: ", curPoints)
                elif (action == "map"):
                    print("Mall -> Trench -> Balloon -> Helipad -> School -> ???")
                elif(action == "follow the trench"):  # Progresses to next area
                    move_num += 1
                    break
                else:
                    move_num -= 1
                    print("\nSorry, didn't quite catch that.")
                move_num += 1

            elif (i == 2):  # Gives valid commands
                action = input("\nPossible actions:\nJump\nWatch\nPoints\nMap\nQuit\n").lower()
                if (action == "quit"):
                    return (None)
                elif(action == "watch"):
                    print("You look out over the city at night, it's "
                          "beautiful. You only wish to know how and why the "
                          "exit to a mall was a trench, and when you stepped "
                          "into an already flying hot air balloon.")
                elif (action == "points"):
                    print("Score: ", curPoints)
                elif (action == "map"):
                    print("Mall -> Trench -> Balloon -> Helipad -> School -> ???")
                elif(action == "jump"):  # Progresses to next area
                    print("You're insane. Just wanted to mention that.")
                    move_num += 1
                    break
                else:
                    move_num -= 1
                    print("\nSorry, didn't quite catch that.")
                move_num += 1

            elif (i == 3):  # Gives valid commands
                action = input("\nPossible actions:\nLeave Through Hatch\nSteal Lights\nPoints\nMap\nQuit\n").lower()
                if (action == "quit"):
                    return (None)
                elif(action == "steal lights"):
                    print("Congrats, you just stole a light from a helipad. "
                          "I'm not sure if that is illegal so you might want"
                          " to leave, soon.")  # Allows for secret ending
                    light = True
                elif (action == "points"):
                    print("Score: ", curPoints)
                elif (action == "map"):
                    print("Mall -> Trench -> Balloon -> Helipad -> School -> ???")
                elif(action == "leave through hatch"):
                    move_num += 1
                    break  # Progresses to next area
                else:
                    move_num -= 1
                    print("\nSorry, didn't quite catch that.")
                move_num += 1

            elif (i == 4):  # Gives valid commands
                action = input("\nPossible actions:\nTake Bag\nView Books\nEnter Next Class\nPoints\nMap\nQuit\n").lower()
                if (action == "quit"):
                    return (None)
                elif(action == "take bag"):
                    print("You figure these 1st graders probably have some "
                          "good survival tools, for some reason, so you "
                          "take one of the moreintact bags.")
                elif(action == "view books"):
                    print("You look at one of the books on the 1st graders "
                          "desk. It reads 'Python Programming: An Introduction"
                          " to Computer \nScience'. You wonder if these made "
                          "up kids could make a game like Zork.")
                elif (action == "points"):
                    print("Score: ", curPoints)
                elif (action == "map"):
                    print("Mall -> Trench -> Balloon -> Helipad -> School -> ???")
                elif(action == "enter next class"):  # Progresses to next area
                    move_num += 1
                    break
                else:
                    move_num -= 1
                    print("\nSorry, didn't quite catch that.")
                move_num += 1

            elif (i == 5):  # Gives valid commands
                action = input("\nPossible actions:\nPull Green Light\nInspect Container\nPoints\nMap\nQuit\n").lower()
                if (action == "quit"):
                    return (None)
                elif (action == "points"):
                    print("Score: ", curPoints)
                elif (action == "map"):
                    print("Mall -> Trench -> Balloon -> Helipad -> School -> ???")
                elif(action == "pull green light"):
                    return(1)  # Bad Ending
                elif(action == "inspect container"):
                    print("It looks exactly like the container the green light"
                          " is stored in. A small light rod could be placed"
                          " inside.")
                    if (light is True):
                        print("\n'Add Red Light' has been added to commands!")
                elif(action == "add red light" and light is True):
                    print("You placed the rod you stole from the helicopter "
                          "pad into the container. It fits perfectly.\n'Pull "
                          "Red Light' has been added to commands!")
                    secret = True
                elif(action == "pull red light" and secret is True):
                    return(1)  # Bad Ending
                elif(action == "pull both lights" and secret is True):
                    break
                else:
                    move_num -= 1
                    print("\nSorry, didn't quite catch that.")
                move_num += 1

        curPoints = change( curPoints)
        # Changes location and score
    return(0)  # True Ending


def outro(cont):
    if (cont == 0):
        print("\nYou walk over and pull both lights at the same time, because"
              " you can and no one's stopping you.\n"
              "The green light goes dark as a door begins to open, releasing "
              "you from this game.\nThe red light, on the other hand, glows "
              "brighter, and brighter. Eventually, it explodes... into "
              "confetti! You Win!\nEnding: Good\n")  # Gives user good ending
    elif (cont == 1):
        print("You pull the one light. The light immediately extinguishes, "
              "leaving you are alone in the dark. You hear a faint noise, "
              "\nbefore a bloddcurdling scream. You failed.\nEnding: Bad\nIf "
              "only you could have done something like "
              "'Pull Both Lights' ;)\n")  # Gives user bad ending
    elif (cont == 2):
        print("Suddenly, your eyes grow dark. Your entire body locks up and "
              "everything fades away. After a moment, a massive red 'Game "
              "Over' appears above you with smaller text saying 'Cause of "
              "death: Time Out'. It would appear you are in some kind of game"
              " and your too slow to keep yourself alive. Congrats!")
    else:
        print("\nWow. You are actually really bad at games or have decided "
              "that this is not the greatest thing you could be doing today. "
              "Regardless, I am offended")  # If player quits the game
    print("Game designed and programmed by Jeremy Gargana & Chris Danyluk.\n"
          "All rights belong to thus and you now owe us $20 for pirating our "
          "life's work :)")  # Credits


def main():
    player = intro()
    cont = game_loop(player)
    outro(cont)


main()
