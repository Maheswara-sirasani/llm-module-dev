## simple calculator
def calculator():
    print("select operators :")
    print("1. addition ")
    print("2. subtraction ")
    print("3. multiplication ") 
    print("4. division ")
    print("5. modulus ")
    print("6. exponentiation ")
    print("7. floor division ")
    print("8. exit ")
    while True:
        choice = input("Enter choice (1-8): ")
        if choice == '8':
            print("Exiting the calculator.")
            break
        if choice not in '1234567':
            print("Invalid choice, please try again.")
            continue
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero.")
        elif choice == '5':
            print(f"Result: {num1 % num2}")
        elif choice == '6':
            print(f"Result: {num1 ** num2}")
        elif choice == '7':
            print(f"Result: {num1 // num2}")
        else:
            print("Invalid choice, please try again.")
            
# Call the calculator function to start the program
calculator()