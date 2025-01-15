'''A simple program to greet the user and output the user's birth year'''

from datetime import date

#Takes in user's name and age as input
Name = input("What is your name? ")
Age = int(input("What is your age? "))  

#Prints out a greeting with their name
print("Hola,",Name)

#Calculates the user's year of birth from their age
Current_year = date.today().year
Birth_year = Current_year - Age

#Prints their year of birth
print("You were born in",Birth_year)
