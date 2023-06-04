#If the bill was 150, split between 5 people , with 12% tip.
#Each person should pay (150.00/5) *1.12=33.6
#Rouund the resilt to 2 decimal places = 33.60

bill = float(input("wnat is the amount of the bill? "))

tip = int(input("What percentage of tip you want to pay? 10, 12, or 15? "))

number_of_person = int(input("How many person the bill should get splitted? "))

tip_as_percentage = tip/100

total_tip_amount = bill * tip_as_percentage

total_bill = bill + total_tip_amount

bill_per_person = total_bill / number_of_person

final_amount =  "{:.2f}".format(bill_per_person)

print(f"Each person should pay : {final_amount}")