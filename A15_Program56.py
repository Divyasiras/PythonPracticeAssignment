from functools import reduce

Maximum = lambda x, y: x if x > y else y

def main():
    Data = [10, 20, 30, 40]

    Ret = reduce(Maximum, Data)

    print("Maximum element is:", Ret)

if __name__ == "__main__":
    main()