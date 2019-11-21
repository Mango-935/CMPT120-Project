# Chris Danyluk & Jeremy Gargana
# Class that holds a location's info


class Locale:

    def __init__(self, name, description1, description2, items):
        self.name = name
        self.description = [description1, description2]
        self.was_visited = False
        self.was_searched = False
        self.items = items