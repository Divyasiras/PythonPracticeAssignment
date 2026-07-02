def Arithmetic(no1, no2):
    Add = no1 + no2
    Sub = no1 - no2
    Mul = no1 * no2
    Div = no1 / no2

    return Add, Sub, Mul, Div

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))

    Ans1, Ans2, Ans3, Ans4 = Arithmetic(Value1, Value2)

    print("Addition =", Ans1)
    print("Subtraction =", Ans2)
    print("Multiplication =", Ans3)
    print("Division =", Ans4)

if __name__ == "__main__":
    main()