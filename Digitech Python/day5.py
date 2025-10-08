# 1.Form input checking -vadidates user input to ensure data is complete and correct
# this program checks on the user inputand validity

def form_input_checking():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    if not name:
        print("Error: Name is required.")
        return
    if not age.isdigit() or int(age) <= 0:
        print("Error: Age must be a positive number.")
        return
    if "@" not in email or "." not in email:
        print("Error: Invalid email format.")
        return

    print("Form submitted successfully!")
    print(f"Name: {name}, Age: {age}, Email: {email}")

 # 2.Menu sections -Responding to user choices in interactive programs

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Exit")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == '1':
            option_1()
        elif choice == '2':
            option_2()
        elif choice == '3':
            option_3()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def option_1():
    print("You selected Option 1.")

def option_2():
    print("You selected Option 2.")

def option_3():
    print("You selected Option 3.")

if __name__ == "__main__":
    main_menu()

# 3.Access control - Determining user permissions and restricting features

def access_control():
    users = {
        "admin": "admin123",
        "user1": "password1",
        "user2": "password2"
    }

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        if username == "admin":
            print("You have admin access.")
            # Admin-specific features
        else:
            print("You have user access.")
            # User-specific features
    else:
        print("Access denied. Invalid credentials.")

#4.Error Handling- Decting and responding to problems in program execution.
def error_handling():
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = num1 / num2
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result of {num1} divided by {num2} is {result}.")
    finally:
        print("Execution completed.")
