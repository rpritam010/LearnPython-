import random

name_string = input("give me everyone's names, seperated by a comma. ")
names = name_string.split(",")
print(names)
random_name = random.randint(0,len(names) -1)
person_to_pay_bill = names[random_name]
print(f"{person_to_pay_bill} is going to pay the bill")

## random choice
person = random.choice(names)
print(f"{person} is going to pay the bill")
