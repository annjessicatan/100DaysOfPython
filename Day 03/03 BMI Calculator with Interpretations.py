# BMI CALCULATOR WITH INTERPRETATIONS

# Define the weight (in kilograms) of the person
weight = 85

# Define the height (in meters) of the person
height = 1.85

# Calculate the BMI using the formula: BMI = weight / (height^2)
bmi = weight / (height ** 2)  # This divides weight (85) by the square of height (1.85^2)

# Conditional statements to determine the BMI category
if bmi >= 18.5:  # If the BMI is greater than or equal to 18.5, the person is considered to have normal weight
    print("normal weight")
# The second condition has a logic error. We should use "elif bmi >= 25 and bmi < 29.9" for the overweight category.
elif bmi >= 25 and bmi < 29.9:  # If the BMI is between 25 and 29.9, the person is considered overweight
    print("overweight")
else:  # If the BMI is less than 18.5, the person is considered underweight
    print("underweight")

