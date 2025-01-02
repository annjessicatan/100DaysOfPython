# ROLLERCOASTER: LOGICAL OPERATORS

# Display a welcome message to the user
print("Welcome to the rollercoaster!")

# Prompt the user for their height in cm and convert it to an integer
height = int(input("What is your height in cm? "))
bill = 0  # Initialize the variable to store the final bill amount

# Check if the user is tall enough to ride the rollercoaster
if height >= 120:
    print("You can ride the rollercoaster!")  # Inform the user they can ride

    # Prompt the user for their age and convert it to an integer
    age = int(input("What is your age? "))

    # Determine the ticket price based on the user's age
    if age < 12:  # Child ticket: under 12 years old
        bill = 5  # Set the bill to $5 for a child
        print("Child tickets are $5.")
    elif age <= 18:  # Youth ticket: 12 to 18 years old
        bill = 7  # Set the bill to $7 for a youth
        print("Youth tickets are $7.")
    else:  # Adult ticket: 19 years or older
        bill = 12  # Set the bill to $12 for an adult
        print("Adult tickets are $12.")

    # Ask if the user wants a photo taken and store their response
    wants_photo = input("Do you want a photo taken? Y or N. ")

    # If the user wants a photo, add $3 to the bill
    if wants_photo == "Y":  # If the answer is 'Y', the bill increases by $3
        bill += 3  # Add $3 to the bill for the photo

    # Print the final bill amount
    print(f"Your final bill is ${bill}")

else:
    # If the user is not tall enough, they cannot ride
    print("Sorry, you have to grow taller before you can ride.")

