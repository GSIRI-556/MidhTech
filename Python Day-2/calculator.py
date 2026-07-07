import math
import random

print("========================================")
print("      SCIENTIFIC CALCULATOR")
print("========================================")

while True:

    print("\n Available Operators")
    print("+    -    *    /")
    print("%    x2   x3   xy")
    print("sqrt cbrt root")
    print("sin  cos  tan")
    print("sinh cosh tanh")
    print("log  ln   exp")
    print("10x  fact  pi")
    print("rand")
    print("exit")

    op = input("\nSelect Operator : ").lower()

    if op == "exit":
        print("Calculator Closed")
        break

    # Addition 
    elif op == "+":
        n = int(input("How many numbers? "))
        total = 0

        for i in range(n):
            num = float(input(f"Enter Number {i+1}: "))
            total += num

        print("Answer =", total)

    # Subtraction 
    elif op == "-":
        n = int(input("How many numbers? "))
        result = float(input("Enter Number 1: "))

        for i in range(1,n):
            num = float(input(f"Enter Number {i+1}:"))
            result -= num

        print("Answer =", result)

    #  Multiplication
    elif op == "*":
        n = int(input("How many numbers? "))
        result = 1

        for i in range(n):
            num = float(input(f"Enter Number {i+1}: "))
            result *= num

        print("Answer =", result)

    #  Division 
    elif op == "/":
        n = int(input("How many numbers? "))
        result = float(input("Enter Number 1: "))

        for i in range(2, n + 1):
            num = float(input(f"Enter Number {i}: "))

            if num == 0:
                print("Cannot Divide By Zero")
                break

            result /= num
        else:
            print("Answer =", result)

    # Percentage 
    elif op == "%":
        num = float(input("Enter Number : "))
        print("Answer =", num / 100)

    # Square
    elif op == "x2":
        num = float(input("Enter Number : "))
        print("Answer =", num ** 2)

    # Cube 
    elif op == "x3":
        num = float(input("Enter Number : "))
        print("Answer =", num ** 3)

    # Power 
    elif op == "xy":
        base = float(input("Enter Base : "))
        power = float(input("Enter Power : "))
        print("Answer =", base ** power)

    # Square Root 
    elif op == "sqrt":
        num = float(input("Enter Number : "))
        print("Answer =", math.sqrt(num))

    # Cube Root 
    elif op == "cbrt":
        num = float(input("Enter Number : "))
        print("Answer =", num ** (1/3))

    # Nth Root 
    elif op == "root":
        num = float(input("Enter Number : "))
        root = float(input("Enter Root : "))
        print("Answer =", num ** (1/root))

    # Sine 
    elif op == "sin":
        angle = float(input("Enter Angle in Degrees : "))
        print("Answer =", math.sin(math.radians(angle)))

    # Cosine 
    elif op == "cos":
        angle = float(input("Enter Angle in Degrees : "))
        print("Answer =", math.cos(math.radians(angle)))

    # Tangent
    elif op == "tan":
        angle = float(input("Enter Angle in Degrees : "))
        print("Answer =", math.tan(math.radians(angle)))

    # Sinh 
    elif op == "sinh":
        num = float(input("Enter Number : "))
        print("Answer =", math.sinh(num))

    # Cosh
    elif op == "cosh":
        num = float(input("Enter Number : "))
        print("Answer =", math.cosh(num))

    # Tanh 
    elif op == "tanh":
        num = float(input("Enter Number : "))
        print("Answer =", math.tanh(num))

    # Natural Log 
    elif op == "ln":
        num = float(input("Enter Number : "))
        print("Answer =", math.log(num))

    # Log Base 10 
    elif op == "log":
        num = float(input("Enter Number : "))
        print("Answer =", math.log10(num))

    #  e^x 
    elif op == "exp":
        num = float(input("Enter Number : "))
        print("Answer =", math.exp(num))

    #  10^x
    elif op == "10x":
        num = float(input("Enter Number : "))
        print("Answer =", 10 ** num)

    #  Factorial 
    elif op == "fact":
        num = int(input("Enter Integer : "))
        print("Answer =", math.factorial(num))

    #  Pi 
    elif op == "pi":
        print("π =", math.pi)

    #  Euler Number 
    elif op == "e":
        print("e =", math.e)

    #  Random 
    elif op == "rand":
        print("Random Number =", random.random())

    else:
        print("Invalid Operator")