#4. Predict the output:

#Why is this allowed?
#--> This is allowed because bytearray is mutable, so its contents can be changed.

ba = bytearray([65, 66, 67])
ba[0] = 97
print(ba)

#Output:
# bytearray(b'aBC')
