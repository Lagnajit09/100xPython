# Functions with outputs
def format_name(f_name, l_name):
    # docstrings
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


# print(
#     format_name(input("What is your first name? "),
#                 input("What is your last name? ")))



# Calculator

from art import logo

# add
def add(n1, n2):
  return n1 + n2
  
# subtract
def subtract(n1, n2):
  return n1 - n2
  
# multiply
def multiply(n1, n2):
  return n1 * n2
  
# divide
def divide(n1, n2):
  return n1 / n2

operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide
}

def calculator():
  print(logo)
  num1 = float(input("Enter the first number: "))
  
  for sign in operations:
    print(sign)
  
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    
    num2 = float(input("Enter the next number: "))
    
    function = operations[operation_symbol]
    answer = function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer} ")
  
    if input(
        f"Type 'Y' to continue calculation with {answer} or type 'N' to start a new calculation: "
    ).lower() == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()


calculator()