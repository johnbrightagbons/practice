# Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, 
# print the sum of the current and previous number.

# Create a variable called previous number and assign it to 0
previous_number = 0

# User input
first_number = int (input ("Enter the first number: "))
last_number = int (input ("Enter the last number: "))

# Iterate the first 10 numbers one by one using for loop and range() function
for i in range (first_number, last_number):
    

# Next, display the current number (i), previous number, and the addition of both numbers in each iteration of the loop. 
# At last, change the value previous number to current number ( previous_num = i)
    sum = previous_number + i
    print("Current Number", i, "Previous Number ", previous_number, " Sum: ", sum)
    # modify previous number
    # set it to the current number
    previous_number = i