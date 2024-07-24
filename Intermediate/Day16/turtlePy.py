import turtle
# Docs: https://docs.python.org/3/library/turtle.html
# Turtle is a class defined inside the turtle module, so we can call it as turtle.Turtle
# to actually construct an object we need to add the () at the end of the class
# now timmy is an object of the class Turtle defined inside turtle module.
# by convention class names are Pascal cased
timmy = turtle.Turtle()
print(timmy)
# Output: <turtle.Turtle object at 0x0000024A61E43F50>


# Object Attributes

# e.g. if a car object has an attribute speed, we can access this attribute using a '.', i.e. car.speed
# Another class the turtle module has, is Screen. Screen is where the Turtle object will show up
# Screen class has attributes like canvas-height and canvas-width that its object can access
my_screen = turtle.Screen()
print(my_screen.canvheight)


# Object Methods
# e.g. if a car object has a method speed, we can call this method using a '.', i.e. car.speed()
# Screen class has a method called exitonclick() that allows the screen to wait until a click is detected
timmy.shape("turtle")
timmy.color("coral")

# move the turtle by 100 paces
timmy.forward(100)

my_screen.exitonclick()

