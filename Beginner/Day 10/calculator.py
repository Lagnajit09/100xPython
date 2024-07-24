# ===========================================================
# Calculator
# from replit import clear

def calculate(num1, num2, operator):
    """ Take two numbers and a operator to perform the operation"""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return False


def calculation(num1, num2):
    print("\n+\n-\n*\n/\n")

    operator = input('Choose the operator: ')
    result = calculate(num1, num2, operator)

    if not result:
      return False

    print(f"\n{num1} {operator} {num2} = {result} \n")

    return result


should_end = False
while not should_end:
    # clear()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    should_continue = True
    while should_continue:
        result = calculation(num1, num2)

        if not result:
          print('Invalid operator!')
          result = calculation(num1, num2)

        continue_calc = input(
            f"Type 'Y' to continue calculation with {result} or type 'N' to start new calculation: "
        ).lower()

        if continue_calc == 'y':
            num1 = result
            num2 = float(input("Enter the new number: "))
        else:
            should_continue = False
