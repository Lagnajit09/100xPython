piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

# Slicing in piano
# Slicing works in list as well as tuple
print(piano_keys[2:5])

# output
# inclusive start, exclusive end
# ["c", "d", "e"]

# if we want to go from a point to the end of the list
# we can omit the last number
# ["c", "d", "e", "f", "g"]
print(piano_keys[2:])

# if we want to go from the start of the list to a point
# we can omit the first number
# ["a", "b", "c", "d", "e"]
print(piano_keys[:5])

# The third number represents increment
# ["c", "e"]
print(piano_keys[2:5:2])

# if we want every second item
# ["a", "c", "e", "g"]
print(piano_keys[::2])

# To reverse a list
print(piano_keys[::-1])
