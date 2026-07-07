def PositiveNegative(no):
    if no > 0:
        return "Positive Number"
    elif no < 0:
        return "Negative Number"
    else:
        return "Zero"

def main():
    Value = int(input("Enter number: "))

    Ret = PositiveNegative(Value)

    print(Ret)

if __name__ == "__main__":
    main()