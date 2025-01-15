#A program that takes a list of numbers and prints the sum and average 

# Function to calculate sum and average
def calculate_sum_and_average(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers) if numbers else 0
    return total_sum, average

# Get user input for a list of numbers
numbers_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(float, numbers_input.split()))

# Calculate sum and average
total_sum, average = calculate_sum_and_average(numbers)

# Print the results
print(f"The sum of the numbers is: {total_sum}")
print(f"The average of the numbers is: {average}")
