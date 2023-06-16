year = int(input("Enter the year which you want to check"))

if year % 4==0:
    if year % 100 ==0:
        if year % 100==0:
            print("The entered year is Leap Year")
        else:
            print(f"The entered year {year} is NonLeap year")
    else:
        print(f"The entered year {year} is Leap Year")      
else:
    print(f"The entered year {year} is NonLeap Year")
            
    
    