# # 100 - Functions with Outputs
# # Functions with Outputs
#
# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#
#     return f"{formatted_f_name} {formatted_l_name}"
#
#
# # formatted_string = format_name("AnGelA", "YU")
# # print(formatted_string)
#
# print(format_name("AnGelA", "YU"))

# 101 - Multiple return values
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"Result: {formatted_f_name} {formatted_l_name}"


print(format_name(input("What is your first name? "), input("What is your last name? ")))

