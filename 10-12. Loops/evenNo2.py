"""
Q - Find first n even numbers
ex. n = 5 -> 2, 4, 6, 8, 10

"""

def main():
    n = int(input("Enter number of even no.s to print: "))

    i = 1
    while( i <= n ):
        evenNo =  2 * i
        print(evenNo)

        i = i + 1
main()