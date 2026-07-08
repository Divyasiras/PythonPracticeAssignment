from multiprocessing import Pool
import os

def OddSum(N):
    sum = 0

    for i in range(1, N + 1, 2):
        sum = sum + i

    print("Process ID :", os.getpid())
    print("Input Number :", N)
    print("Sum of Odd Numbers :", sum)
    print()

    return sum


def main():
    Data = []

    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    p = Pool()

    Result = p.map(OddSum, Data)

    p.close()
    p.join()


if __name__ == "__main__":
    main()