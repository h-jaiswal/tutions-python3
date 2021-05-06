# To open Command Prompt (i.e Terminal) in VS CODE -> Ctrl + J to open and close
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 > num2 :
        print(str(num1) + " is greater.")
    else :
        print(str(num2) + " is greater.")

main() # calling main()