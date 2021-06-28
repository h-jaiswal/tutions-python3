"""
Odd number ->  1, 3, 5, 7, 9, 11, .................. infinty

CONCEPT 1 

k = 1
kth even number is given by the formula - 2*k - 1

k = 1, 1st even no = 2 * 1 - 1 i.e 1

k = 2, 2st even no = 2 * 2 - 1  i.e 3

k = 3, 3st even no = 2 * 3 - 1 i.e 5

k = 4, 4st even no = 2 * 4 - 1 i.e 7

k = 5, 5st even no = 2 * 5 - 1 i.e 9


CONCEPT 2:

Even number ->  1, 3, 5, 7, 9, 11, .................. infinty

first most odd number = 1
every odd no = previous odd number + 2

"""

def main():
    print("program to print ODD numbers upto n")
    n = int(input("Please enter value of n: "))

    i = 1 # first most ODD number
    while( i <= n):
        print(i)
        i = i + 2 # next ODD number
main()