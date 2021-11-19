def main():
    student = { "name" : "Harshit" ,
        "rollNo" : 101 ,
        "marks" : 98 ,
        "mobileNo" : 851904620
    }

    print(student["name"])
    print(student["rollNo"])
    print(student["marks"])
    print(student["mobileNo"])

    print()

    for key,value in student.items() :
        print(value)


    for key,value in student.items():
        print(student[key])


    
    print()
    print()


    for value in student.values():
        print(value)


    for key in student.keys() :
        print(key)          # key
        print(student[key]) # value
        print()


    print()
    print()


    all_values_only = student.values()

    print(all_values_only)

    # print(student.values())

    all_key_only = student.keys()

    print(all_key_only)

    print(student.keys())

    # dict_values(['Harshit', 101, 98, 851904620])

    # dict_keys(['name', 'rollNo', 'marks', 'mobileNo'])




    # to clear all key value pairs i.e. all items in a dictionary, we use clear() method

    print()
    print()

    print(str(student))

    student.clear()

    
    print()
    print()

    print(str(student))


main()