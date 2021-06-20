# 022 
# Ask the user to enter their first name and surname in any 
# case. Change the case to title case and join them together. 
# Display the finished result. 


def main():
    firstName = input("Please enter first name: ")
    surName = input("Please enter surname: ")  

    fullName = firstName.title() + " " + surName.title()

    print( fullName )

main()