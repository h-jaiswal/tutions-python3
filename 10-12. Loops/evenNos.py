"""
Even number ->  2, 4, 6, 8, 10, 12, .................. infinty

CONCEPT 1 

k = 1
kth even number is given by the formula - 2*k

k = 1, 1st even no = 2 * 1 i.e 2

k = 2, 2st even no = 2 * 2 i.e 4

k = 3, 3st even no = 2 * 3 i.e 6

k = 4, 4st even no = 2 * 4 i.e 8

k = 5, 5st even no = 2 * 5 i.e 10


CONCEPT 2:

Even number ->  2, 4, 6, 8, 10, 12, .................. infinty

first most even = 2
every even no = previous even number + 2

"""

def main():
    print("program to print even numbers upto n")
    n = 10

    i = 2 # first most even number
    while( i <= n):
        print(i)
        i = i + 2 # next even number
main()