def AreaCircle(radius):
    return 3.14 * radius * radius

def main():
    radius = float(input("Enter radius of circle: "))

    area = AreaCircle(radius)

    print("Area of circle is:", area)

if __name__ == "__main__":
    main()