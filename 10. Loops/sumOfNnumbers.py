""" 
We'll ask user for how many numbers he wants to find sum//total.

Then we'll calculate the sum of those numbers using while loop.

Procedure:

1. Ask for value of n.
2. loop from i = 1 to i = n, update statement: i = i + 1
3. In each loop: i) ask the user for ith value
                 ii) include it in the sum
4. finally, print the final sum 

n = 5, total five values for sum

when no value is provided: 
sum = 0

first value
10

sum = 10

second value
7

sum = 17

third value
3

sum = 20

fourth value
1

sum = 21

fifth value
4

sum = 25

end

final sum = 25

"""


def main():

    n = int( input("Enter how many values to add: "))

    # i = 1 
    # while( i <= n ):
        
    #     i = i + 1
    
    sum = 0  # sum of no values is zero

    i = 1 
    while( i <= n ):

        val = int(input("Please enter value #" + str(i) + ": "))
        sum = sum + val
        i = i + 1

    print(sum)
main()

