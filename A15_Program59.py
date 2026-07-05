Divisible = lambda No: (No % 3 == 0) and (No % 5 == 0)

def main():
    Data = [10, 15, 18, 30, 45, 50, 60, 77]

    Ret = list(filter(Divisible, Data))

    print("List:", Data)
    print("_"*80)
    print("Numbers divisible by 3 and 5:", Ret)

if __name__ == "__main__":
    main()