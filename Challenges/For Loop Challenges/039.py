"""039 
Ask the user to enter a number between 1 
and 12 and then display the times table for 
that number. """

def main():
    num = int(input("Enter a number between 1 and 12: "))

    # display table
    
    # i = 1
    # while(i <= 10):
    #     result = num * i
    #     print(num + " X " + i + " = " + result)
    #     i = i + 1

    for i in range(1, 11):
        result = num * i
        print(num + " X " + i + " = " + result)
main()