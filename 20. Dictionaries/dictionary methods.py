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



main()



