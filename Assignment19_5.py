from functools import reduce

def ChkPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

MapX = lambda No: No * 2
ReduceX = lambda A, B: A if A > B else B

def main():
    Data = [2, 70, 11, 10, 17, 23, 31, 77]

    FData = list(filter(ChkPrime, Data))
    MData = list(map(MapX, FData))
    Result = reduce(ReduceX, MData)

    print("Input List =", Data)
    print("List after filter =", FData)
    print("List after map =", MData)
    print("Output of reduce =", Result)

if __name__ == "__main__":
    main()