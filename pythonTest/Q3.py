# The correct password is "python123".
# Create a program that checks if a user enters the correct password.
correct_password = "python123"
use_input = input("Enter the Correct password: ")
if use_input == correct_password:
    print("Access Granted")
else:
    print("Access Denied")  

# The user should be given only 3 attempts.
user_attempts = 3
while user_attempts > 0:
    if use_input == correct_password:
        print("Permission Granted")
        break 
    else:
        user_attempts -= 1
        print(f"Permission Denied. You have {user_attempts} attempts left.")
        if user_attempts == 0:
            print("No attempts left. Access permanently denied.")
            break 

user_input = input("Enter the right password: ")
if user_input == correct_password:
    print("Permission Granted") 
else:
    user_attempts -= 1
    print(f"Permission Denied. You have {user_attempts} attempts left.")
    if user_attempts == 0:
        print("No attempts left. Access permanently denied.")
    user_input = input("Enter the right password: ")
    if user_input == correct_password:
        print("Permission Granted")