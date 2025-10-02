# Funktioner för räkneoperationerna
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def power(a, b):
    return a ** b  # a upphöjt till b


print("Welcome to Basic Calculator")
print("Choose a mathematical operation:")
raw = input("(1) Add two numbers\n(2) Subtract two numbers\n(3) Multiply two numbers\n(4) Divide two numbers\n(5) Power (x^y)\n")

# plocka ut första tecken som är 1–5
choice = next((ch for ch in raw if ch in "12345"), None)
if choice is None:
    print("Invalid menu choice. Type 1, 2, 3, 4 or 5.")
    exit()

try:
    firstNumber = float(input("Type the first number: ").replace(",", "."))
    secondNumber = float(input("Type the second number: ").replace(",", "."))
except ValueError:
    print("You must enter numbers, not text!")
    exit()

# använd funktionerna
match choice:
    case "1":
        total = add(firstNumber, secondNumber)
        print(f"The addition of {firstNumber} + {secondNumber} is {total}")
    case "2":
        total = subtract(firstNumber, secondNumber)
        print(f"The subtraction of {firstNumber} - {secondNumber} is {total}")
    case "3":
        total = multiply(firstNumber, secondNumber)
        print(f"The multiplication of {firstNumber} * {secondNumber} is {total}")
    case "4":
        total = divide(firstNumber, secondNumber)
        print(f"The division of {firstNumber} / {secondNumber} is {total}")
    case "5":
        total = power(firstNumber, secondNumber)
        print(f"{firstNumber} raised to the power of {secondNumber} is {total}")

