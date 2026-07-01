def Cube(no):
    return no * no * no

def main():
    value = int(input("Enter Number:"))
    ret = Cube(value)
    print("Cube is:",ret)

if __name__ == "__main__":
    main()