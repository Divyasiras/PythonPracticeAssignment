def CheckCharacter(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or \
       char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
       
        return True
    
    else:
        return False

def main():
    Value = input("Enter a character: ")

    Ret = CheckCharacter(Value)

    if Ret == True:
        print("Vowel")
    else:
        print("Consonant")

if __name__ == "__main__":
    main()