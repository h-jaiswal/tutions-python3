def main():

    # 5. Combining items of two different lists in one single list using the + operator 

    rishavList = ["GTA", "Notebooks", "Bicycle"]

    harshitList = ["Pens", "Hard disk", "Cover"]

    shoppingList = rishavList + harshitList

    print( str(shoppingList) )


    # Note - when we use + operator -> what happens is we combine two already existing list to create a new single list containing items from both lists


    # extend() method

    list1 = [1, 2, 3, 4, 5 ]

    list2 = [6, 7, 8, 9]

    # if we want to add all items of some list2 to an already existing list1 


    print(list1)
    print(list2)

    list1.extend( list2 )

    print(list1)
    print(list2)


main()