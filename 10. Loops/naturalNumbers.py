"""
Print natural numbers upto n. Ask value of n from user.

"""

def main():
    print("program to print natural numbers upto n")

    n = int(input("Enter value of n: "))

    i = 1   # natural number starts from 1
    while( i <= n ):
        print( i )
        i = i + 1
main()