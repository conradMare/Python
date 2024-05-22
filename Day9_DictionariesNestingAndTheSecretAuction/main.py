# # 92 - The Python Dictionary: Deep Dive
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# # Retrieving items from dictionary
# # print(programming_dictionary["Bug"])
#
# # Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# # print(programming_dictionary)
#
# # Create an empty dictionary
# empty_dictionary = {}
#
# # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)
#
# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# # print(programming_dictionary)
#
# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# # 94 - Nesting Lists and Dictionaries
# # Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }
#
# # Nesting a List in a Dictionary
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
#
# # Nesting Dictionary in a Dictionary
#
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }
#
# # Nesting Dictionaries in Lists
#
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5,
#     },
# ]

# 96 - The Secret Auction Program Instructions and Flow Chart
# from replit import clear
# HINT: You can call clear() to clear the output in the console.

# 97 - Solution and Complete Code for the Secret Auction Program
from art import logo

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

"""
FAQ: My console doesn't clear()

This will happen if you’re using an IDE other than replit. 
I’ll cover how to use PyCharm in Day 15. That said, you can write your own clear() function or configure your IDE like so: 

https://www.udemy.com/course/100-days-of-code/learn/lecture/19279420#questions/16084076

"""
