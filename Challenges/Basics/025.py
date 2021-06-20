# 025 
# Ask the user to enter their first name. If the length 
# of their first name is under five characters, ask 
# them to enter their surname and join them 
# together (without a space) and display the name 
# in upper case. If the length of the first name is five
# or more characters, display their first name in 
# lower case

def main():
    firstName = input("Please enter first name: ")
    if ( len(firstName) < 5 ):
        surName = input("Please enter surname: ")

        # print(firstName + " " + surName)
        print(firstName + surName) # no space in between firstname and surname
    else:
        # print( firstName )
        print( firstName.lower() )  # firstName in lower case

main()