def CheckPerfect(no):
    sum = 0

    for i in range(1, no):
        if (no % i == 0):
            sum = sum + i

    if (sum == no):
        return True
    else:
        return False

def main():
    value = int(input("Enter a number: "))

    ret = CheckPerfect(value)

    if (ret == True):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

if __name__ == "__main__":
    main()