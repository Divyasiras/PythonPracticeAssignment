def Maximum(Data):
    Max = Data[0]

    for i in Data:
        if i > Max:
            Max = i

    return Max

def main():
    Data = [10, 20, 30, 40, 50]

    Ret = Maximum(Data)

    print("Maximum number is:", Ret)

if __name__ == "__main__":
    main()