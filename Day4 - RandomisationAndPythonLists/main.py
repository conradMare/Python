# 42 - Random Module
import random
import my_module

# print(my_module.pi)

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# 44 - Understanding the Offset and Appending Items to List
# states_of_america = [
#     "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
#     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
#     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
#     "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
#     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
#     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
#     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
#     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
#     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
# ]
#
# # print(states_of_america[0])
# # print(states_of_america[-1])
#
# states_of_america[1] = "Pencilvania"
#
# # states_of_america.append("Angelaland")
#
# # states_of_america.extend(["Angelaland", "Jack Bauer Land"])
#
# print(states_of_america)
#
# dirty_dozen = [
#     "Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes",
#     "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"
# ]

# 46 - IndexErrors and Working with Nested Lists
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

# print(len(states_of_america))
# IndexError
# print(states_of_america[50])

num_of_states = len(states_of_america)
print(states_of_america[num_of_states - 1])

# dirty_dozen = [
#     "Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes",
#     "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"
# ]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Nested List
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
