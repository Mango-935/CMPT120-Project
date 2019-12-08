# Chris Danyluk & Jeremy Gargana
# Class that holds the player's info


class Player:

    def __init__(self, name, curLoc):
        self.name = name
        self.score = 0
        self.curLoc = curLoc
        self.moveNum = 0
        self.inventory = []
        self.secret = False

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def getCurLoc(self):
        return self.curLoc

    def getMoveNum(self):
        return self.moveNum

    def incMoveNum(self):
        self.moveNum += 1

    def getInventory(self):
        x = []
        for i in (self.inventory):
            x.append(self.inventory[i].getName())
        return x

    def getSecret(self):
        return self.secret

    def secret(self):
        self.secret = True

    def goto(self, loc):
        self.score += 5
        self.curLoc = loc
        print(self.curLoc.getDescription())

    def take(self, item):
        if (self.curLoc.getSearched()):
            x = self.curLoc.removeItem(item)
            if (x is not None):
                self.inventory.append(x)
            else:
                print("I'm sorry, That item was already taken or doesn't exist.")
        else:
            print("I'm sorry, I don't understand.")

    def use(self, item):
        for i in (self.inventory):
            x = self.inventory[i].getName()
            if (x == item):
                self.inventory[self.inventory.index(item)].useItem()
                if (self.inventory[self.inventory.index(item)].getNumUses() == 0):
                    drop(self.inventory[i])
                return True
        print("I'm sorry, That item was already used or doesn't exist.")
        return False

    def drop(self, item):
        self.inventory.remove(item)