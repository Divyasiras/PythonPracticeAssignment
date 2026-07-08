import threading

def EvenList(Data):
    sum = 0
    print("Even Elements are:")

    for i in Data:
        if i % 2 == 0:
            print(i, end=" ")
            sum = sum + i

    print("\nSum of Even Elements:", sum)


def OddList(Data):
    sum = 0
    print("Odd Elements are:")

    for i in Data:
        if i % 2 != 0:
            print(i, end=" ")
            sum = sum + i

    print("\nSum of Odd Elements:", sum)


def main():
    Data = []

    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    t1 = threading.Thread(target=EvenList, args=(Data,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(Data,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()