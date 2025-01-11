# A function that takes a number as input and returns the factorial of that number.

#Using while loop 
def fact(n):
    if n < 0:
        return "not defined."
    elif n == 1 or n == 0:
        return 1
    else:
        result = n
        while n > 1:
            result *= (n - 1)
            n-=1
        return result

num = int(input("Enter a number: "))
fact = fact(num)
print(f"The factorial of {num} is {fact}")

#Using recursive function
def fact(n):
    if n < 0:
        return "not defined" 
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

num = int(input("Enter a number: "))
fact = fact(num)
print(f"The factorial of {num} is {fact}")
