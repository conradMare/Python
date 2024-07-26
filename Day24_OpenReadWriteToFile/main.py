# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# S24.222_How to Open, Read and Write to Files using the "with" Keyword:
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")

# S24.224_Understand Relative and Absolute File Paths:
# Example if file was moved to Desktop using Absolute Path: (Video example)
# with open("/Users/LondonAppBrewery/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Example if file was moved to Desktop using Relative Path: (Video Example)
with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
