# Chris Danyluk & Jeremy Gargana
# Class that holds an item's info


class Item:

    def __init__(self, description, numUses, condUse):
        self.description = description
        self.numUses = numUses
        self.condUse = condUse

    def getDescription(self):
        return self.description

    def getNumUses(self):
        return self.numUses

    def getCondUse(self):
        return self.condUse

    def useItem(self):
        if (numUses > 0):
            numUses -= 1
            return True
        else:
            return False