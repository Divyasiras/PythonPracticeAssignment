maximum = lambda no1, no2: no1 if no1 > no2 else no2 

def main():
    value1 = int(input("Enter first number :"))
    value2 = int(input("Enter second number :"))

    ret = maximum(value1,value2)
    print("maximum number is :",ret)

if __name__ == "__main__":
    main()