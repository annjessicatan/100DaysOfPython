# PYTHON PIZZA

# Display a welcome message to the user
print("Welcome to Python Pizza Deliveries!")

# Prompt the user to input the size of the pizza and store the response
size = input("What size pizza do you want? S, M or L: ")

# Ask the user if they want pepperoni and store the response
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

# Ask the user if they want extra cheese and store the response
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Initialize the bill variable to track the total cost
bill = 0

# Determine the base price of the pizza based on size
if size == 'S':  # If the size is small
    bill += 15  # Add $15 to the bill
elif size == 'M':  # If the size is medium
    bill += 20  # Add $20 to the bill
elif size == 'L':  # If the size is large
    bill += 25  # Add $25 to the bill
else:  # If the size input is invalid
    print("Sorry, this size doesn't exist. Please try again.")  # Inform the user the size doesn't exist

# Add the cost of pepperoni to the bill, based on the pizza size
if pepperoni == 'Y':  # If the user wants pepperoni
    if size == 'S':  # If the pizza size is small
        bill += 2  # Add $2 for pepperoni
    else:  # If the pizza size is medium or large
        bill += 3  # Add $3 for pepperoni

# Add the cost of extra cheese to the bill if the user wants it
if extra_cheese == 'Y':  # If the user wants extra cheese
    bill += 1  # Add $1 for extra cheese

# Display the final bill to the user
print(f"Your final bill is: ${bill}.")
