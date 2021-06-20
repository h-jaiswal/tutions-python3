def main():
    student = {
        "name": "Harshit",
        "rollNo": 20,
        "standard" : 7,
        "marks": 78
    }



    # accessing a value using its key
    # dictionary_name[ "key_name" ]

    print( student["name"] )

    rollNo = student["rollNo"]
    print(rollNo)

    student["standard"] = student["standard"] + 1

    # student["marks"]





    # modify or change the value stored at a particular key to any new_value (may or may not be of same data type)

    # dictionary_name["key_name"] = new_value

    student["name"] = "Peter"

    student["rollNo"] = 21

    student['marks'] = {
        "science" : 20,
        "maths" : 98
    }


    # print( student["address"] )       # keyError



    # marks = [10, 20, 30]

    # print( str(marks) )

    print( str(student) )

main()