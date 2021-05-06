# 026 
# Vowel - a, e, i, o, u ( 5 vowels )
# consonant - alphabets other than vowel ( 26 - 5 = 21 consonants)

# QUESTION
# A Pig named Latin takes the first letter of a word,
# and if it is a consonant then it 
# moves the consonant to the end of the word and adds on an 
# “ay”. 
# 
# If a word begins with a vowel you just add 
# “way” to the end. 
# 
# For example, pig becomes igpay, 
# banana becomes ananabay, and aadvark becomes 
# aadvarkway. 
# 
# Create a program that will ask the 
# user to enter a word and change it as per Pig Latin. 
# Make sure the new word is displayed in lower case. 


# NOTE THEORY:
# nth letter in a string can be found using [] brackets 
# letter at nth index is string_name[n]
# remember, index = position - 1
# example, 1st position index is 0, firstLetter = word[0]
# example, 4th position index is 3, fourth_letter = word[3]

# NOTE THEORY:

# # WAY 1 using "in" operator 
#     if (firstLetter in "aeiou"):
#         # true i.e. is a vowel
#     else:
#         # false i.e. is not a vowel i.e it is a consonant
 
#     # WAY 2 using combinations "or" and "==" operators 
#     if( firstLetter == 'a' or firstLetter == 'e' or firstLetter == 'i' or firstLetter == 'o' or firstLetter == 'u'):
#         # true i.e. is a vowel
#     else: 
#         #  false i.e. is not a vowel i.e it is a consonant

def main():
    word = input("Please enter a word: ")

    firstLetter = word[0]

    if (firstLetter in "aeiou"):
        # true i.e. is a vowel

        result = word + "way"
    else:
        # false i.e. is not a vowel i.e it is a consonant

        remainingWord = word[1:] # will give part of word from position 2 (i.e. index 1) till last 
        result = remainingWord + firstLetter + "ay"

    print( result.lower() )

main()