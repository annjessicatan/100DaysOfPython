# Tip Calculator

# Display a welcoming message to the user
print("Welcome to the tip calculator!")

# Prompt the user to input the total bill amount and convert it to a float
bill = float(input("What was the total bill? $"))

# Prompt the user to input the tip percentage and convert it to an integer
tip = int(input("What percentage tip would you like to give? 10 12 15 "))

# Prompt the user to input the number of people to split the bill and convert it to an integer
people = int(input("How many people to split the bill? "))

# Calculate the tip amount based on the percentage entered by the user
final_tip = bill * tip / 100  # Tip = bill * (tip percentage / 100)

# Add the tip to the original bill to get the total bill including the tip
bill_plus_tip = bill + final_tip  # Total bill = original bill + calculated tip

# Calculate how much each person should pay by dividing the total bill by the number of people
total_bill = bill_plus_tip / people  # Amount per person = total bill / number of people

# Round the final amount to the nearest 2 decimal places to make it user-friendly
final_amount = round(total_bill, 2)  # Round to 2 decimal places

# Display the amount each person needs to pay
print(f"Each person should pay: ${final_amount}")  # Display the final rounded amount
