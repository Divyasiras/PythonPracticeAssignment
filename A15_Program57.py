from functools import reduce

Minimum = lambda x, y: x if x < y else y

def main():
    Data = [10, 20, 30, 40]

    Ret = reduce(Minimum, Data)

    print("Minimum element is:", Ret)

if __name__ == "__main__":
    main()