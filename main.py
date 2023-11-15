################################################################################
# NAME: Rowan Stratton
# DATE:  10 December 2021
# COURSE: IT-140-X1234
# ASSIGNMENT: 6-4 Milestone: Moving Between Rooms
# PURPOSE: User has the ability to move between rooms in the Jail Game.
# KNOWN ISSUES: None found
# CREDIT: Javier E. Zapanta
# ################################################################################
def showInstructions():
    # print a main menu and the commands
    print('Free yourself from Jail Game.')
    print('Move Between the Rooms with Commands.')
    print('Move Commands: go South, go North, go East, go West')
    print('Type Exit to end the game')

# A dictionary for the simplified Jail Game game, template pulled from Dragon Sample Game.
# The dictionary links a room to other rooms.


rooms = {
            'Cell Block': {'South': 'Community Room', 'North': 'Jail Cell', 'East': 'Warden Office', 'West': 'Dinning Hall'},
            'Community Room': {'North': 'Cell Block', 'East': 'Office'},
            'Office': {'West': 'Community Room'},
            'Jail Cell': {'South': 'Cell Block', 'East': 'Officer Station'},
            'Officer Station': {'West': 'Jail Cell'},
            'Dining Hall': {'West': 'Cell Block', 'North': 'Kitchen'},
            'Kitchen': {'South': 'Dining Hall'},
            'Warden Office': {'East': 'Cell Block'}
}

# starting the player on the Hall
currentRoom = 'Jail Cell'

newRoom = currentRoom
showInstructions()
while True:
    print("\nYou are in the {}".format(newRoom))

    # displays the current location and allows the user to move in a direction.
    move = input("Enter your move: ").split()[-1].capitalize()

    # user to exit
    if move == 'Exit':
        newRoom = 'exit'
        print('Thanks for playing the game. Hope you enjoyed it.')
        break

    # okay move
    elif move in rooms[newRoom]:
        newRoom = rooms[newRoom][move]

    # move will error.
    else:
        print("Invalid Move. There's no room to the {}".format(move))
