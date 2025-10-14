#Defining a function 
def get_pass(name, age):
    if age <= 17:
        return f"{name}, you are not allowed to go in!!"
    else:
        return f"{name}, you are allowed to go in!!"

 
# generate the actual name and age
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

final = get_pass(user_name, user_age)
print(final)


    
 