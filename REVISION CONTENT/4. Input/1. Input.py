def main():

    name = input("Please enter name - ")
    print("Name - '{}'".format(name))

#  ValueError comes during when we the input provided is not of required

    age = int( input("Please enter age - ") )
    print("Age - {}".format(age))

    height = float( input("Please enter height - ") ) 
    print("Height - {}".format(height))


    # isBoy = bool( input("Are you a boy (true or false) - ") )          # WROND

    isBoy = False    # Assume

    if ( input("Are you a boy? (yes or no) - ").lower() == "yes"):
        isBoy = True

    print("isBoy - {}".format(isBoy))

if __name__ == "__main__" :
    main()