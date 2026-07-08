from multiprocessing import Pool
import os

def EvenCount(N):
    count = 0

    for i in range(2, N + 1, 2):
        count = count + 1

    print("Process ID :", os.getpid())
    print("Input Number :", N)
    print("Even Number Count :", count)
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

    Result = p.map(EvenCount, Data)

    p.close()
    p.join()


if __name__ == "__main__":
    main()