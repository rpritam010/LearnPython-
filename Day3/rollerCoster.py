print("Welcom to rollerCoster")
height = int(input("Enter your height in cm"))

if height >=120:
    print("you can ride the roller Coster")
    age =int(input("What is your age? "))
    if age <12:
        bill =5
        print("Children ticket are $5. ")
    elif age <=18:
        bill = 12
        print("Youth ticket are $7. ")
    elif age >= 45 & age <=55:
        print("Everything is going to be ok. Have a free rideon us! ")
    else:
        bill = 12
        print("Adult tickets are $12. ")    
    want_photo = input("Do you wan a photo taken? Y or N. ")
    if want_photo == "Y":
        ''' add $3 to the bill'''
        bill +=3
        
    print(f"your final bill is {bill}")
        
else:
    print("Sory you have to grow taller before you can ride. ")
    