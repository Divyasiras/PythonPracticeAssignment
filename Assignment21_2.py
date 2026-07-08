import threading

def Maximum(Data):
    Max = Data[0]

    for i in Data:
        if i > Max:
            Max = i

    print("Maximum element:", Max)


def Minimum(Data):
    Min = Data[0]

    for i in Data:
        if i < Min:
            Min = i

    print("Minimum element:", Min)


def main():
    Data = []

    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    t1 = threading.Thread(target=Maximum, args=(Data,), name="Thread1")
    t2 = threading.Thread(target=Minimum, args=(Data,), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()