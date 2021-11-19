from os import linesep


def main():

    lines = []

    # we will take input from a text file named input.txt which is already present in the same folder as our main.py file

    # file.read() # gives whole content of the file as a string

    # file.readlines()  gives a list of each line in the file, where each line is in the form of a string

# FileNotFoundError: WHEN file does not exist
    with open("input.txt", mode="r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        print(line)


    # file output
    data = "xyzkjfuhafhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh   iuf iufy eriufhe iuf;erhf f fiu ru fufg iuf vg\n hhhhhhhhhhhlokaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"  # str type
    filename = "output.txt"        
    with open(filename , mode="w", encoding="utf-8") as file:
        file.write( data )
        
    # write -> str data   (\n works for new line)
    # writelines ->   list data   (every item in the list takes a new line in output file)
    
main()