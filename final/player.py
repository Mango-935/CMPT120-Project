# Chris Danyluk & Jeremy Gargana
# Class that holds the player's info


class Player.py:

    def __init__(self, name, curLoc):
        self.name = name
        self.score = 0
        self.curLoc = curLoc
        self.moveNum = 0
        self.inventory = []

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def getCurLoc(self):
        return self.curLoc

    def getMoveNum(self):
        return self.moveNum

    def getInventory(self):
        return self.inventory

    def take(self, item):
        if (self.curLoc.removeItem(item) is True):
            self.inventory.append(item)
        else:
            print("I'm Sorry! That item was already taken or doesn't exist.")

    def use(self, item):
        if (self.inventory.index(item) >= 0):
            self.inventory[self.inventory.index(item)].useItem()
            if (self.inventory[self.inventory.index(item)].getNumUses() == 0):
                self.inventory.remove(item)
        else:
            print("I'm Sorry! That item was already used or doesn't exist.")

    def drop(self, item):
        self.inventory.remove(item)
