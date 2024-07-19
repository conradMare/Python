# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("LightGreen")
#
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# screen = Screen()
# screen.exitonclick()

# import turtle as t
# tim = t.Turtle()
#
# import heroes
# print(heroes.gen())

# Draw a dotted line:
# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("LightGreen")
#
# # for _ in range(10):
# #     tim.forward(10)
# #     tim.color("white")
# #     tim.forward(10)
# #     tim.color("LightGreen")
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# screen = Screen()
# screen.exitonclick()

# Draw shapes:
# from turtle import Turtle, Screen
# import random
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("LightGreen")
#
# colors = ["red", "orange", "yellow", "green", "blue", "violet"]
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.left(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)
#
# screen = Screen()
# screen.exitonclick()

# Draw a random walk:
# from turtle import Turtle, Screen
# import random
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("LightGreen")
#
# colors = ["aquamarine", "coral", "CornflowerBlue", "DarkCyan", "DarkSlateGray", "DarkSeaGreen4"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
# screen = Screen()
# screen.exitonclick()

# Draw with random colors:
# import turtle as t
# import random
#
# tim = t.Turtle()
# t.colormode(255)
# tim.shape("turtle")
# tim.color("LightGreen")
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r,g,b)
#     return random_color
#
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("slowest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# Draw a Spirograph:
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("LightGreen")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
