#Data Types

# Type Error
# print(len(12345))

# subscripting
print("Hello"[0])

print("123" + "345")

# Integer
print(123 + 345)
print(123_345_456) 

test = input()
print(type(test))

# Float
print(3.14159)

# Boolean
True
False

# -----------------------
# Type Error
num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")

# Type Checking
print(type(num_char))

new_num_char = str(num_char)
print(type(num_char))

print("Your name has " + new_num_char + " characters.")

# Operations
3 + 5
7 - 4
3 * 7
print(6 / 3)
print(2 ** 3)
print(type(6/3))
# PEMDASLR
# Parentheses ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -
print(3 * 3 + 3 / 3 - 3)

# Sum of digits of a two-digit number
two_digit_number = input()

num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

print(num1 + num2)

# BMI Calculator
height = input()
weight = input()
bmi = float(weight) / float(float(height) ** 2)
print(int(bmi))

# Rounding
print(round(8 / 3))
print(round(8 / 3, 2))
print(round(2.66666666, 2))
# floor division
print(8 // 3)
print(type(8 // 3))

result = 4 / 2
result /= 2
print(result)

# f-String
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}" )


# Years in weeks
age = input()
remaining = 90 - int(age)
weeks = remaining * 52
print(f"You have {weeks} weeks left.")
