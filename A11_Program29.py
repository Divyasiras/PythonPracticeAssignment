def SumDigits(no):
    Sum = 0

    while(no != 0):
        Digit = no % 10
        Sum = Sum + Digit
        no = no // 10
        
    return Sum

def main():
    value = int(input("Enter Number:"))
    ret = SumDigits(value)
    print("Sum of Digits is:",ret)

if __name__ == "__main__":
    main()
