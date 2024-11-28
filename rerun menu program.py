while True:  
    print("MENU")
    print("1: Calculator")
    print("2: Area of Circle")
    print("3: Temperature Conversion")
    print("4: Factorial of a Number")
    print("5: Even/Odd Number")
    print("6: Exit")  # Added exit option
    option = int(input("Enter the option you want: "))
    print("*" * 50)

    if option == 1:
        # Calculator
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        operation = int(input("Enter the operation you want to apply: "))
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if operation == 1:
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == 2:
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == 3:
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operation == 4:
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Division by zero is not allowed.")
        else:
            print("Invalid operation selected.")
    
    elif option == 2:
        # Finding the area of a circle
        r = float(input("Enter radius of the circle: "))
        PI = 3.142
        area_of_circle = PI * (r ** 2)
        print("Area of Circle =", area_of_circle)
    
    elif option == 3:
        # Conversion of temperature
        print("Select the temperature conversion:")
        print("1: Celsius to Fahrenheit")
        print("2: Fahrenheit to Celsius")
        temperature = int(input("Enter your choice: "))
        if temperature == 1:
            celsius = float(input("Enter Celsius temperature: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print("Fahrenheit =", fahrenheit)
        elif temperature == 2:
            fahrenheit = float(input("Enter Fahrenheit temperature: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print("Celsius =", celsius)
        else:
            print("Invalid choice for temperature conversion.")
    
    elif option == 4:
        # Factorial by for and while loop
        print("Select a loop for calculating factorial:")
        print("1: For loop")
        print("2: While loop")
        loop = int(input("Select a loop: "))
        number = int(input("Enter a number to find its factorial: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            factorial = 1
            if loop == 1:
                for i in range(1, number + 1):
                    factorial *= i
            elif loop == 2:
                i = 1
                while i <= number:
                    factorial *= i
                    i += 1
            else:
                print("Invalid loop choice.")
            print("Factorial =", factorial)
    
    elif option == 5:
        # Even or odd check
        number = int(input("Enter a number to check if it's even or odd: "))
        if number % 2 == 0:
            print("The number you entered is even.")
        else:
            print("The number you entered is odd.")
    
    elif option == 6:
        # Exit the loop
        print("Exiting the program. Thank you!")
        break
    
    else:
        print("Invalid option selected.")

    # Ask if user wants to continue
    rerun = input("Do you want to perform another operation? (y/n): ").lower()
    if rerun != 'y':
        print("Exiting the program. Thank you!")
        break