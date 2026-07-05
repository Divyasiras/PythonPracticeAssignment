def main():
    Data = list(map(int, input("Enter List: ").split()))

    Square = list(map(lambda no: no * no, Data))

    print("List :", Data)
    print("Square List   :", Square)

if __name__ == "__main__":
    main()