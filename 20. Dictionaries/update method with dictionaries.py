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

#   After user1.update(user2), user1 becomes as shown below, while user2 remains unchangeds
    # user1 = {
        
    #     "lastLogin" : "5 hours ago"
    #     "name" : "Harshit",
    #     "score" : 99999,
    #     "username" : "farrago",
    #     "totalScore" : 9999999999
    # }



    print(str(user1))
    print()

    print(str(user2))


main()