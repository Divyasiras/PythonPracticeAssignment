CheckEven = lambda No: No % 2 == 0

def main():
    Data = [10, 20, 35, 40, 55, 65, 70]

    Ret = list(filter(CheckEven, Data))

    print("List:", Data)
    print("Count of even numbers:", len(Ret))

if __name__ == "__main__":
    main()