from multiprocessing import Pool
import os

def Factorial(no):
    fact = 1

    for i in range(1, no + 1):
        fact = fact * i

    print("Process ID :", os.getpid())
    print("Input Number :", no)
    print("Factorial :", fact)
    print()

    return fact


def main():
    Data = []

    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    p = Pool()

    Result = p.map(Factorial, Data)

    p.close()
    p.join()


if __name__ == "__main__":
    main()