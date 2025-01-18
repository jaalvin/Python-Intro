import re

def validate_email(email):
    # Define a regex pattern for validating email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match() to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

if __name__ == "__main__":
    # Get user input for an email address
    email = input("Enter an email address to validate: ")
    
    # Validate the email address
    if validate_email(email):
        print("The email address is valid.")
    else:
        print("The email address is invalid.")