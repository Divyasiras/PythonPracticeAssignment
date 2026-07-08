import threading

def ChkPrime(no):
    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


def Prime(Data):
    print("Prime Numbers are:")

    for i in Data:
        if ChkPrime(i):
            print(i, end=" ")

    print()


def NonPrime(Data):
    print("Non-Prime Numbers are:")

    for i in Data:
        if not ChkPrime(i):
            print(i, end=" ")

    print()


def main():
    Data = []

    size = int(input("Enter number of elements: "))

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    t1 = threading.Thread(target=Prime, args=(Data,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(Data,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()