from multiprocessing import Pool
import os

def OddCount(N):
    count = 0

    for i in range(1, N + 1):
        if i % 2 != 0:
            count = count + 1

    print("Process ID :", os.getpid())
    print("Input Number :", N)
    print("Odd Number Count :", count)
    print()

    return count


def main():
    Data = []

    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    p = Pool()

    Result = p.map(OddCount, Data)

    p.close()
    p.join()


if __name__ == "__main__":
    main()