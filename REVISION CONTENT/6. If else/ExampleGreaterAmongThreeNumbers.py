# maximum of THREE  numbers

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    # WAY 1
    # this way does not give required result if 
    # all three numbers are equal

    if (num1 >= num2  and  num1 >= num3):
        print(str(num1) + " is greater")
    
    if (num2 >= num1  and  num2 >= num3):
        print(str(num2) + " is greater")

    if (num3 >= num1  and  num3 >= num2):
        print(str(num3) + " is greater")


    # WAY 2  - better than WAY 1

    if ( num1 > num2 ):
        if (num1 > num3):
            max = num1
        else:
            max = num3
    else:
        if (num2 > num3):
            max = num2
        else:
            max = num3
    
    print("{} is maximum".format(max))



    # WAY 3 - better than WAY 1

    max = num1

    if (num2 > max):
        max = num2
    
    if (num3 > max):
        max = num3
    
    print("{} is the maximum".format(max))

main()