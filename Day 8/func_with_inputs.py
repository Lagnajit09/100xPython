def greet():
  print("Hello")
  print("Hello")
  print("Hello")

# Function with input
def greet_with_name(name):
  # name = parameter
  print(f"Hello {name}")
  print(f"How do you do {name}?")

# Passing the argument
greet_with_name("Lagnajit")

# Function with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

# # Positional Arguments
greet_with("Lagnajit", "Kolkata")

# # Keyword Arguments
greet_with(location="Kolkata", name="Lagnajit")