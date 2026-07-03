Divisible = lambda no : no % 5 == 0

def main():
    value = int(input("Enter number:"))

    ret = Divisible(value)
    print(ret)

if __name__ == "__main__":
    main()