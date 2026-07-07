def DisplayEven():
    Data = []
    no = 2
    count = 0

    while count < 10:
        Data.append(no)
        no = no + 2
        count = count + 1

    return Data

def main():
    Ret = DisplayEven()

    for i in Ret:
        print(i)

if __name__ == "__main__":
    main()
