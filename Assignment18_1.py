def Addition(Data):
    Sum = 0

    for i in Data:
        Sum = Sum + i

    return Sum

def main():
    value = int(input("Enter number : "))

    Data = []

    print("Enter the elements:")
    for i in range(value):
        No = int(input())
        Data.append(No)

    Ret = Addition(Data)

    print("Addition is:", Ret)

if __name__ == "__main__":
    main()