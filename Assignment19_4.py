from functools import reduce

FilterX = lambda No: No % 2 == 0
MapX = lambda No: No * No
ReduceX = lambda A, B: A + B

def main():
    Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    FData = list(filter(FilterX, Data))
    MData = list(map(MapX, FData))
    Result = reduce(ReduceX, MData)

    print("Input List =", Data)
    print("List after filter =", FData)
    print("List after map =", MData)
    print("Output of reduce =", Result)

if __name__ == "__main__":
    main()