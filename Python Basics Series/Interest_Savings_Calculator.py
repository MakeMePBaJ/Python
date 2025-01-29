#user input
saved = float(input("current savings: "))
interest = float(input("interest (%): "))
monthly_money_rate = float(input("monthly saving rate: "))
years = int(input("how long? (in years): "))

#calculation compound interest
for _ in range(years):
    saved += monthly_money_rate * 12  # Jährliche Sparrate hinzufügen
    saved += saved * (interest / 100)  # Zinsen hinzufügen

#calculated result
print(
    f"\n\nMoney saved after {years} years: {saved:.2f} €"
)

#end application
input(f"\n\npress any key to close the application")