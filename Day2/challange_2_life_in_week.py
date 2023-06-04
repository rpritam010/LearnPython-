age = input("What is your age? ")

age_as_int = int(age)

Years_remaining = 90 - age_as_int
days_remaining = Years_remaining * 365
weeks_remaining = Years_remaining * 52
months_remaining = Years_remaining * 12

print(f"you have {days_remaining} days,{weeks_remaining} weeks, and {months_remaining} month left");