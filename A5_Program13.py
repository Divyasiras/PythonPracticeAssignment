#2. Predict the output:
# Explain how numbers are converted internally.
b = bytes([65, 66, 67])
print(b)

# Output
#--> b'ABC'

#Explain how numbers are converted internally.
#-->Numbers in the range 0–255 are stored as bytes. Values 65, 66, and 67 correspond to the ASCII characters A, B, and C, so the output is b'ABC'.