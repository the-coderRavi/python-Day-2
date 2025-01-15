# write a python program to  arthematic operations
a = 5 
b = 8 
print (a+b)

x = 6 
y = 10
print(x-y)

a = 10 
b = 12
print(a%b)

x = 44 
y = 100
print(x*y)

g = 10 
h =56 
print(g//h)

i = 35 
j = 45
print(i**j)

print("Calculator")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    choice = input("Enter your choice: ")

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Addition result:", num1 + num2)
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Subtraction result:", num1 - num2)
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Multiplication result:", num1 * num2)
    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print("Division result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero.")
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please select a valid option.")
