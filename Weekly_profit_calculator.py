print("Welcome to Circle Phones Profit Calculator\n")
print("You can calculate the profit of the company according to a specific day or by a week or \n"
      "divide the week into weekdays and weekend\n")

entry = int(input("Enter:\n 1 - For specific Day\n 2 - For the week\n 3 - For Week Business Days\n 4 - For Weekend "
                  "days\n 0 - Exit\n"))
prod = 1
total = 0
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]


'''
Uses if statement to check if the user entered 1 if yes continue. Asks to input a day of the week and runs the same 
while loop used in part 1. Prints the profit at the end alongside the day the user specified and has two if statements
which if its above 10000 print a good job message if less then prints a work harder message.
'''
if entry == 1:
    period = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")
    print("For ", period, "\n")
    while 0 < prod < 6:
        prod = int(input("Enter product number 1-5, or enter 0 to stop\n"))
        if prod == 0:
            break
        if prod > 6 or prod < 0:
            print("Invalid Input, please enter a valid number\n")
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
    print("Your total profit for ", period, "is", total)
    if total >= 10000:
        print("You did well this", period, "! Keep up the great work!")
    if total < 10000:
        print("We didn't reach our goal for this ", period, ".More work is needed.")
# Uses elif to check for entry being 2. This time it uses a for while loop to use the while loop for each day in the
# list specified above which is 7 days. Resets prod to 1 after each day so that it loops for all days of the week.
# Uses same while loop and prints the total at the end and based on if you
# made over or under 10000 it will either print a good job message or a work harder message.

elif entry == 2:
    for day in week:
        print("For ", day)
        prod = 1
        while 0 < prod < 6:
            prod = int(input("Enter product number 1-5, or enter 0 to stop\n"))
            if prod == 0:
                break
            if prod > 6 or prod < 0:
                print("Invalid Input, please enter a valid number\n")
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
    print("Total profit for the week is", total)
    if total >= 10000:
        print("You did good this week")
    if total < 10000:
        print("We didn't reach our goal for this week.More work is needed.")

# Is the same as the above elif statement except the list used is for the week days only. And it checks for entry being
# 3. Prints the total at the end including that this option is for weekdays and the if statements for how much you made.
elif entry == 3:
    for day in week_days:
        print("For ", day)
        prod = 1
        while 0 < prod < 6:
            prod = int(input("Enter product number 1-5, or enter 0 to stop\n"))
            if prod == 0:
                break
            if prod > 6 or prod < 0:
                print("Invalid Input, please enter a valid number\n")
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
    print("Total profit for the week (business days) is", total)
    if total >= 10000:
        print("You did good this week (business days)")
    if total < 10000:
        print("We didn't reach our goal for this week(business days).More work is needed.")
# Same as the other for while loops but checks for option 4 and only loops twice since the list only has Sat and Sun.
# Prints total at the end and specifies that it's the weekend. At the end of the if elif statements it checks if its 0
# in order to just end the program and if they enter anything else it tells them invalid input.
elif entry == 4:
    for day in weekend:
        print("For ", day)
        prod = 1
        while 0 < prod < 6:
            prod = int(input("Enter product number 1-5, or enter 0 to stop\n"))
            if prod == 0:
                break
            if prod > 6 or prod < 0:
                print("Invalid Input, please enter a valid number\n")
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
    print("Total profit for the weekend is", total)
    if total >= 10000:
        print("You did good this weekend")
    if total < 10000:
        print("We didn't reach our goal for this weekend.More work is needed.")
elif entry == 0:
    print("Program End!")
else:
    print("Invalid Input, please enter a valid input")
