def Add(No1, No2):
     
     return No1 + No2
 
def main():
     value1 =int(input("Enter first Number:"))
     value2 =int(input("Enter second number:"))

     result = Add(value1, value2)

     print("Addition is :",result)
     

if __name__ == "__main__":
    main()