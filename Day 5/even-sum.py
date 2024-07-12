# Find sum of even numbers from 1 to X
target = int(input())  # Enter a number between 0 and 1000

for number in range(2, target + 1, 2):
    total += number

print(total)
