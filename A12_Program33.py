def Factors(no):
    i = 1

    while i <= no:
        if no % i == 0:
            print(i)
        i = i + 1

def main():
    Value = int(input("Enter a number: "))

    Factors(Value)

if __name__ == "__main__":
    main()