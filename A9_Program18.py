def ChkGreater(no1, no2):
    if (no1 > no2):
        return True
    else:
        return False

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    Ret = ChkGreater(value1, value2)
    
    if(Ret == True):
        print(value1,"is Greater")
    else:
        print(value2,"is Greater")

if __name__ == "__main__":
    main()