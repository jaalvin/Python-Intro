'''Create a program that takes user input for their name and age, then prints a greeting with their name 

and calculates the year they were born.'''

#Takes in user's name and age as input
Name = input("What is your name? ")
Age = int(input("What is your age? "))

#Prints out a greeting with their name
print("Hello, ", Name)

#Calculates the user's year of birth from their age
Year = 2024 - Age

#Prints their year of birth
print("You were born in ", Year)
