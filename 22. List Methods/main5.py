def main():

    # 9. reverse method 

    # we know, a list is an ordered collection (i.e. order of items remains same)

    # we use, reverse method to reverse order of items in place, i.e. by modifying the original list

    # [1, 2, 3, 4]
    # reverse is ->   [4, 3, 2, 1]

    numbers = [1, 4, 5, 9, 10]

    print(numbers)

    numbers.reverse()  # reverse the original list

    print(numbers)

    print()
    print()


    # reversed function - Does not modifies/changes the original list
    
    # usage ->   list( reversed( list_name ) )


    items = [1, 3, 4, 5, 6, 7]

    print( "Reversed list is : " + str( list( reversed(items) ) ) )

    print( items )

main()