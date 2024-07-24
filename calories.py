# To calculate calories from fat
print ("This program computes the calories in a food item using fat")
print ()
calories = float (input("Calories: "))
fat = float (input("Fat: "))

total_calories = fat / calories * 100
print (f"The food has {total_calories:.2f}% of calories from fat.")
