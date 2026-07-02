def DisplayBinary(no):
    binary = ""

    while no > 0:
        digit = no % 2
        binary = str(digit) + binary
        no = no // 2

    return binary

def main():
    value = int(input("Enter a number: "))

    ret = DisplayBinary(value)

    print("Binary equivalent is:", ret)

if __name__ == "__main__":
    main()