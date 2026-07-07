def CountDigits(No):
    Count = 0

    for i in str(No):
        Count = Count + 1

    return Count

def main():
    Value = int(input("Enter a number: "))

    Ret = CountDigits(Value)

    print("Number of digits is:", Ret)

if __name__ == "__main__":
    main()