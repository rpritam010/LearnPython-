height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = int(weight)/float(height) ** 2
bmi_as_int = int(BMI)

print("the BMI is "+str(bmi_as_int))

#f-String 
print(f"the BMI is for the height :{height},and for the wight :{weight} is {BMI}")
