'''A program that takes user input for a number and catches errors if the user inputs something 
invalid (non-integer)'''

def valid_int(num):
  try:
    num = int(num)
    print("Cool number for a chill guy")
    return num
  except ValueError:
    raise ValueError("Invalid. Input must be an integer.")

while True:
  try:
    num = input("Enter a number: ")
    valid_int(num)
    break
  except ValueError as e:
    print(e)
