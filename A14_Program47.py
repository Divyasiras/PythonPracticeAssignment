Odd = lambda no : no % 2 != 0 

def main():
    value = int(input("Enter number :"))

    ret = Odd(value)
    print(ret)
    
if __name__ == "__main__":
    main()
