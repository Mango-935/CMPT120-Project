# Chris Danyluk & Jeremy Gargana
# Final version of our final game project

from player import Player
from locale import Locale
from item import Item


def intro():
    print("Welcome to Super Duper Mario!\nThis game was inspired by Adventure "
          "& Zork.\n"
          "The game begins with you waking up after a rough night of sleep.\n"
          "You rub your eyes and blink a few times, only to realize you are "
          "not in your room.\n"
          "As you look around, you notice that you are infact in a Mall.\n")
    # Gives user title and background info



def customization():
    player = input("You have to think hard, but eventually you remember your "
                   "own name(If you did not remember your name, life would be"
                   "\neasier. Trust me on this one): ")
    return (player)
    # Gets user name for further messages and returns it


def init_game_data(player):
    curLoc = [player + ", you find yourself in a dimly lit mall. The walls "
              "are bare, revealing cracked bricks and sheetrock.",  # Mall
              "You find yourself in a trench. Dirt, grime, and rocks tumble"
              " into the center path as you stand there.",  # Trench
              player + ", you find yourself in an air balloon. The "
              "fabric seems strained, as if it could rip any "
              "moment.",  # Balloon
              player + ", you find yourself in a baseball stadium. "
              "The roar of the crowd deafens you.",  # Stadium
              "You find yourself on a helipad in the dead of night."
              " The wind batters against you, disturbing your "
              "focus.",  # Helipad
              "You find yourself on a boat in the middle of a river. The "
              "intense waves are almost making the boat capsize. "
              "Almost.",  # Boat
              player + " you find yourself in an abandoned classroom of "
              "your old school. There are old books and backpacks laying"
              " about the \nroom.",  # School
              "You find yourself in a pitch black room. There is a "
              "single green light and an empty container in the center, "
              "dangling \nfrom the ceiling."]  # DarkRoom
    b4CurLoc = ["You are inside an abandoned mall. You stand up and rub your eyes a little after your nap.",
                player + ", you walk out the back door and are greeted by an old trench, 60 feet deep.",
                "You are walking for a while, and then the world around you distorts. You magically appear in a balloon.",
                player + ", the balloon crashed into a baseball stadium. Not sure why, but continuity demands it.",
                "You head out of the stands, and once again, you seamlessly appear on a helipad.",
                player + ", you fall about 6 ft into the hatch, onto a boat. You know, adding locations after the first four has seriously changed this story.",
                "The boat docked in the window of a school classroom. Yup.",
                player + ", You walk out into a dark room. A light flickers to life as the air become very hard to breathe."]
    # Descriptions of each location given to the user.
    Light = Item("Light", "It glows a faint red light. Still too dark to see anything better.", -1, True)
    Medkit = Item("Medkit", "You start to feel a little better, not good enough to recover from what you've seen today.", 1, False)
    BugSpray = Item("BugSpray", "You spray a can of bug spray around you. You watch a millions of gnats drop to your feet, and there appears to be more", 6, False)
    Axe = Item("Axe", "Contrary to what you thought this was, you smell different now. For better or worse.", 2, False)
    # Items in game
    Mall = Locale("Mall", b4CurLoc[0], curLoc[0], [Medkit])
    Trench = Locale("Trench", b4CurLoc[1], curLoc[1], [BugSpray])
    Balloon = Locale("Balloon", b4CurLoc[2], curLoc[2], None)
    Stadium = Locale("Stadium", b4CurLoc[3], curLoc[3], None)
    Helipad = Locale("Helipad", b4CurLoc[4], curLoc[4], [Light, Axe])
    Boat = Locale("Boat", b4CurLoc[5], curLoc[5], [BugSpray])
    School = Locale("School", b4CurLoc[6], curLoc[6], None)
    Darkroom = Locale("Dark Room", b4CurLoc[7], curLoc[7], None)
    # All locations
    curLocList = [Mall, Trench, Balloon, Stadium, Helipad, Boat, School, Darkroom]
    x = Player(player, curLocList[0])
    time = 24
    return [x, curLocList, time]


def get_input(i):
    if (i == 0):  # Gives valid commands
        action = input("\nPossible actions:\nInspect Walls\nMove South\nTurn "
                       "on Lights\nLook\nSearch\nTake\nUse\nInventory\nPoints\nMap\nQuit\n").lower()
        if (action != "inspect walls" and action != "move south" and
                action != "turn on lights" and action != "look" and action != "search" and action != "take" and action != "use" and action != "inventory" and action != "points" and
                action != "map" and action != "quit"):
            action = None
    elif (i == 1):  # Gives valid commands
        action = input("\nPossible actions:\nFollow the Trench\nLook Over\n"
                       "Look\nSearch\nTake\nUse\nInventory\nPoints\nMap\nQuit\n").lower()
        if (action != "follow the trench" and action != "look over" and
                action != "look" and action != "search" and action != "take" and action != "use" and action != "inventory" and action != "points" and action != "map" and action != "quit"):
            action = None
    elif (i == 2):  # Gives valid commands
        action = input("\nPossible actions:\nJump\nWatch\nLook\nSearch\nTake\nUse\nInventory\nPoints\nMap\n"
                       "Quit\n").lower()
        if (action != "jump" and action != "watch" and action != "look" and action != "search" and action != "take" and action != "use" and action != "inventory" and action != "points" and
                action != "map" and action != "quit"):
            action = None
    elif (i == 3):  # Gives valid commands
        action = input("\nPossible actions:\nInspect Crowd\nView Field\n"
                       "Head Toward Stands\nLook\nSearch\nTake\nUse\nInventory\nPoints\nMap\nQuit\n")
        if (action != "inspect crowd" and action != "view field" and
                action != "head towards stands" and action != "look" and action != "search" and action != "take" and action != "use" and action != "inventory" and action != "points" and
                action != "map" and action != "quit"):
            action = None
    elif (i == 4):  # Gives valid commands
        action = input("\nPossible actions:\nLeave Through Hatch"
                       "\nLook\nSearch\nTake\nUse\nInventory\nPoints\nMap\nQuit\n").lower()
        if (action != "leave through hatch" and
                action != "look" and action != "search" and action != "take" and action != "use" and action != "inventory" and action != "points" and action != "map" and action != "quit"):
            action = None
    elif (i == 5):  # Gives valid commands
        action = input("\nPossible actions:\nGaze out\nHead inside\nLook\nSearch\nTake\nUse\nInventory\nPoints\n"
                       "Map\nQuit\n")
        if (action != "gaze out" and action != "head inside" and
                action != "look" and action != "search" and action != "take" and action != "use" and action != "inventory" and action != "points" and action != "map" and action != "quit"):
            action = None
    elif (i == 6):  # Gives valid commands
        action = input("\nPossible actions:\nTake Bag\nView Books\nEnter Next"
                       " Class\nLook\nSearch\nTake\nUse\nInventory\nPoints\nMap\nQuit\n").lower()
        if (action != "take bag" and action != "view books" and
                action != "enter next class" and action != "look" and action != "search" and action != "take" and action != "use" and action != "inventory" and action != "points" and
                action != "map" and action != "quit"):
            action = None
    elif (i == 7):  # Gives valid commands
        action = input("\nPossible actions:\nPull Green Light\nInspect "
                       "Container\nLook\nSearch\nTake\nUse\nInventory\nPoints\nMap\nQuit\n").lower()
        if (action != "pull green light" and action != "inspect container" and
                action != "add red light" and action != "pull red light" and
                action != "pull both lights" and action != "look" and action != "search" and action != "take" and action != "use" and action != "inventory" and action != "points" and
                action != "map" and action != "quit"):
            action = None
    return action


def update(game_data, action, i):
    me = game_data[0]
    time = game_data[2]
    if (me.getMoveNum() >= time):
        return (2)
    if (action == "quit"):
        return (3)
    elif(action == "inspect walls"):
        print("You walk over to the walls and make out a few "
              "pictures etched into the walls. You cannot "
              "make heads nor tails of them\nthough.")
    elif (action == "turn on lights"):
        print("You find the circuit breaker and fix the lights. "
              "You immediately regret doing that as the sudden "
              "flash blinds before thelights die down again.")
    elif(action == "move south"):  # Progresses to next area
        return -1
    elif(action == "look over"):
        print("You peer over the trench wall to see nothing but "
              "dust for miles around. It's quiet, too quiet.")
    elif(action == "follow the trench"):  # Progresses to next area
        return -1
    elif(action == "watch"):
        print("You look out over the city at night, it's "
              "beautiful. You only wish to know how and why the "
              "exit to a mall was a trench, and when you stepped "
              "into an already flying hot air balloon.")
    elif(action == "jump"):  # Progresses to next area
        print("You're insane. Just wanted to mention that.")
        return -1
    elif(action == "inspect crowd"):
        print("As you look through the cheering crowd around you, you notice "
              "something very unsettling. No one has a face, almost as if it "
              "had been stolen.")
    elif(action == "view field"):
        print("You look at into the field, and see no one there. The crowd "
              "deafens you with their unintelligeable chanting, but no "
              "one is playing.")
    elif(action == "head toward stands"):  # Progresses to next area
        return -1
    elif(action == "leave through hatch"):
        return -1
    elif(action == "gaze out"):
        print("You attempt to gaze out into the river, but the jerking of the "
              "boat makes you so nauseous that you can barely see straight.")
    elif(action == "head inside"):
        return -1
    elif(action == "take bag"):
        print("You figure these 1st graders probably have some "
              "good survival tools, for some reason, so you "
              "take one of the moreintact bags.")
    elif(action == "view books"):
        print("You look at one of the books on the 1st graders "
              "desk. It reads 'Python Programming: An Introduction"
              " to Computer \nScience'. You wonder if these made "
              "up kids could make a game like Zork.")
    elif(action == "pull green light"):
        return(1)  # Bad Ending
    elif(action == "inspect container"):
        print("It looks exactly like the container the green light"
              " is stored in. A small light rod could be placed"
              " inside.")
        if (me.getInventory().count("Light") > 0):
            print("\n'Add Red Light' has been added to commands!")
    elif(action == "add red light" and me.use("Light") is True):
        print("You placed the rod you stole from the helicopter "
              "pad into the container. It fits perfectly.\n'Pull "
              "Red Light' has been added to commands!")
        me.secret()
    elif(action == "pull red light" and me.getSecret() is True):
        return(1)  # Bad Ending
    elif(action == "pull both lights" and me.getSecret() is True):
        return(0)  # True Ending
    elif (action == "look"):
        print(me.getCurLoc().getDescription())
    elif (action == "search"):
        x = me.getCurLoc().getItems()
        for i in (x):
            print(x[i])
    elif (action == "take"):
        x = input("Is there an item you wish to pick up?")
        me.take(x)
    elif (action == "use"):
        x = input("What item would you like to use?")
        me.use(x)
    elif (action == "inventory"):
        x = me.getInventory()
        for i in (x):
            print(x[i])
    elif (action == "points"):
        print("Score: ", me.getScore())
    elif (action == "map"):
        print("Mall -> Trench -> Balloon -> Stadium -> Helipad -> Boat "
              "-> School -> ???")
    else:
        print("\nSorry, didn't quite catch that.")
    me.incMoveNum()
    # Changes score


def game_loop(player):
    game_data = init_game_data(player)
    me = game_data[0]
    curLocList = game_data[1]
    time = game_data[2]
    count = 0
    while (True):
        action = get_input(count)
        val = update(game_data, action, count)
        if (val is not None and val != -1):
            return val
        if (val == -1):
            count += 1
            player.goto(curLocList[count])
        # Cycles through locations


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
        # Time out ending
    else:
        print("\nWow. You are actually really bad at games or have decided "
              "that this is not the greatest thing you could be doing today. "
              "Regardless, I am offended")  # If player quits the game
    print("Game designed and programmed by Jeremy Gargana & Chris Danyluk.\n"
          "All rights belong to thus and you now owe us $20 for pirating our "
          "life's work :)")  # Credits
    
    replay = input("Would you like to play again?: ").lower()
        
    if replay == "yes":
        main()
    elif replay == "no":
        return None
    else:
        print("Please choose yes or no.")   
        
def main():
    intro()
    player = customization()
    cont = game_loop(player)
    outro(cont)


main()
