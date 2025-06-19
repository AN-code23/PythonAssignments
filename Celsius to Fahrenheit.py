# Create a program to convert Celsius to Fahrenheit and vice versa
# Hint : use int() fir typecase,  and use formula F = (C * 9/5) + 32

celsius=int(input("Enter celsius:"))
Fahrenheit = (celsius * 9 / 5) + 32
print(Fahrenheit )

Fahrenheit = int(input("Enter Fahrenheit:"))
celsius = (Fahrenheit - 32) * 5 / 9
print(celsius)
