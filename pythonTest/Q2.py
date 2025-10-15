student = {
"name": "Ali",
"age": 17,
"grade": "B"
}

# Update the student's grade to "A".
student["grade"] = "A"
print(student)

# Retrieve the value associated with any key of your choice and display the output.
print("Student's name:", student["name"])

# Using the relevant method, return a view of all keys in the dictionary.
print("all Keys in the dictionary:", student.keys())