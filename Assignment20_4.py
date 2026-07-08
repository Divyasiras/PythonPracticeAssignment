
import threading

def Small(str):
    count = 0

    for ch in str:
        if ch.islower():
            count = count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Small letters :", count)
    print()


def Capital(str):
    count = 0

    for ch in str:
        if ch.isupper():
            count = count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Capital letters :", count)
    print()


def Digits(str):
    count = 0

    for ch in str:
        if ch.isdigit():
            count = count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", count)
    print()


def main():
    value = input("Enter a string : ")

    t1 = threading.Thread(target=Small, args=(value,), name="Small")
    t2 = threading.Thread(target=Capital, args=(value,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(value,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()