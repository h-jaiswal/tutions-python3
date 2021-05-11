"""
048 
Ask for the name of somebody the user wants to invite 
to a party. 

After this, display the message “[name] has 
now been invited” 
and add 1 to the count. 

Then ask if 
they want to invite somebody else. Keep repeating this 
until they no longer want to invite anyone else to the 
party and then display how many people they have 
coming to the party. 

"""

def main():
    partyAttendeesCount = 0

    toInviteAnother = "y"
    while(toInviteAnother == "y" ):
        attendeeName = input("Enter name of the person to invite: ")
        print( attendeeName + " has been invited" )
        partyAttendeesCount = partyAttendeesCount + 1

        toInviteAnother = input("Do you want to invite anyone else? (y or n): ")

    print("Total people attending the party: " + str(partyAttendeesCount))
main()