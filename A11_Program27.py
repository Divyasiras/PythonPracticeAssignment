def PrimeNumber(no):
    if (no <=1):
        return False
    
    for i in range(2,no):
        if (no % i == 0):
            return False
    return True

def main():
    value = int(input("Enter Number:"))
    ret = PrimeNumber(value)

    if(ret == True):
        print("Number is Prime")
    else:
        print("Number is not Prime")

if __name__ == "__main__":
    main()