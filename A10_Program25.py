def EvenNumbers(no):
    Data = []

    for i in range(1, no + 1):
        if (i % 2 == 0):
            Data.append(i)
    return Data

def main():
    value = int(input("Enter Number:"))
    ret = EvenNumbers(value)

    for i in ret:
        print(i)

if __name__ == "__main__":
    main()