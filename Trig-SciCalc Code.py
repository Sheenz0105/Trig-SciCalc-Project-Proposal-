import math

def trigonometry_calculator():
    print("\n--- Trigonometry Calculator ---")
    
    while True:
        print("\nChoose a function:")
        print("1. Sine (sin)")
        print("2. Cosine (cos)")
        print("3. Tangent (tan)")
        print("4. Inverse Sine (asin)")
        print("5. Inverse Cosine (acos)")
        print("6. Inverse Tangent (atan)")
        print("7. Back to Main Menu")

        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            angle = float(input("Enter the angle in degrees: "))
            # Convert degrees to radians
            radians = math.radians(angle)

            if choice == '1':
                result = math.sin(radians)
                print(f"sin({angle}) = {result}")
            elif choice == '2':
                result = math.cos(radians)
                print(f"cos({angle}) = {result}")
            elif choice == '3':
                result = math.tan(radians)
                print(f"tan({angle}) = {result}")
            elif choice == '4':
                result = math.asin(math.sin(radians))
                print(f"asin(sin({angle})) = {math.degrees(result)} degrees")
            elif choice == '5':
                result = math.acos(math.cos(radians))
                print(f"acos(cos({angle})) = {math.degrees(result)} degrees")
            elif choice == '6':
                result = math.atan(math.tan(radians))
                print(f"atan(tan({angle})) = {math.degrees(result)} degrees")
        else:
            print("Invalid choice. Please select a valid option.")

def scientific_calculator():
    print("\n--- Scientific Calculator ---")
    
    while True:
        print("\nChoose a function:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Square Root (√)")
        print("7. Back to Main Menu")

        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice in ['1', '2', '3', '4', '5']:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    result = num1 + num2
                    print(f"{num1} + {num2} = {result}")
                elif choice == '2':
                    result = num1 - num2
                    print(f"{num1} - {num2} = {result}")
                elif choice == '3':
                    result = num1 * num2
                    print(f"{num1} * {num2} = {result}")
                elif choice == '4':
                    if num2 != 0:
                        result = num1 / num2
                        print(f"{num1} / {num2} = {result}")
                    else:
                        print("Error: Division by zero is not allowed.")
                elif choice == '5':
                    result = num1 ** num2
                    print(f"{num1} ^ {num2} = {result}")
            elif choice == '6':
                num = float(input("Enter the number: "))
                if num >= 0:
                    result = math.sqrt(num)
                    print(f"√{num} = {result}")
                else:
                    print("Error: Cannot take the square root of a negative number.")
        else:
            print("Invalid choice. Please select a valid option.")

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Trigonometry Calculator")
        print("2. Scientific Calculator")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            trigonometry_calculator()
        elif choice == '2':
            scientific_calculator()
        elif choice == '3':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu() 
    