import MarvellousNum

def Prime(Data):
    Sum = 0

    for i in Data:
        if MarvellousNum.ChkPrime(i):
            Sum = Sum + i

    return Sum


def main():
    value = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")
    for i in range(value):
        No = int(input())
        Data.append(No)

    Ret = Prime(Data)

    print("Addition of prime numbers is:", Ret)


if __name__ == "__main__":
    main()