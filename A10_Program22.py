def Table(no):
    Data = []

    for i in range(1,11):
        Data.append(no * i)
    return Data

def main():
    value = int(input("Enter Number:"))
    ret = Table(value)
    
    for i in ret:
        print(i)

if __name__ == "__main__":
    main()