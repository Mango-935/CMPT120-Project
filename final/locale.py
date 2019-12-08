# Chris Danyluk & Jeremy Gargana
# Class that holds a location's info


class Locale:

    def __init__(self, name, description1, description2, items):
        self.name = name
        self.description = [description1, description2]
        self.was_visited = False
        self.was_searched = False
        self.items = items

    def getName(self):
        return self.name

    def getDescription(self):
        if (self.was_visited is True):
            return self.description[1]
        else:
            self.was_visited = True
            return self.description[0]

    def getSearched(self):
        return self.was_searched

    def getItems(self):
        self.was_searched = True
        return self.items

    def removeItem(self, item):
        if (self.items is None):
            return None
        for i in (self.items):
            if (item == i.getName()):
                x = i
                self.items.remove(i)
                return x
