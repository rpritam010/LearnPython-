height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = int(weight)/float(height) ** 2
bmi_as_int = int(BMI)

print("the BMI is "+str(bmi_as_int))

if BMI <18.5:
    print("underweight")
elif BMI <25:
    print("Normalweight")
elif BMI <30:
    print("overweight")
elif BMI <35:
    print("obese")
else:
    print("clinically obese")

#f-String 
print(f"the BMI is for the height :{height},and for the wight :{weight} is {BMI}")