# Python Packages vs Modules

# To add an external package
# Go to https://pypi.org/
# Search for the package name, and its docs
# Go to Settings (windows) or Preferences (mac) -> Project name -> Python Interpreter -> Add the package

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "File"])
table.align = "l"

print(table)

