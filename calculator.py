import time
def add(x, y):
    result = x + y
    print(f"Adding {x} and {y}...")
    return result

def subtract(x, y):
    result = x - y
    print(f"Subtracting {y} from {x}...")
    return result

def multiply(x, y):
    result = x * y
    print(f"Multiplying {x} by {y}...")
    return result

def divide(x, y):
    if y != 0:
        result = x / y
        print(f"Dividing {x} by {y}...")
        return result
    else:
        print("Error: Cannot divide by zero")
        return None

print("Welcome to the Overly Complicated Calculator!")
print("This calculator performs basic operations with unnecessary verbosity.")

num1 = float(input("Please enter the first number: "))
operator = input("Now, choose an operator (+, -, *, /): ")
num2 = float(input("Finally, enter the second number: "))
print("\nPerforming calculations. Please wait...\n")
for _ in range(3):
    print("...")
    time.sleep(1)
if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "Error: Invalid operator"
print("\nCalculation complete! Here is the overly detailed result:")
print(f"Result of operation: {num1} {operator} {num2} = {result}")
print("Thank you for using the Overly Complicated Calculator. Have a confusing day!")
