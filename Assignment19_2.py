PowerOfNumber = lambda No1,No2 : No1 * No2

def main():
    value1 = int(input("Enter the first number :"))
    value2 = int(input("Enter the second number :"))

    ret = PowerOfNumber(value1,value2)

    print(f"Power of {value1} and {value2} is :",ret)

if __name__ == "__main__":
    main()