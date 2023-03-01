# Welcome message
print("Welcome to the Global Energy Bill Calculator!\n")

# Ask user for account number
account_no = int(input("Please enter your account number:\n"))

# Ask user for month number
month_no = int(input("Please enter the month number (1-12):\n"))

# Ask user for electricity plan
electricity_plan = input("Please enter your electricity plan (EFIR or EFLR):\n")

# Ask user for electricity usage
electricity_used = int(input("Please enter the amount of electricity used in kilowatt-hours (kWh):\n"))

# Ask user for natural gas plan
natural_gas_plan = input("Please enter your natural gas plan (GFIR or GFLR):\n")

# Ask user for natural gas usage
gas_used = int(input("Please enter the amount of natural gas used in gigajoules (GJ):\n"))

# Ask user for province abbreviation
province = input("Please enter the abbreviation for your province of residence:\n")

# Calculate total electricity cost
if electricity_plan == "EFIR":
    if electricity_used <= 1000:
        electricity_price = 8.36
        total_electricity_price = electricity_used * (electricity_price / 100) + 120.62
    else:
        greater_rate = electricity_used - 1000
        electricity_price = 9.41
        remainder = greater_rate * (electricity_price / 100)
        under_the_rate = 1000 * (8.36 / 100)
        total_electricity_price = remainder + under_the_rate + 120.62
else:
    electricity_price = 9.11
    total_electricity_price = electricity_used * (electricity_price / 100) + 120.62

# Calculate total natural gas cost
if natural_gas_plan == "GFIR":
    if gas_used <= 950:
        gas_price = 4.56
        total_gas_price = gas_used * (gas_price / 100) + 1.32
    else:
        greater_gas_rate = gas_used - 950
        gas_price = 5.89
        remainder = greater_gas_rate * (gas_price / 100)
        under_gas_rate = 950 * (4.56 / 100)
        total_gas_price = remainder + under_gas_rate + 1.32
else:
    gas_price = 3.93
    total_gas_price = gas_used * (gas_price / 100) + 1.32

# Calculate tax rate based on province
tax_rate = 0.00
if province == "AB" or province == "BC" or province == "MB" or province == "NT" or province == "NU" or province == "QC" or province == "SK" or province == "YT":
    tax_rate = 0.05
elif province == "ON":
    tax_rate = 0.13
elif province == "NB" or province == "NL" or province == "NS" or province == "PE":
    tax_rate = 0.15

# Calculate total tax
tax = (total_electricity_price + total_gas_price) * tax_rate

# Calculate and print total amount due 
total_amount = total_electricity_price + total_gas_price + tax
print("Thank you. Your total amount due now is:", str(total_amount))