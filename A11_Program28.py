def CountDigits(no):
    count = 0
    while(no != 0):
        count = count + 1
        no = no // 10
    return count

def main():
    value = int(input("Enter Number:"))
    ret = CountDigits(value)
    print("Count of Digits is:",ret)

if __name__ == "__main__":
    main()
