def main():

    a = 10
    b = 20
    sum = a + b

    # we have different ways to print the same thing


    
    # first way
    print("The sum of " + str(a) + " and " + str(b) + " is = " + str(sum))

    # second way
    print("The sum of", a, "and", b, "is =", sum)


    # using string format function

    # third way
    print( "The sum of {a} and {b} is = {sum}".format(a=a, b=b, sum=sum) )

    # more ways

    # fourth way
    print( "The sum of {} and {} is = {}".format(a, b, sum) )

    # fifth way
    print( "The sum of {first} and {second} is = {third}".format(first=a, second=b, third=sum) )

    # sixth way
    print( "The sum of {0} and {1} is = {2}".format(a, b, sum) )


main()