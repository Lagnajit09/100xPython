import random
import my_module

random_integer = random.randint(1, 10)
# including 1 and 10
print(random_integer)
print(my_module.pi)

# 0.00000 - 0.999999
random_float = random.random()
print(random_float)

# random decimal between 0-5
random_float *= 5
print(random_float)

# Heads or Tails
random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")


# Lists
fruits = ["apple", "mango" , "banana", 'orange', 'grapes', 'pineapple']
print(fruits[0])
print(fruits[-2])

fruits[1] = "Mango"
print(fruits)

fruits.append("Watermelon")
print(fruits)

fruits.extend(["Papaya", "Kiwi"])
print(fruits)


# Nested Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)



