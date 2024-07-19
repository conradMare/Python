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

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("LightGreen")

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.left(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
