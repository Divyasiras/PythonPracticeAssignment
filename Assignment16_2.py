def ChkNum(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    value = int(input("Enter a number :"))

    result = ChkNum(value)

    if(result == True):
        print("Even number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()