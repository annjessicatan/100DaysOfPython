# TREASURE ISLAND

# Print an ASCII art image of Treasure Island
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Print a welcome message and the mission objective
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Prompt the user to choose a direction (left or right)
direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()

# Check if the user chose 'left' or 'right' at the crossroad
if direction == 'left':
    # Prompt for the next decision when the user goes left (lake and boat options)
    decision = input('You\'ve come to a lake. There is an island in the middle of the lake.'
                     'Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    
    if decision == 'wait':  # If the user chooses to wait for the boat
        # Prompt the user to choose a door on the island
        color_choice = input('You arrive at the island unharmed. There is a house with 3 doors.'
                             ' One red, one yellow and one blue. Which colour do you choose?\n')
        
        # Check the user's choice of door and display the outcome
        if color_choice == 'red':
            print("It's a room full of fire. Game over!")  # Game over if they choose red
        elif color_choice == 'yellow':
            print("You win!")  # User wins if they choose yellow
        elif color_choice == 'blue':
            print("You were eaten by beast. Game over!")  # Game over if they choose blue
    elif decision == 'swim':  # If the user decides to swim across
        print("Oh no! You were attacked by trout. Game over!")  # Game over if they swim
elif direction == 'right':  # If the user chooses the right direction at the crossroad
    print("Sorry, you fell into a hole. Game over!")  # Game over if they go right

else:  # If the user enters an invalid input other than 'left' or 'right'
    print("Invalid input. Game over!")  # Inform the user the input was invalid and end the game
