#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people_to_split = int(input("How many people to split the bill? "))

total_bill = bill + (bill * tip) / 100
bill_per_person = (total_bill / people_to_split)

end_bill = round(bill_per_person, 2)

print(end_bill)
