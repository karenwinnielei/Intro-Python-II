from room import Room
from player import Player
from item import Item

import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("flashlight", "to help with navigation"), Item("backpack", "to help carry items")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("electrolytes", "to help with hydration"), Item("helmet", "to protect your head from falling objects")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
print(
    'Welcome to the adventures game. Use [`n`, `s`, `w`, `e`] to navigate through the rooms.')

# Make a new player object that is currently in the 'outside' room.
player_name = input('Enter your name here: ')
player = Player(player_name, room['outside'])

# Write a loop that:
while True:
    #
    # * Prints the current room name
    print(f'{player.name}, you are in the {player.current_room.name}.')
# * Prints the current description (the textwrap module might be useful here).
    print((f'Location description: {player.current_room.description}'))
# * Waits for user input and decides what to do.
    player.current_room.print_item()
    player.print_items()
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
    item_selection = int(input("Which item would you like to retrieve? "))

    possible_items = player.current_room.items

    selected_item = possible_items[item_selection]

    player.retrieve(selected_item)


# If the user enters "q", quit the game.
    print('Enter [n], [s], [w], [e] to navigate.\n Enter [q] to quit.')
    command = input("> ").split(',')

    directions = ['n', 's', 'w', 'e']

    if command[0] == 'q':
        break

    elif command[0] == 'n':
        # check if the player can move to the north
        # if there is, set that north room as the player's location
        try:
            player.current_room = player.current_room.n_to
        except AttributeError:
            print("\nCannot go in that direction\n")
    elif command[0] == 's':
        try:
            player.current_room = player.current_room.s_to
        except AttributeError:
            print("\nCannot go in that direction\n")
    elif command[0] == 'e':
        try:
            player.current_room = player.current_room.e_to
        except AttributeError:
            print("\nCannot go in that direction\n")
    elif command[0] == 'w':
        try:
            player.current_room = player.current_room.w_to
        except AttributeError:
            print("\nCannot go in that direction\n")
    else:
        player.move(command[0])
    
