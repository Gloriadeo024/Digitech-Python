my_list = [1,2,3,4,4]
print(my_list)

# APPEND ADDS AN ELEMENT TO THE END OF THE LIST
my_list.append(5)
print(my_list)

# EXTEND 
my_list.extend([6,7,8])
print(my_list)

# INSERT 
my_list.insert(2, 9)
print(my_list)

# REMOVE
my_list.remove(9)
print(my_list)

# POP ...REMOVES AND RETURN AT INDEX I
# BY DEFAULT REMOVES THE LAST ELEMENT ,BUT STORES IT IN A MEMORY
popping = my_list.pop(7)
print(my_list, "removed element is: ", popping)

# INDEX
my_list.index(5)
print(my_list)

# COUNT shows how many times a thing is repeated
counting = my_list.count(4)
print(counting)

# SORT
my_list.sort()
print(my_list)

# REVERSE
my_list.reverse()
print(my_list)

# LENGTH
length = len(my_list)
print(length)

# MAXIMUM
maximum = min(my_list)
print(maximum)
maximum = max(my_list)
print(maximum)

checking = 3 in my_list
print(checking)

checking = 3 not in my_list
print(checking)

gloria = my_list.copy()

# CLEAR
my_list.clear
print(my_list)

print(gloria)


