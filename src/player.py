# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

    def __repr__(self):    
        return f"\nYou are in the {self.current_room}. \n\nYour inventory: {', '.join(str(x) for x in self.inventory)}."

    def grab(self, item):
        self.inventory.append(item)
