tip = float(input("What is the tip amount? "))

while tip <0: # This repeats as long as the value entered is truth
    print("Sorry the amount cannot be negative. ")
    tip = float(input("What is the tip amount? "))
# Jump to line 3 and exist the loop if the value entered is greater than 0


print(f"You have tipped an amount of ${tip:.2f}")
