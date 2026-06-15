from utils import safe_divide

try:
    a, b = int(input("Enter the first number: ")), int(input("Enter the second number: "))
    print(safe_divide(a, b))

except ValueError:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Execution completed.")