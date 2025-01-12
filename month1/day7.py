"""A program that stores user information (name, age) in a dictionary and allows the user to 
retrieve it by providing the name"""

name = input("What's your name? ")
age = int(input("How old are you? "))

info = {"name": name, "age": age}

username = input("Who do you want information about? ")
if info["name"] == username:
    print(f"Hello, {name}. \nYou are {age} years old.")
else:
    print("Invalid user.")
