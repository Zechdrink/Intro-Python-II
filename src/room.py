# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __repr__(self):
        return f"{self.name}, {self.description}. By the exit, you notice there is an {self.items}. Press Y to pick it up or choose a direction to continue."

    def addItem(self, item):
        self.items.append(item)
