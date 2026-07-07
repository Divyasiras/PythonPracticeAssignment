def StringLength(Str):
    return len(Str)

def main():
    String = input("Enter your name: ")

    Ret = StringLength(String)

    print("Length of name is:", Ret)

if __name__ == "__main__":
    main()