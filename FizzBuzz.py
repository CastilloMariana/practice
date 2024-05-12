
for Num in range(1, 101):

    if Num % 3 == 0 and Num % 5 == 0:
        print("FizzBuzz")
    elif Num % 3 == 0:
        print("Fizz")
    elif Num % 5 == 0:
        print("Buzz")
    else:
        print(Num)


