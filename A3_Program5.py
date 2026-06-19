# 6. Write a Program to Display
# Data type
# memory Address
# size in bytes  of a variable entered by the user 

import sys

data = input("Enter a Number: ")

print("Value:", data)
print("Data Type:", type(data))
print("Memory Address:", id(data))
print("Size in Bytes:", sys.getsizeof(data))