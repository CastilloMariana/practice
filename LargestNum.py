
#Calculate the largest number among 3 numbers.

#Input
number_1 = int(input("Enter a number: "))
number_2 = int (input("Enter another number: "))
number_3= int(input("Enter one more number: "))

largest_number = number_1

#Conditionals

if number_2 > largest_number:
    largest_number = number_2
    
if number_3 > largest_number:
    largest_number = number_3
    print("The largest number is: ",largest_number)

