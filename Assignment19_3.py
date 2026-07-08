from functools import reduce

FilterX = lambda No: No >= 70 and No <= 90
MapX = lambda No: No + 10
ReduceX = lambda A, B: A * B

def main():
    Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    FData = list(filter(FilterX, Data))
    MData = list(map(MapX, FData))
    Result = reduce(ReduceX, MData)

    print("Input List =", Data)
    print("List after filter =", FData)
    print("List after map =", MData)
    print("Output of reduce =", Result)

if __name__ == "__main__":
    main()