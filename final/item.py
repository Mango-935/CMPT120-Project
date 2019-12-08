# Chris Danyluk & Jeremy Gargana
# Class that holds an item's info


class Item:

    def __init__(self, name, description, numUses, condUse):
        self.name = name
        self.description = description
        self.numUses = numUses
        self.condUse = condUse

    def getName(self):
        return self.name

    def getNumUses(self):
        return self.numUses

    def getCondUse(self):
        return self.condUse

    def useItem(self):
        if (numUses > 0):
            numUses -= 1
        print(self.description)
