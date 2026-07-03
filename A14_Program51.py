largestNo = lambda a,b,c: a if (a > b and a > c) else (b if b > c else c)

def main():

    value1 = int(input("Enter fisrt number :"))
    value2 = int(input("Enter second number :"))
    value3 = int(input("Enter third number :"))

    ret = largestNo(value1,value2,value3)

    print("largest numbeer is :",ret)

if __name__ == "__main__":
    main()