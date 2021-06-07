def main():

    numbers = [10, 20, 45, -9, 4, 43, 4, 2]

    # 3 ways to print

    for number in numbers:
        print( "Count of {} : {}".format(number,  numbers.count(number) ) )

    # or 

    # for i in range(len(numbers)):
    #     number = numbers[i]
    #     print( "Count of {} : {}".format(number,  numbers.count(number) ) )

    # or 

    # for i in range(len(numbers)):
    #     print( "Count of {} : {}".format(numbers[i],  numbers.count(numbers[i]) ) ) 

main()