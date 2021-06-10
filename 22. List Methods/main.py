def main():

    numbers = [10, 20, 45, -9, 4, 43, 4, 2]

    # count = int(input("Enter how many numbers you want in the list? "))

    # for i in range(count):
    #     number = int( input("Enter a number: ") )
    #     numbers.append(number)


    # 1. len() function

    # used to find total number of items in a list
    # usage -    len(list_name)

    print( "Number of items: {}".format( len(numbers) ) )

    # 2. min() function

    # used to find the minimum value among all values in the list
    # usage -   min(list_name)

    print( "Minimum value : {}".format( min(numbers) ) )

    # 2. max() function

    # used to find the maximum value among all values in the list
    # usage -   max(list_name)

    print( "Maximum value : {}".format( max(numbers) ) )


    # 3. Ways to check if a item exist in a given list or not

    # 3.1 

    # Using index method
    # We will get -1 if the item do not exist in a given list
    # otherwise we'll get the index value, which can be anything from 0 to len(list_name)-1 

    if ( numbers.index(50) != -1 ):
        print("50 exist in numbers list")
    elif ( numbers.index(50) == -1 ):
        print("50 DO NOT exist in numbers list")


    # 3.2 

    # Using "in" operator 
    # usage -      item_value in list_name     statement will give true if item_value exist in the given list_name  otherwise it gives false

    if ( 50 in numbers ):
        print("50 exist in numbers list")
    else:
        print("50 DO NOT exist in numbers list")


    # 3.3

    # Using "not in" operator 
    # usage -      item_value not in list_name     statement will give true if item_value DO NOT EXIST in the given list_name  otherwise it gives false

    if ( 50 not in numbers ):
        print("50 DO NOT exist in numbers list")
    else:
        print("50 exist in numbers list")


    
    # 4. count() method

    # we can get the number of times a particular item_value repeats/occurs in a given list using count() method

    # usage -   list_name.count( item_value )  return required count

    # example, 
    # numbers = [10, 20, 45, -9, 4, 43, 4, 2]
    # in above list, 45 occurs 1 time
    # in above list, 4 occurs 2 times, etc.

    print( "Count of 4 : {}".format( numbers.count(4) ) )
    print( "Count of 45 : {}".format( numbers.count(45) ) )

    

    
    
main()