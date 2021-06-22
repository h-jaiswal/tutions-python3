def main():


    user = {
        "name" : "Rishav",
        "username" : "striver",
        "score" : 99
    }


    print( str(user) )

    # for k,v in user.items():
    #     print("{} - {}".format(k,v))


    print(user.get("name"))
    print(user.get("score"))



    user2 = user.copy()

    # dictionary_1.update(dictionary_2)
    

    print(str(user))

    # user.items()
    # user.values()
    # user.keys()

    user.clear()

    print( str(user) )


    student = {
        # "name" : "Harshit Jaiswal"

        "name" : {
            "firstName" : "Harshit",
            "middleName" : "",
            "lastName" : "Jaiswal",
            "userName" : "farrago"
        },

        # "age" : 21

        "dateOfBirth" : {
            "day" : 30,
            "month": 3,
            "year" : 2000
        },

        # "standard" : 7 

        "stardard" : {
            "standard" : 7,
            "section" : "A"
        },      

        # marks : 96,

        # # -1 means Absent on test day
        # marks : [10, 94, 78, -1, 76]

        # -1 means Absent on test day
        "marks": {
            "maths" : 10,
            "science" : 94,
            "english" : 78,
            "social" : -1,
            "hindi" : 76
        }
    }

# main()



def main2() :

    user1 = {
        "name" : "Harshit",
        "score" : 99,
        "username" : "striver",
        "lastLogin" : "5 hours ago"
    }

    user2 = {
        "name" : "Harshit",
        "score" : 99999,
        "username" : "farrago",
        "totalScore" : 9999999999
    }

    print()

    print(str(user1))
    print()

    print(str(user2))
    print()

    user1.update(user2)

    print(str(user1))
    print()

    print(str(user2))


main2()