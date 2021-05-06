"""
Print WHOLE numbers upto n. Ask value of n from user.

"""

def main():
    print("program to print whole numbers upto n")

    n = int(input("Enter value of n: "))

    i = 0   # whole number starts from 0
    while( i <= n ):
        print( i )
        i = i + 1
main()