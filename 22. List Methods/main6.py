def main():

    # CRUD- Create , Read, Update, Delete

    # 1. delete or remove

    list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    # 1.1 Delete an item at a particular index
    # EXAMPLE :

    print(list1)  # [10, 20, 30, 40, 50, 60, 70, 80, 90]

    del list1[3]    
 
    print(list1)  # [10, 20, 30, 50, 60, 70, 80, 90] 


    # 1.2 Deleting a range of values starting from a particular index i (include) upto a particular index j (excluded)


    # 1.2.1 BASIC METHOD using for loop

    # del list1[2]
    # del list1[2]
    # del list1[2]
    # del list1[2]

    # if we want to remove 4 items starting from item at index i=2

    for i in range(4):
        del list1[2]


    list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    # to delete 3 items starting from item at index 4  

    for i in range(3):
        del list2[4]



    # 1.2.2 USING del with a range of list value


    list3 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    # if in above list, you want to delete from 40 to 70 i.e. from index no. 3 to index no. 6

    # del list_name[i:j+1]

    print(list3)

    del list3[3:7]

    print(list3)



    # 2. Removing item using its item_value, using remove method

    list4 = [10, 20, 30, 40, 50]

    print(list4)

    list4.remove( 50 )

    print(list4)


    # 3. To add a new item at the end of the list, we using append() method

    list5 = [10, 20, 30]

    list5.append(40)
    list5.append(50)


    # 4. To remove an item from the end of the list, using pop() method


    list6 = [10, 20, 30, 40]
    list6.pop()

    print(list6)


    # pop() method removes the last item and returns it

    list7 = [10, 20, 30, 40]

    last_value = list7.pop()

    print(last_value)


    # 5. To insert an item at a particular index anywhere in the list, we use insert() method

    # usage-    list_name.insert(index, item_value)

    list8 = [10, 20, 30, 40, 50]

    list8.insert(3, 35)

    print(list8)    #[10, 20, 30, 35, 40, 50]

    list8.insert(5, 45)

    print(list8)    #[10, 20, 30, 35, 40, 45, 50]

    list8.insert(7, 55)
    
    print(list8)




    # 6. index() method with three arguments

main()