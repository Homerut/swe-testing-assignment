from quick_calc.calculator import Calculator

calc = Calculator()

print("Quick Calc")
print("Type: number operator number")
print("Example: 5 + 3")
print("Type 'exit' to quit")

while True:

    user_input = input("> ")

    if user_input == "exit":
        break

    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid format")
        continue

    a = float(parts[0])
    op = parts[1]
    b = float(parts[2])

    try:

        if op == "+":
            result = calc.add(a,b)

        elif op == "-":
            result = calc.subtract(a,b)

        elif op == "*":
            result = calc.multiply(a,b)

        elif op == "/":
            result = calc.divide(a,b)

        else:
            print("Unknown operator")
            continue

        print("Result:", result)

    except Exception as e:
        print("Error:", e)
