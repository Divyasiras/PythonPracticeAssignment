from multiprocessing import Pool
import time

def SumPower5(N):
    sum = 0

    for i in range(1, N + 1):
        sum = sum + (i ** 5)

    return sum


def main():
    Data = []

    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    start = time.time()

    p = Pool()

    Result = p.map(SumPower5, Data)

    p.close()
    p.join()

    end = time.time()

    print("\nResults:")
    for i in range(size):
        print("Sum of 5th powers from 1 to", Data[i], "=", Result[i])

    print("\nTotal Execution Time:", end - start, "seconds")


if __name__ == "__main__":
    main()