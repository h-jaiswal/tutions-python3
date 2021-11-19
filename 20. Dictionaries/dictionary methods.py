def main():


    user = {
        "name" : "Rishav",
        "username" : "striver",
        "score" : 99
    }

    # user = {}    # empty dict.

    # user = {
    #     "name" : {
    #         "first" : "Rishav",
    #         "middle": "",
    #         "last": "Kumar"
    #     },
    #     "username" : "striver",
    #     "score" : 99
    # }

    print( str(user) )

    print(user["name"])
    print(user["score"])
    print()
    print(user.get("name"))
    print(user.get("score"))



    user2 = user.copy()

    # dictionary_1.update(dictionary_2)
    

    print(str(user))
    print(user.items())
    print(user.values)
    print(user.keys())

    # user.items()
    # user.values()
    # user.keys()

    user.clear()

    print( str(user) )



main()



