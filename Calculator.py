import sys

def get_two_numbers():
    try:
        a = float(input("\nFirst number: "))
        b = float(input("Second number: "))
        return a, b
    except ValueError:
        print("⚠️ Please enter valid numbers!")
        return get_two_numbers()

def calculator():
    while True:
        try:
            choice = int(input(
                "\n=== CALCULATOR ===\n"
                "1. Multiplication\n"
                "2. Division\n"
                "3. Subtraction\n"
                "4. Addition\n"
                "5. Exponentiation\n"
                "6. Take Average\n"
                "7. Exit\n"
                "Choose: "
            ))
        except ValueError:
            print("⚠️ Invalid input! Please enter a number between 1-7.")
            continue

        if choice == 1:  # Multiplication
            a, b = get_two_numbers()
            print(f"👉 {a} * {b} = {a * b}")

        elif choice == 2:  # Division
            a, b = get_two_numbers()
            try:
                print(f"👉 {a} / {b} = {a / b}")
            except ZeroDivisionError:
                print("❌ Cannot divide by zero!")

        elif choice == 3:  # Subtraction
            a, b = get_two_numbers()
            print(f"👉 {a} - {b} = {a - b}")

        elif choice == 4:  # Addition
            a, b = get_two_numbers()
            print(f"👉 {a} + {b} = {a + b}")

        elif choice == 5:  # Exponentiation
            try:
                base = float(input("\nEnter base: "))
                exp = int(input("Enter exponent: "))
                print(f"👉 {base}^{exp} = {base ** exp}")
            except ValueError:
                print("⚠️ Please enter valid numbers!")

        elif choice == 6:  # Average
            try:
                count = int(input("\nHow many numbers do you want to enter? "))
                nums = []
                for i in range(count):
                    nums.append(float(input(f"Enter number {i+1}: ")))
                average = sum(nums) / count
                print(f"👉 Average = {average}")
            except ValueError:
                print("⚠️ Invalid input!")

        elif choice == 7:  # Exit
            print("\n👋 Goodbye!")
            sys.exit()

        else:
            print("⚠️ Please choose a number between 1-7.")

calculator()
