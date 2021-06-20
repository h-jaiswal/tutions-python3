def main():

    # ways to create a list collection

    # one way is to use [] brackets with item_values seperated by comma

    names_list = []  # empty list

    names_list2 = ["Harsh", "Rishav", "Palak"]



    # to modify or change value at an index ->

    # eg. to change value at index 1 i.e. "Rishav" to "Peter"
    # usage -    list_name[index] = new_value
    
    names_list2[1] = "Peter"



    # another way is to list()  with item_values seperated by comma

    names_list3 = list(( "Harsh", "Rishav", "Palak" ))

    

    # we can also find index value of a particular item in the list
    # list_name.index( item_value )

    index = names_list2.index("Harsh")



    # to get number of items present in a list a collection we use len()

    noOfItems = len( names_list2 )




    # we can change a list collection
    # it means we can add or remove items from a list collection
    # note : we cannot change a tuple collection, we cannnot add or remove items from a tuple once created


    # to a items to a list, we use append(), which adds the item_value at the end of the current list
    # list_name.append( item_value )

    names_list2.append( "Frank" )   # now names_list2 = ["Harsh", "Rishav", "Palak", "Frank" ]
    names_list2.append( "David" )    # now names_list2 = ["Harsh", "Rishav", "Palak", "Frank", "David" ]





    # remove element using elements index

    # to remove the last item from a list
    # we use pop() function
    # listname.pop()

    names_list3.pop()     # list becomes -> ["Harsh", "Rishav"]

    # if we want to remove i.e delete "Palak" from this list, we can use its index value which is as shown below, names_list2 = ["Harsh", "Rishav", "Palak", "Frank", "David" ]

    # "Palak" is at 3rd position in list, therfore it's index is 3-1 i.e. 2 
    # to remove Palak, using its index value, we can write

    del names_list2[2]

    # now names_list2 becomes = ["Harsh", "Rishav", "Frank", "David" ]



    # we can also remove items using its value
    # for example if we want to remove "David"

    names_list2.remove("David")

    # now names_list2 becomes = ["Harsh", "Rishav", "Frank"]





    # we can access the items of a list collection using the index of a particular
    # list_name[ index_value ]
    second_item_value = names_list2[1]




    

    # we can store same type of items and mixed type of items in a collection, i.e. the data type (integer, float, string, etc) do not matter.

    items = [2, "Hi", "Jacob", 3.14, "table", 21]

    heights = [ 1.7, 1.2, 1.5, 1.6]

    shoppingItems = ["coffee", "pen", "chips"]
    

    # one more things, the item values can repeat, i.e. two items can have same value in a tuple or list

    shoppingItems = ["coffee", "pen", "chips", "pen", "chips", "chips"]

    