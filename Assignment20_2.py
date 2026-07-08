import threading

def EvenFactor(no):
    sum = 0
    print("Even Factors are:")

    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i, end=" ")
            sum = sum + i

    print("\nSum of Even Factors:", sum)


def OddFactor(no):
    sum = 0
    print("Odd Factors are:")

    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i, end=" ")
            sum = sum + i

    print("\nSum of Odd Factors:", sum)


def main():
    value = int(input("Enter a number: "))

    t1 = threading.Thread(target=EvenFactor, args=(value,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(value,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()