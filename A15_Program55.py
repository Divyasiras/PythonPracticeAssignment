from functools import reduce

Addition = lambda x, y: x + y

def main():
    Data = [10, 20, 30, 40]

    Sum = reduce(Addition, Data)

    print(Sum)

if __name__ == "__main__":
    main()