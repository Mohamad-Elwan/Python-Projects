print("Welcome to Circle Phones Profit Calculator")
prod = 1
total = 0
'''
While statement runs when the number inputted is between 1-5 and starts off as 1 to run it once atleast.
if statements check for what number is inputted 1-5 but it also takes the quantity sold. Then it calculates
and adds it all up based on what products were sold and their quantity. Loops until 0 is inputted. Then prints
the total
'''
while 0 < prod < 6:
    prod = int(input("Enter product number 1-5, or enter 0 to stop\n"))
    if prod == 0:
        break
    if prod > 6 or prod < 0:
        print("Invalid Input, please enter a valid number")
    quan = int(input("Enter quantity sold\n"))
    if prod == 1:
        apple = 120.45 * quan
        total += apple
    elif prod == 2:
        android = 99.50 * quan
        total += android
    elif prod == 3:
        apple_tablet = 75.69 * quan
        total += apple_tablet
    elif prod == 4:
        android_tablet = 65.73 * quan
        total += android_tablet
    else:
        windows_tablet = 51.49 * quan
        total += windows_tablet
print("Your total is ", total)
