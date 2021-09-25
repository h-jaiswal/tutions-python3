def main():

    name = input("Please enter name - ")
    print("Name - '{}'".format(name))

#  ValueError comes during when we the input provided is not of required

    age = int( input("Please enter age - ") )
    print("Age - {}".format(age))

    height = float( input("Please enter height - ") ) 
    print("Height - {}".format(height))


    # isBoy = bool( input("Are you a boy (true or false) - ") )          # WRONG WAY

    # 0

    if ( input("Are you a boy? (yes or no) - ").lower() == "yes"):
        isBoy = True
    else:
        isBoy = False

    # 1
    isBoy = False    # Assume

    if ( input("Are you a boy? (yes or no) - ").lower() == "yes"):
        isBoy = True

    print("isBoy - {}".format(isBoy))


    # 2
    isBoy = input("Are you a boy? (yes or no) - ").lower()
    if (isBoy == "yes"):
        isBoy = True
    elif(isBoy == "no"):
        isBoy = False
    else:
        print("Invalid Input")
        isBoy = ""
    
    print("isBoy - {}".format(isBoy))
    

    # 3
    isBoy = False
    answer = input("Are you a boy? (yes or no) - ")
    if ( answer.lower() == "yes" ):
        isBoy = True 

if __name__ == "__main__" :
    main()