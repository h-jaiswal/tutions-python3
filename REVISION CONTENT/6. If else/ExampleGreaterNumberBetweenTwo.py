# To open Command Prompt (i.e Terminal) in VS CODE -> Ctrl + J to open and close
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))


    # WAY 1
    if (num1 > num2) :
        print(str(num1) + " is greater.")
    else :
        print(str(num2) + " is greater.")


    # WAY 2
    if (num1 > num2) :
        max = num1
    else :
        max = num2

    print(str(max) + " is greater.")
    

main() # calling main()