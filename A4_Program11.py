#7. Predict the output:
# Why does this happen?
#--> The value "ONE" overwrites "One" because dictionaries do not allow duplicate keys.

d = {1: "One", 1: "ONE", 2: "Two"}
print(d)

# Output
# {1: 'ONE', 2: 'Two'}