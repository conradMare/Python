from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_estimate = screen.textinput(title="Make a estimate", prompt="Which turtle will wint the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])

screen.exitonclick()
