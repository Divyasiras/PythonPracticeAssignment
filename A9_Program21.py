def ChkDivisible(no):
    if (no % 3 == 0)and (no % 5 == 0):
        return True
    else:
        return False

def main():
    value = int(input("Enter first number: "))

    Ret = ChkDivisible(value)
    
    if(Ret == True):
        print(value,"is divisible by both 3 and 5")
    else:
        print(value,"is not divisible by both 3 and 5")

if __name__ == "__main__":
    main()