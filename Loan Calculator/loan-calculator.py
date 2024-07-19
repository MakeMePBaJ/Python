# intro text
print()
print("This is a loan calculator made by KB")
print("feel free to use it, have fun!")
print()

# given values from strings
money_hour = float(input("Please insert your pay per hour: "))
work_time_hour = float(input("please insert how many hours you work per day: "))
work_time_days = float(input("please insert how many days you work per month (usually 20): "))
taxes = float(input("please insert your taxes in percent (usually around 20%): "))
print()

# loan calculation for inserted time and money
def calculate_loan(money_hour, work_time_hour, work_time_days, taxes):
    
    money_day = money_hour * work_time_hour
    money_month = money_day * work_time_days

# tax calculation
    after_tax_percent = taxes / 100
    tax_value =  money_month * after_tax_percent
    money_after_taxes = money_month - tax_value

    return money_day, money_month, money_after_taxes, after_tax_percent, tax_value

# income splitted to days, months, hours
def print_calculation(money_hour, money_day, money_month, money_after_taxes):

    print(f"Your Loan per HOUR is equaly to {money_hour} Euro")
    print()
    print(f"Your loan per DAY is equaly to {money_day} Euro")
    print()
    print(f"Your loan per MONTH is equaly to {money_month} Euro")
    print()
    print(f"Your loan per MONTH after TAXES is equaly to {money_after_taxes} Euro")
    print()

# end of calculation
def end():

    input("Please press any button to close the application.")

# call
money_day, money_month, money_after_taxes, after_tax_percent, tax_value = calculate_loan(money_hour, work_time_hour, work_time_days, taxes)
money_day, money_month, money_after_taxes, after_tax_percent, tax_value = calculate_loan(money_hour, work_time_hour, work_time_days, taxes)
print_calculation(money_hour, money_day, money_month, money_after_taxes)
end()