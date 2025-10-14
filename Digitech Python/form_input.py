# form_input.py
# Taking input from user and using functions to process the input

email = input("Enter your email: ")
password = input("Enter your password: ")   
def validate_user(email, password):
    if "@" not in email:
        return "Invalid email address"
    elif len(password) < 6:
        return "Password must be at least 6 characters long"
    else:
        return "Login successful"   