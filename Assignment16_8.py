def Display(no):
    data = []
    for i in range(no):
        data.append("*")
    return data

def main():
    value = int(input("Enter number:"))

    ret = Display(value)

    for i in ret:
        print(i,end="")
    

if __name__ == "__main__":
    main()

    