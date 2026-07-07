def Minimum(Data):
    min = Data[0]

    for i in Data:
        if i < min:
            min = i

    return min

def main():
    Data = [10, 20, 30, 40, 50]

    Ret = Minimum(Data)

    print("Minimum number is:", Ret)

if __name__ == "__main__":
    main()