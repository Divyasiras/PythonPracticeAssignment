from multiprocessing import Pool

def ChkPrime(no):
    if no < 2:
        return False

    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            return False

    return True


def PrimeCount(N):
    count = 0

    for i in range(1, N + 1):
        if ChkPrime(i):
            count = count + 1

    return count


def main():
    Data = []

    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    p = Pool()

    Result = p.map(PrimeCount, Data)

    p.close()
    p.join()

    for i in range(size):
        print("Prime count between 1 and", Data[i], "=", Result[i])


if __name__ == "__main__":
    main()