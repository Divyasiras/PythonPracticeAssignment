# 5. Predict the output:
# Explain the reason for change / no change in id().

s = "Python"
print(id(s))
s = s + "3"
print(id(s))

#output :
#1680335634480
#1680336048544

#Reason: The id() changes because strings are immutable and concatenation creates a new string object.