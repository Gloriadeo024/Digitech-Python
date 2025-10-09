# We are performing the FOR loop in our program
for number in range(5, 10):
    if number %2 == 0:
    # if number %2 == 1:
        print(number *"*")

#  WE ARE PERFORMING THE WHILE LOOP IN OUR PROGRAM
trial = 3
attempts = 0
while attempts < trial:
    value = input("Enter the password")
    if value == "1234":
        print("Access granted")
        break
    else:
        print("Access denied try again")
        attempts += 1
else:
    print("All attempts used. Access permanently denied.")
