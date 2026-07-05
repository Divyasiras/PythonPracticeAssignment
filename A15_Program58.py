String = lambda Str: len(Str) > 5

def main():
    Data = ["Python", "java", "C#", "javascript", "MongoDB", "MySQL"]

    Ret = list(filter(String, Data))

    print("List:", Data)
    print("_"*80)
    print("Strings with length greater than 5:", Ret)

if __name__ == "__main__":
    main()