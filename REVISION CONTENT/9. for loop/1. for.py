def main():

    # print Hi for 10 times

    for i in range(10):  # i -> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        print("Hi")


    print()


    # print Hi for 5 times

    for i in range(5):  # i -> {0, 1, 2, 3, 4}
        print("Hi")


    print()

    
    # run for loop for  i  ->> {1, 2, 3, 4, 5}

    for i in range(1, 6):
        print(i)

    
    # run for loop where loop variable changes from 1 to n like -> {1,2,3,4,5,6, ......., n-1, n}
    n = 8

    for i in range(1, n+1):
        print(i)

    
    # Analysis in below for loop
    # loop variable ->  item 
    # range(2,10,2) ->  {2, 4, 6, 8}
    # loop runs -> FOUR times because range function gives FOUR items
    # item -> {2, 4, 6, 8}

    for item in range(2, 10, 2):
        print(item)



    print()



    # Analysis for below for loop
    # loop variable ->  
    names = ["A", "B", "C", "D"]

    for name in names:
        print(name)
main()