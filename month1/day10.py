#A Python script that calculates the square root of a number using the math library.

import math

num = float(input("Enter a number to find the square root: "))
if num > 0:
  result = math.sqrt(num)
  print(f"The square root is: {result}")
else:
  print("Number must be a positive integer
