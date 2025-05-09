import os
import sys

# --- Basiese funksies vir berekeninge ---

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        # geen deel deur 0 
        return "Error! Division by zero."
    return a / b

def clear_screen():
    if os.name == 'nt':  # vir Windows
        os.system('cls')
    else:  # vir Mac/Linux
        os.system('clear')

# --- Main Program Loop ---

def main():
    running = True  # Sentinel variable

    while running:
        clear_screen()
        print("Simple Python Calculator")
        print("-------------------------")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")

        # toets insette
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid input! Please select a valid option.")
            input("Press Enter to continue...")
            continue 

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            running = False  # herstel die loop
            break

        # Now, we simulate a do-while loop for getting valid numbers
        valid_numbers = False
        while not valid_numbers:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                valid_numbers = True  # insette is geldig, loop word verwyder
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                # loop sal aangaan tot dat geldige waardes herken word

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'
        
        # Resultate
        print(f"\nResult: {num1} {operation} {num2} = {result}")

        continue_choice = input("\nDo you want to perform another calculation? (y/n): ").lower()

        
        if continue_choice != 'y':
            running = False  

    print("\nThank you for using the calculator!")


if __name__ == "__main__":
    main()