number = int(input("Please enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if number < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,number + 1):
       factorial = factorial*i
   print("The factorial of",number,"is",factorial)
