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

import turtle as t
tim = t.Turtle()

import heroes
print(heroes.gen())
