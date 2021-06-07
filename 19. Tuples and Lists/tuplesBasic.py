def main():
    
    # ways to create a tuple collection

    # note - variable name can be anything

    # first way is to use () simple brackets

    fruits_tuple = ("apple", "kiwi", "watermelon")

    tuple1 = (2, 80, -1, -4, 0, 23, 2.4, "String", "Another String", 90)

    # another way is using tuple() function/constructor

    fruits_tuple2 = tuple((  "apple", "kiwi", "watermelon", "mango"  ))



    # to get the number of items present in a tuple, we can use len() function

    noOfFruits = len(fruits_tuple)



    # every item in a tuple is ordered. it means every item in a tuple has a fixed index value

    # first item's index value = 0
    # second item's index value = 1
    # third item's index value = 2

    # last item's index value = totalItems - 1

    # always remember, index = position - 1




    # we can access item value at a particular index, 
    # for example, item with index_value i is tuple_name[index_value]

    third_item_value = fruits_tuple[2]



    # we can also access the index value of a particular item whose value is known

    # for example, item with item_value will have index = tuple_name.index(item_value)
    index_value_of_kiwi = fruits_tuple.index("kiwi")





    # we can store same type of items and mixed type of items in a collection, i.e. the data type (integer, float, string, etc) do not matter.

    items = (2, "Hi", "Jacob", 3.14, "table", 21)

    heights = ( 1.7, 1.2, 1.5, 1.6)

    shoppingItems = ("coffee", "pen", "chips")