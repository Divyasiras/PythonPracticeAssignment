Multiplication = lambda no1, no2: no1 * no2

def main():
    value1 = int(input("enter First number:"))
    value2 = int(input("Enter second number:"))

    ret = Multiplication(value1,value2)

    print("Multiplication is:", ret)

if __name__ == "__main__":
    main()

