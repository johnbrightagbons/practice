# Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, 
# else return their sum.

first_number = int (input("Please enter the first number: "))
second_number = int (input("Please enter the second number: "))

sum = first_number + second_number
product = first_number * second_number
if product <= 1000:
    print (f"The result is {product}")
else:
    print (f"The result is {sum}")

