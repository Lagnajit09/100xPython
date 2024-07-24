# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

# For loop using range function
# from 1 to 9 (excluding 10)
# by default it increments by 1
for number in range(1, 10):
    print(number)

# to make it increment by another number
# range(start, end, step)
for number in range(1, 10, 3):
    print(number)

# to add all numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)





