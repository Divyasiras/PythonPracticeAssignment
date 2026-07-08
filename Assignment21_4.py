import threading

Sum = 0
Product = 1

def Addition(Data):
    global Sum

    for i in Data:
        Sum = Sum + i


def Multiplication(Data):
    global Product

    for i in Data:
        Product = Product * i


def main():
    Data = []

    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    t1 = threading.Thread(target=Addition, args=(Data,))
    t2 = threading.Thread(target=Multiplication, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", Sum)
    print("Product of elements:", Product)


if __name__ == "__main__":
    main()