# this program checks on the user inputand validity
print("This program checks if the input is a valid day of the week.")
print()

# username = "Gloria"
# password = "12345"
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "Gloria" and password == "12345":
    print("Access granted!!")

elif username != "Gloria" and password == "12345":
    print("Invalid username !!")

else:
     print("Access denied.") 