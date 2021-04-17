def main():
    billAmount = int(input("Enter total amount: "))
    amountPaid = int(input("Enter amount paid: "))

    if amountPaid >= billAmount :
        
        changeAmount = amountPaid - billAmount

        print("Thank you.")

        if changeAmount != 0 :  # != means not equal to
            print("Your change amount is " + str(changeAmount))
        
        print("Please visit again.")

    else :
        print("Excuse me. Please pay the full amount.")

main()