    
    # bool is data type, variables of bool data type can store either True or False (without double quotes)
    # we'll study later in detail
    # example  a = True


def main():

    # input
    age = int(input("Enter age: "))
    hasVoterID =  input("Do you have a voter ID card?: ")
    
    if (hasVoterID == "True" or hasVoterID == "Yes"):
        hasVoterID = True 

    if (hasVoterID == "False" or hasVoterID == "No"):
        hasVoterID = False

    # if age >= 18 and hasVoterID:
    #     print("You can vote. Thank you.")
    # else:
    #     print("You cannot vote. Please come later.")

    # WAY 1
    
    if (age >= 18):
        if hasVoterID:
            print("You can vote.")
        else:
            print("You can vote only after getting a voter ID card.")
    else: 
        print("You cannot vote.")

    # WAY 2

    if ( age < 18 ):
        print("You cannot vote.")
    elif (hasVoterID):
        print("You can vote.")
    else:
        print("You can vote only after getting a voter ID card.")
    
main()