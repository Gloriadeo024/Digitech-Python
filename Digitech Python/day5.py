# 1.Form input checking -vadidates user input to ensure data is complete and correct

name = input("Enter your name: ")
age = input("Enter your age: ")

if not name.strip() or not age.strip():
    print("⚠️ All fields are required!")
elif not name.replace(" ", "").isalpha():
    print("⚠️ Name must contain only letters.")
elif not age.isdigit() or int(age) <= 0:
    print("⚠️ Age must be a positive number.")
else:
    print("✅ Form submitted successfully!")
    print(f"Name: {name}, Age: {age}")


#  2.Menu sections -Responding to user choices in interactive programs

print("=== Simple Menu ===")
print("1. Add Record")
print("2. View Record")
print("3. Delete Record")
print("4. Exit")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("You chose to Add a Record.")
elif choice == "2":
    print("You chose to View a Record.")
elif choice == "3":
    print("You chose to Delete a Record.")
elif choice == "4":
    print("Exiting program... Goodbye!")
else:
    print("⚠️ Invalid choice! Please enter a number between 1 and 4.")

# 3.Access control - Determining user permissions and restricting features

role = input("Enter your role (admin/user/guest): ").lower()

if role == "admin":
    print("✅ Access granted: You can view, edit, and delete records.")
elif role == "user":
    print("✅ Access granted: You can view and edit records only.")
elif role == "guest":
    print("✅ Access granted: You can view records only.")
else:
    print("❌ Access denied: Unknown role.")


# # 4.Error Handling- Decting and responding to problems in program execution.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result =", result)
except ValueError:
    print("⚠️ Error: Please enter valid numbers only.")
except ZeroDivisionError:
    print("⚠️ Error: Cannot divide by zero.")
finally:
    print("Program finished.")
