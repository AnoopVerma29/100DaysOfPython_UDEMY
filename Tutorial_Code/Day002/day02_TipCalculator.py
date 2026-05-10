# Day 02 of 100 Days of Python
# Tip Calculator
#
# Instructions:
# Create a tip calculator that takes the total bill amount, the percentage tip you want to give,
#  and the number of people to split the bill between. The calculator should then output the 
#  amount each person should pay.

# Anoop Verma, 6-May-2026
#
print("Welcome to the tip calculator.") 
bill = float(input("What was the total bill? INR ")) 
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip / 100)
total_amount = bill + tip_amount
amount_per_person = total_amount / people

print(f"Each person should pay: INR {amount_per_person:.2f}")
