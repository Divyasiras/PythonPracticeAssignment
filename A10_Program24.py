def Factorial(no):
    Fact = 1
    for i in range(1 , no + 1):
        Fact = Fact * i
    return Fact

def main():
    value = int(input("Enter Number:"))
    ret = Factorial(value)
    
    print("Factorial is:",ret)

if __name__ == "__main__":
    main()