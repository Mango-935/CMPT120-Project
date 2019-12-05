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
        if (was_visited)
            return self.description[1]
        else:
            return self.description[0]

    def getSearched(self):
        return self.was_searched

    def getItems(self):
        was_searched = True
        return items
