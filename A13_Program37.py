def AreaRectangle(length, width):
    return length * width

def main():
    length = int(input("Enter length of rectangle: "))
    width = int(input("Enter width of rectangle: "))

    area = AreaRectangle(length, width)

    print("Area of rectangle is:", area)

if __name__ == "__main__":
    main()