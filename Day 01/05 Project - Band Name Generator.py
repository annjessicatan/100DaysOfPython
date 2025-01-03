# Band Name Generator Project

# Display a welcoming message to the user
print("Welcome to the Band Name Generator")

# Prompt the user to input the name of the city they grew up in and store it in the 'city' variable
city = input("What's the name of the city you grew up in? \n")

# Prompt the user to input their pet's name and store it in the 'pet' variable
pet = input("What's your pet's name? \n")

# Display the band name suggestion by combining the city and pet names
# Another way: print("Your band name could be: " + city + " " + pet)
print(f"Your band name could be: {city} {pet}")