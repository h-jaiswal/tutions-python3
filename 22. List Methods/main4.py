def main():

    # 7. sort method (IN PLACE SORTING -> ie. the list will get modified/changed)

    # sort method is used to arrange a list in ascending order;

    # if list is a list of numbers, then sorted in ascending order (increading order)

    # if list is a list of strings, then sorted in dictionary order (lexicographic order)


    # example

    heights = [157, 140, 145, 130, 135]

    print(heights)

    heights.sort()   # in place sorting, i.e. modifies the list

    print(heights)

    
    print()
    print()

    # descending order, pass reverse=True inside the sort method

    sizes = [1, 4, 6, 90, 1, 43]

    print(sizes)

    sizes.sort()  # by default, list is inplace arranged in increasing order

    print(sizes)

    sizes.sort(reverse=True)  # arranges the list inplace in descending order

    print(sizes)

    print()
    print()


    # 8. sorted function - does not modify original list

    
    heights = [157, 140, 145, 130, 135]

    print(  "Heights in increasing order: " + str( sorted(heights) )   )
    
    print( heights )


    print()
    print()

    # descending order, pass reverse=True inside the sort method

    sizes = [1, 4, 6, 90, 1, 43]

    print(sizes)

    print( sorted( sizes , reverse=True ) )    # descending order
    print()
    print()


    temp = sorted( sizes , reverse=True )

    print(temp)
    print(type(temp))

    


main()