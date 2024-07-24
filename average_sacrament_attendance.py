# A program to calculate the average sacrament attendance of a unit
# based on the numbers of sundays
print ("This program calculates the average sacrament attendance for a unit in a month.")
print()
first_sunday = int(input("Please enter the total attendance for first sunday: "))
second_sunday = int(input("Please enter the total attendance for second sunday: "))
third_sunday = int(input("Please enter the total attendance for third sunday: "))
forth_sunday = int(input("Please enter the total attendance for forth sunday: "))
fifth_sunday = int(input("Please enter the total attendance for fifth sunday: "))
numbers_of_sundays = int(input("Please enter the number of sundays: "))

month_total = int (first_sunday + second_sunday + third_sunday + forth_sunday + fifth_sunday) 

total = float (month_total/numbers_of_sundays) 
total = round (total, 2)
print ("The average sacrament meeting attedance is " , total)
print()
output = f"The total attendance is {month_total}, the number of sundays are {numbers_of_sundays}, and the average sacrament meeting attendance is {total}"
print (output)
