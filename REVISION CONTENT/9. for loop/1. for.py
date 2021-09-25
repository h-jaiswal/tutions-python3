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
    # loop variable -> name
    # names = ["A", "B", "C", "D"]   
    # len(names) is FOUR (four items)
    # loop runs -> FOUR times because names list contains FOUR items
    # name ->  { first time = "A" , second time = "B" , third time = "C", fourth time = "D" }
    names = ["A", "B", "C", "D"]

    for name in names:
        print(name)




    print()
    
    names = ("A", "B", "C", "D")

    for name in names:
        print(name)



    print()

    # for with dictionary


    # way 1 

    student = {  # dictionary has 3 items (= 3 key-value pairs)
        'name' : 'Rishav',
        'roll' : 101,
        'age' : 14
    }

    for k,v in student.items():
        print("{} has value {}".format(k, v))

    print()
    # changed name of loop variable for key and value
    for key,value in student:
        print("{} has value {}".format(key, value))

    for key,value in student:
        print(key)

    for key,value in student:
        print(value)



    # way 2

    # looping over values of a dictionary
    for v in student.values():
        print(v)

    # way 3

    # looping over keys of a dictionary
    for k in student.keys():
        print(k)

    for k in student.keys():
        print(student[k])
    
    for k in student.keys():
        print("{} has value {}".format(key, student[k]))

    for k in student.keys():
        value = student[k]
        print("{} has value {}".format(key, value))
        
main()