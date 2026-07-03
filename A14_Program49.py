Addition = lambda no1, no2: no1 + no2

def main():
    value1 = int(input("enter First number:"))
    value2 = int(input("Enter second number:"))

    ret = Addition(value1,value2)

    print("Addition is:", ret)

if __name__ == "__main__":
    main()

