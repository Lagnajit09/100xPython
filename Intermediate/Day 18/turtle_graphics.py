# Types of import
# import turtle
# from turtle import Turtle
# import turtle as t

import turtle
import random

tim = turtle.Turtle()

# # Drawing a square
# tim.shape("turtle")
# tim.color("red")
#
# for _ in range(0, 4):
#     tim.forward(100)
#     tim.right(90)


# # Drawing a dashed line
# tim.shape("arrow")
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# # Draw shapes
# tim.shape("arrow")
# colors = ["cornflower blue", "dark gray", "medium turquoise", "goldenrod",
#           "navajo white", "misty rose", "orchid", "medium slate blue"]
#
#
# def draw(shape, angle):
#     for _ in range(shape):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape in range(3, 11):
#     angle = 360 / shape
#     tim.pencolor(colors[shape-3])
#     draw(shape, angle)


# # Draw a random walk
# turtle.colormode(255)
# # directions = [tim.left, tim.right]
# directions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fast")
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb
#
#
# for _ in range(200):
#     direction = random.choice(directions)
#     tim.color(random_color())
#     # direction(90)
#     tim.setheading(direction)
#     tim.forward(30)


# # Draw a spirograph
# tim.speed("fastest")
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(5)







screen = turtle.Screen()
screen.exitonclick()
