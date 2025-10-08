# 1.Form input checking -vadidates user input to ensure data is complete and correct
# this program checks on the user inputand validity

def validate_name(name):
    if not name.strip():
        return "Name cannot be empty."
    elif not name.replace(" ", "").isalpha():
        return "Name must contain only letters."
    return None


def validate_age(age):
    try:
        age = int(age)
        if age <= 0:
            return "Age must be a positive number."
    except ValueError:
        return "Age must be a number."
    return None


def validate_email(email):
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        return "Invalid email format."
    return None


def get_user_input():
    print("=== User Registration Form ===")

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    # Validate all inputs
    errors = []

    name_error = validate_name(name)
    if name_error:
        errors.append(name_error)

    age_error = validate_age(age)
    if age_error:
        errors.append(age_error)

    email_error = validate_email(email)
    if email_error:
        errors.append(email_error)

    # Display results
    if errors:
        print("\n⚠️ Form submission failed! Please fix the following errors:")
        for e in errors:
            print("-", e)
    else:
        print("\n✅ Form submitted successfully!")
        print(f"Name: {name}\nAge: {age}\nEmail: {email}")


# Run the form
if __name__ == "__main__":
    get_user_input()    

 # 2.Menu sections -Responding to user choices in interactive programs

def menu_choice(choice):
    if choice == '1':
        print("You selected Option 1.")
    elif choice == '2':
        print("You selected Option 2.")
    elif choice == '3':
        print("You selected Option 3.")
    else:
        print("Invalid choice. Please select a valid option.")

# Example usage
user_input = input("Enter your choice (1-3): ")
menu_choice(user_input)

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
            print("Accessing admin dashboard, managing users, viewing logs...")
        else:
            print("You have user access.")
            # User-specific features
            print("Accessing user profile, viewing tasks, updating info...")
    else:
        print("Access denied. Invalid credentials.")


# Run the function
access_control()



# 4.Error Handling- Decting and responding to problems in program execution.
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

# Example usage
try:
    set_age(-5)
except ValueError as e:
    print(f"Error: {e}")