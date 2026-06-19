
#1.What is a user defined function? Write a function to accept two numbers and return their multiplication.

#A function written by the user (programmer) to perform a specific task. It is created using the def keyword.

def multi(x, y):
    return x * y

No1 = int(input("Enter first number: "))
No2 = int(input("Enter second number: "))

result = multi(No1, No2)
print("Multiplication is:", result)