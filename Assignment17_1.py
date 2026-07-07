import Arithmetic

def main():
    value1 = int(input("Enter first number:"))
    value2 = int(input("Enter second number:"))

    print("Addition is:", Arithmetic.add(value1, value2))
    print("Substraction is:", Arithmetic.sub(value1, value2))
    print("Multiplication is:", Arithmetic.mul(value1, value2))
    print("Division is:", Arithmetic.div(value1, value2))

if __name__ == "__main__":
    main()