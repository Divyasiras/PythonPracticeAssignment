def Frequency(Data, No):
    Count = 0

    for i in Data:
        if i == No:
            Count = Count + 1

    return Count


def main():
    Value = int(input("Enter number: "))

    Data = []

    print("Enter the elements:")
    for i in range(Value):
        Value1 = int(input())
        Data.append(Value1)

    Search = int(input("Enter element to search: "))

    Ret = Frequency(Data, Search)

    print("Frequency is:", Ret)


if __name__ == "__main__":
    main()