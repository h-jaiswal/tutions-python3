# Ask the user to enter their first name and then ask them to 
# enter their surname. Join them together with a space between 
# and display the name and the length of whole name. 

def main():
    firstName = input("Please enter first name: ")
    surName = input("Please enter surname: ")  
    # shift + alt + down arrow is used duplicate a line

    fullName = firstName + " " + surName
    length = len( fullName )

    print( fullName )
    print( length )

main()