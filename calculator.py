
def calculator():
    """
    Runs an interactive calculator with basic operations.
    """

    print("-" * 40)
    print("       Welcome to calculator 🧮")
    while True :
        print("-" * 40)

        # Get first number with input validation
        while True:
            try:
                num1 = int(input("Enter the number : "))
            except ValueError:
                print("Invalid choice... Enter a number")
                continue
            break

        # Get operator with validation
        while True:
            operator = input("Enter the operator(➕ , ➖ , ➗ , ✖️  ) : ")
            if operator in ["+" , "/" , "*" , "-"]:
                break
            print("Invalid choice")

        # Get second number with input validation
        while True:
            try:
                num2 = int(input("Enter the 2 number : "))
                break
            except ValueError:
                print("Invalid choice... Enter a number")
                continue
        
            # Perform calculation and show result
        if operator == "+":
            print("The addidtion ➕ of the numbers are : " , num1 + num2)
        elif operator == "-":
            print("The subtraction ➖ of the numbers are : " ,num1 - num2)
        elif operator == "*":
            print("The multiplication ✖️  of the numbers are : " ,num1 * num2)
        elif operator == "/":
            print("The division ➗ of the numbers are : " ,num1 / num2)
            
        print("-" * 40)

        # Ask if user wants to calculate again
        while True:
            calculate_again = input("\nWanna calculate again yes/no : ")
            if calculate_again in ["yes" , "no"]:
                break
            print("Invalid choice...Type yes/no")

        if calculate_again == "no":
            print("-" * 40)
            print("      Thanks for Calulating ")
            print("         Session Ended😀")
            print("-" * 40)
            break
        else:
            continue
    

if __name__ == "__main__":
    calculator()