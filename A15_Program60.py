from functools import reduce

Product = lambda x, y: x * y

def main():
    Data = [2, 3, 4, 5]

    Ret = reduce(Product, Data)

    print("Product of all elements:", Ret)

if __name__ == "__main__":
    main()