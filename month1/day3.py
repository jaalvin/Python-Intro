'''Build a simple age checker: Ask the user for their age and tell them if they are eligible for certain 
services (e.g., "You are eligible to vote" or "You are too young to vote").'''

#Ask the user for their age
age = int(input("How old are you? \n"))

#Check if user's age is eligible
if age>=60:
    print("Congrats Soldier!, thank you for your service. \nYou can retire now.")

elif 18<age<60:
    print("You are going nowhere lazy comrade! \nThere's a war to win.")

else:
    print("Relax Comrade! \nChop rice, chop rice.")
