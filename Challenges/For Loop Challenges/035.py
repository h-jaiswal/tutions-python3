"""035 
Ask the user to enter 
their name and then 
display their name 
three times."""

def main():
    name = input("Enter a name: ")
    # i = 1
    # while( i <= 3 ):
    #     print(name)
    #     i = i + 1

    for i in range(3):
        print(name)
main()

