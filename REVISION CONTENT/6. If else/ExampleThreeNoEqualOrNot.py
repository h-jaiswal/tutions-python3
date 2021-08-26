

# check if all three numbers are equal or not

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    if ( num1 == num2 and num2 == num3 ):
        print("All three are equal")
    else:
        print("All three are not equal.")