hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    temph = float(hours)
    tempr = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if temph > 40:
    pay = 40 * tempr + (temph-40) * tempr * 1.5
else:
    pay = temph * tempr

print("Pay: ", pay)
