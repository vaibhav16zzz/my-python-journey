# Basic Calculator v1
# Created by Vaibhav Kale
# Date: 20 Feb 2026

print("BASIC MATHEMATICS CALCULATOR :-")
a = float(input("Enter number one : "))
b = float(input("Enter number two : "))

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)

try:
    print("Power :", a ** b)
except OverflowError:
    print("Power : Result too large")