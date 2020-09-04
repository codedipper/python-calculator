# Math functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Inputting method.

print("Select operation:")
print("`1`. Add")
print("`2`. Subtract")
print("`3`. Multiply")
print("`4`. Divide\n")

# Get method input.
method = input()

# Create function for all methods.
if method == "1":
    print("\nWhat is the first number you would like to add?\n")
    num1 = int(input())
    print("\nWhat is the second number you would like to add?\n")
    num2 = int(input())
    print("\n", num1, "+", num2, "=", add(num1, num2))
elif method == "2":
    print("\nWhat is the first number you would like to subtract?\n")
    num1 = int(input())
    print("\nWhat is the second number you would like to subtract?\n")
    num2 = int(input())
    print("\n", num1, "-", num2, "=", subtract(num1, num2))
elif method == "3":
    print("\nWhat is the first number you would like to multiply?\n")
    num1 = int(input())
    print("\nWhat is the second number you would like to multiply?\n")
    num2 = int(input())
    print("\n", num1, "*", num2, "=", multiply(num1, num2))
elif method == "4":
    print("\nWhat is the first number you would like to divide?\n")
    num1 = int(input())
    print("\nWhat is the second number you would like to divide?\n")
    num2 = int(input())
    print("\n", num1, "/", num2, "=", divide(num1, num2))
else:
    print("\nInvalid method provided.\n")
