def Display(no):
    Data = []

    for i in range(no, 0, -1):
        Data.append(i)

    return Data

def main():
    Value = int(input("Enter a number: "))

    Ret = Display(Value)

    for i in Ret:
        print(i)

if __name__ == "__main__":
    main()