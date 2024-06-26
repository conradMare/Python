# 60 - Defining and Calling Python Functions
# (from reeborg.ca - Practice)
# def turn_around():
#     turn_left()
#     turn_left()
#
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

# 61 - The Hurdles Loop Challenge
# (from reeborg.ca - Challenge)
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# for step in range(6):
#     hurdle()

# 62 - Indentation in Python
# Python indentation == 1 tab or 4 spaces
# Can't mix tabs and spaces in Python 3

# 63 - While Loops
# (from reeborg.ca - Challenge)
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def hurdle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# while not at_goal():
#     hurdle()

# 64 - Hurdles Challenge using While Loops
# (from reeborg.ca - Challenge)
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def hurdle():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         hurdle()
#     else:
#         move()

# 65 - Jumping over Hurdles with Variable Heights
# (from reeborg.ca - Practice)
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def hurdle():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         hurdle()
#     else:
#         move()
