# The body mass index (BMI) is a measure used in medicine to see if someone is underweight
#  or overweight. This is the formula used to calculate it: bmi is equal to the person's 
#  weight divided by the person's height squared.
#

height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kilograms? "))

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height * height)

print(f"Your BMI is: {bmi:.2f}")

