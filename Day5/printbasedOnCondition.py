
for number in range(1,101):
    if number %3 ==0:
        print(f"{number} Fizz")
        if number % 5==0:
            print(f"{number} FizzBuzz")
    elif number % 5==0:
        print(f"{number} Buzz")
    elif number %3==0 & number % 5==0:
        print(f"{number} FizzBuzz")
    else:
        print(f"{number}")
