# Scope  

enemies = 2

def increase_enemies():
  enemies = 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Local scope
def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()
# The below line will give an error as potion_strength is not defined outside the function and it is a local variable
# print(potion_strength)


# Global scope
player_health = 10

def game():
  # Local function
  def drink_potion():
    potion_strength = 2
    print(player_health)

  # Calling the local function
  drink_potion()
  print(player_health)


# Local functions or variables cant be accessed outside the function
# drink_potion()
# print(potion_strength))


# Does python have block scope?
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
  # new_enemy is a global variable
  new_enemy = enemies[0]

# It is valid as new_enemy is a global variable
print(new_enemy)



# Modifying global variable
enemies = "Skeleton"
heroes = 1

def increase_enemies():
  # It is a creating a new local variable with the same name as the global variable instead of modifying the global variable
  enemies = "Zombie"
  print(f"enemies inside function: {enemies}")


def increase_heroes():
  # To access the global variable inside the function, we need to use the global keyword
  # Not a good practice to modify global variables inside a function
  # Instead, we can use the return statement
  # global heroes
  # heroes += 1
  # print(f"heroes inside function: {heroes}")

  # This heroes is refering to the global variable
  return heroes + 1


increase_enemies()
heroes = increase_heroes()
print(f"enemies outside function: {enemies}")
print(f"heroes outside function: {heroes}")



# Global constants
PI = 3.14159
URL = "https://www.google.com"
