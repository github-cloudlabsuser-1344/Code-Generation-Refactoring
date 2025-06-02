# Create a basic calculator
# This code takes two numbers as input and prints their sum.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2
print("The result is:", result)
print("Choose an operation to perform with the two numbers:")
print("1. Subtract (num1 - num2)")
print("2. Multiply (num1 * num2)")
print("3. Divide (num1 / num2)")
choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    print("Subtraction result:", num1 - num2)
elif choice == "2":
    print("Multiplication result:", num1 * num2)
elif choice == "3":
    if num2 != 0:
        print("Division result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice.")