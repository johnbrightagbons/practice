# A program to output a calendar 
import calendar # This brings the calendar function 
# Prompt user for input
year = int (input("Please enter the year:"))
month = int (input("Please enter the month:"))
print(calendar.month(year,month))
