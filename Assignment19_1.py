PowerOfNumber = lambda No : 2 ** No

def main():
    value = int(input("Enter a number :"))

    ret = PowerOfNumber(value)

    print(f"Power of {value} is :",ret)

if __name__ == "__main__":
    main()