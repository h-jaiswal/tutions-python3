from typing import ItemsView


def main():

    shoppingList = []         # empty list

    print("My shopping list = " + str(shoppingList) )
    
    num = int( input("How many you want to buy? ") )

    # 1 way to input a list
    for i in range(num):
        itemValue = input("Enter item name: ")
        shoppingList.append(itemValue)


    # 2 ways to print a list

    for i in range(num):
        print( shoppingList[i] )    
    
    # or
    
    for item in shoppingList:
        print( item )


main()