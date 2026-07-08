from multiprocessing import Pool

def SumSquare(N):
    sum = 0

    for i in range(1, N + 1):
        sum = sum + (i * i)

    return sum


def main():
    Data = []

    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    p = Pool()

    Result = p.map(SumSquare, Data)

    p.close()
    p.join()

    print("Output:", Result)


if __name__ == "__main__":
    main()