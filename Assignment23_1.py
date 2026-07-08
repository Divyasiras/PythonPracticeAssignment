from multiprocessing import Pool
import os

def EvenSum(N):
    sum = 0

    for i in range(2, N + 1, 2):
        sum = sum + i

    print("Process ID :", os.getpid())
    print("Input Number :", N)
    print("Sum of Even Numbers :", sum)
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

    Result = p.map(EvenSum, Data)

    p.close()
    p.join()


if __name__ == "__main__":
    main()