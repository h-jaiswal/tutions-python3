def main() :
    age = int(input("Enter your age = "))

    # WAY 1

    if age >= 18 :
        print("Allowed to vote")
    else :
        print("You are not allowed to vote")



    # WAY 2

    isAllowedToVote = False # assume, by default, that not allowed to vote

    if ( age >= 18 ):
        isAllowedToVote = True


    if (isAllowedToVote):
        print("Can Vote")
    else:
        print("Cannot Vote")


    
main() # call main()