#  operators in Python  
# Bitwise Operators  
#1. Bitwise AND (&)   
a = 5
b = 4   

cal = a & b
binary = bin(cal)
print(f"{cal} in binary is {binary}")


# #2. Bitwise OR (|)
a = 5
b = 4

cal = a | b
binary = bin(cal)
print(f"{cal} in binary is {binary}")


# # 3. Bitwise XOR (^)
a = 10
b = 8

cal = a ^ b
binary = bin(cal)
print(f"{cal} and it's binary is {binary}")   

#4. Bitwise NOT (~)
a = 5
print(~a) 

#5. Bitwise Left and right Shift 
print(a >>2)
print(a <<2)
