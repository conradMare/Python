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

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("LightGreen")

# for _ in range(10):
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
#     tim.color("LightGreen")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()

