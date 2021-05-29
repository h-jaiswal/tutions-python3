import random

def main():

    num1 = random.random()     # gives a random number between 0 and 1
    print(num1)

    print()



    # if we want a random number greater than 100  or 1000 or any number, than we just multiply with that number

    num2 = random.random() * 100  # gives a random number between 0 and 100 (reason - between 0 * 100 and 1 * 100)
    print(num2)

    print()


    # to generate integer numbers in a range, we use random.randint(argumen1Value, argument2Value)

    # generate random integer (without decimal part) between 0 and 10, both inclusive   

    # Below example Pick a random integer from 0, 1, 2, 3, ......, 10
    num3 = random.randint(0, 10)

    print(num3)

    print()
    


    # choose a random value among given values ->  10   20  -7  11  0   19   31   15

    num4 = random.choice( [10, 20, -7, 11, 0, 19, 31, 15] )
    
    print(num4)

    print()

    # Picks a random value from the options “red”, “black” or “green” and stores it as the  variable “colour”.

    colour = random.choice(["red", "green", "black"]) 

    print(colour)

    print()



    # In below example, it Picks a random number between the 
    # numbers 0 [first argument] and 100 [second argument] (inclusive) in steps of 5 [third argument], 
    # i.e. it will only pick from 0, 5, 10, 15, 20, etc. 

    num = random.randrange( 0 ,100 ,5 ) 


    #  Pick a random number between 2 , 4 , 6, 8 ....... 100
    
    num = random.randrange(2, 100, 2)

    # Picks a random number between, 1, 3, 5, ......... 50

    num = random.randrange(1, 50, 2)

main()