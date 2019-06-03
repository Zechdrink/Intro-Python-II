from room import Room
from player import Player
from equipment import Equipment
import random

equipment = {
    "Item 1": Equipment("Long Sword", 
    "strong against heavily armoured monsters"),

    "Item 2": Equipment("Long Bow",
    "the strongest stealthed distanced item in the game"),

    "Item 3": Equipment("Spartan Shield",
    "slightly offensive, mostly defensive"),

    "Item 4": Equipment("Axe",
    "good for gathering firewood and breaking down doors"),

    "Item 5": Equipment("Dirk",
    "stealthy dagger that is useful for assassinations"),

    "Item 6": Equipment("Poison Vile",
    "mixes well with any delectable beverage"),

    "Item 7": Equipment("Rock",
    "they make fantastic sounds when they forcefully come into contact with heads"),  

}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", random.choice(list(equipment.items()))),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", random.choice(list(equipment.items()))),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", random.choice(list(equipment.items()))),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", random.choice(list(equipment.items()))),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", random.choice(list(equipment.items()))),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
# room['outside'].n_to
# print("START",room['outside'], "END")
# Write a loop that:

def move(direction, current_room):
    attribute = direction + '_to'
    if direction == "y":
        return current_room
    elif hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print("Sorry, the path is blocked, find another way!! \n")
        return current_room

def pickup(cmd, current_room):
    if cmd == "y" and len(current_room.items) > 0:
        print(f"Good job adding the {current_room.items[1]} to your inventory")
        return player.grab(current_room.items[1])
    elif cmd == "n" or "e" or "w" or "s":
        return print(f"Your inventory: {player.inventory}.")
    else:
        print("There are no items in the room to pickup \n")
        return current_room

  



while True:
# * Prints the current room name
    print("\nYou are currently in the", player.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(f"Take note, {player.current_room.description}. Also you notice a {player.current_room.items[1]} on the floor.")
### asks the player to pick up the item
    print(f"Press 'y' to pick up the {player.current_room.items[1]} or choose a direction to continue on.")
# * Waits for user input and decides what to do.
    cmd = input("\n> please input here: ").lower()
# If the user enters a cardinal direction, attempt to move to the room there.

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    # print(cmd)
    if cmd == "q":
        print("The loop has been broken!")
        break

    pickup(cmd, player.current_room)
    player.current_room = move(cmd, player.current_room)
        
