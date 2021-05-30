import sys

def main():

    # taking filename from the first command line argument
    if ( len(sys.argv) > 1) :  
        inputFileName = sys.argv[1] 
    else:
        print("Please provide file name as first command line argument")
        
        # below line safely exits from the program
        sys.exit(0)

    inputLineByLine = []      # list variable to store input from file

    with open( file = inputFileName , mode = "r" , encoding="utf-8" ) as file:
        inputLineByLine = file.readlines()

    for line in inputLineByLine:
        name = line
        print("Hello " + name)

main()


# def main():

#     # name = input("Enter your name: ")
#     # print("Hello " + name)

# main()