"""036 
Alter program 035 so that it will ask the user to enter their 
name and a number and then display their name that 
number of times."""

def main():
    name = input("Enter a name: ")
    n = int(input("Enter how many times to print the name: "))

    # i = 1
    # while( i <= n ):
    #     print(name)
    #     i = i + 1

    for i in range(n):
        print(name)
main()