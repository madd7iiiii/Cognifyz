def calculator():
    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /, %): ")

    
        if operator == '+':
            result = num1 + num2

        elif operator == '-':
            result = num1 - num2

        elif operator == '*':
            result = num1 * num2
        
        elif operator == '/':
      
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        
        elif operator == '%':
        
            if num2 != 0:
                result = num1 % num2
            else:
                print("Error: Modulus by zero is not allowed.")
                return
        else:
            print("Error: Invalid operator")
            return

    
        print(f"Result: {num1} {operator} {num2} = {result}")


calculator()
