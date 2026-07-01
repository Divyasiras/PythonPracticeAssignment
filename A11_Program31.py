def Palindrome(No):
    Temp = No
    Rev = 0

    while No != 0:
        Digit = No % 10
        Rev = (Rev * 10) + Digit
        No = No // 10

    if Temp == Rev:
        return True
    else:
        return False

def main():
    Value = int(input("Enter number: "))

    Ret = Palindrome(Value)

    if Ret == True:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()