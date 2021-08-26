def main():

    # IF ELSE LADDER/ CHAIN 

    marks = int( input("Enter total marks out of 100: ") )
    

    # if ( marks >= 90 ):
    #     grade = 'A'
    # if ( marks >= 80 and marks < 90):
    #     grade = 'B'
    # if ( marks >= 70 and marks < 80):
    #     grade = 'C'
    # if ( marks >= 60 and marks < 70):
    #     grade = 'D'
    # if ( marks >= 45 and marks < 60):
    #     grade = 'E'
    # else:
    #     grade = 'F'


    if ( marks >= 90 ):
        grade = 'A'
    elif ( marks >= 80 ):
        grade = 'B'
    elif ( marks >= 70 ):
        grade = 'C'
    elif ( marks >= 60 ):
        grade = 'D'
    elif ( marks >= 45 ):
        grade = 'E'
    else:
        grade = 'F'
    

if __name__ == "__main__":
    main()