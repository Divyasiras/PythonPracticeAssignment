Square = lambda no: no * no * no

def main():
    value = int(input("Enter Number:"))
    ret = Square(value)
    print("Square is:",ret)

if __name__ == "__main__":
    main()