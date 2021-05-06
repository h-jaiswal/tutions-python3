# 023 
# Ask the user to type in the first 
# line of a nursery rhyme and 
# display the length of the string. 
# Ask for a starting number and an 
# ending number and then display 
# just that section of the text 
# (remember Python starts 
# counting from 0 and not 1). 


    # NOTE - some escape characters 
    #  
    # NOTE  \n will print a new line 
    # NOTE  \t will print a tab space
    # NOTE  \r means carriage return 

    # NOTE  \\ is used to print a single back slash
    # NOTE  \" is used to print a double quote character
    # NOTE  \' is used to print a single quote character 

    # index starts from 0
    # position starts from 1

    # index = position - 1
    # in computers, we always start from 0 i.e. we always use index

def main():
    nurseryRhyme = input("Enter a nursery rhyme: \n") 

    startPostion = int( input("Enter position of a charcter (start): ") )
    endPostion = int( input("Enter position of a charcter (end): ") )
    
    startIndex = startPostion - 1
    endIndex = endPostion - 1

    partRhyme = nurseryRhyme[ startIndex : endIndex + 1]

    print(partRhyme)
main()
