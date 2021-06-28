"""
Q - Print first n odd number
Take value of n from user
ex. if n = 3

print -> 1, 3, 5

Hint: Use odd no. formula

"""

def main():
    n = int(input("Please enter how many odd no.s to print:"))

    i = 1
    while( i <= n ):
        oddNo = 2 * i - 1
        print(oddNo) 
        i = i + 1

main()