def Natural(no):
    sum = 0
    for i in range(1 , no + 1):
        sum = sum + i
    return sum 

def main():
    value = int(input("Enter Number:"))
    ret = Natural(value)
    print("Sum of Natural Numbers is:",ret)

if __name__ == "__main__":
    main()