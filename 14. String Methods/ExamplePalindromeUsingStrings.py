# A string which remains unchanged if it is reversed is called a palindrome string/numer

# in other words if reverse of a string is same as the original string, then it is called palinrome string/number

# example

# MADAM  - MADAM

# 10901  - 10901

# LOL  - LOL

def main():

    word = input("Enter a word or number: ")

    reverse_word = word[-1: :-1]

    if ( word == reverse_word ):
        print( word + " is a palindrome")
    else:
        print( word + " is not a palindrome")

main()