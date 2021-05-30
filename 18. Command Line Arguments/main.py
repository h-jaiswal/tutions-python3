import sys

def main():
    # sys.argv[0] contains the location of the current file if run from any other folder than its current folder. 
    # Otherwise if run from its current folder, then sys.argv[0] contains the file name only

    fileLocation = sys.argv[0]

    print(fileLocation)

    print( len(sys.argv) ) 

    # If provided, then first command line argument is stored in sys.argv[1]

    # If provided, then second command line argument is stored in sys.argv[2]

    # If provided, then third command line argument is stored in sys.argv[3]

    numberOfCommandLineArguments = len(sys.argv) - 1

    for i in range( 1, numberOfCommandLineArguments + 1):
        argumentValue = sys.argv[i]
        print(argumentValue)

    # If the argument is not provided, and we try to access it using sys.argv then it will an error
    # print( sys.argv[4] )   # will give error if 4th command line argument
    
main()