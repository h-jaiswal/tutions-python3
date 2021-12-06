from os import linesep


def main():


    # we will take input from a text file named input.txt which is already present in the same folder as our main.py file

    # file.read() # gives whole content of the file as a string
    # fileContent = ""
    # file -> first line has 23, 2nd line has 95, 3rd line 8
    # fileContent = file.read()
    # fileContent will store "23\n95\n8"   where \n is newline character

    # file.readlines()  gives a list of containing all lines of a file, where each line is in the form of a string
    # line 1 ->  lines[0] , line 2 -> lines[1]   and so on,  last line -> lines[n-1]
    # file -> first line has 23, 2nd line has 95 
    # lines = file.readlines()
    # lines will store ["23", "95"]

    lines = []


# C:/Path/To/File/file.txt   called Absolute Path
# ../../Folder/file.txt   example of Relative Path
# file.txt   picks from current folder where program is running from (base folder)

# . means current folder,   .. means parent folder

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

    # 
    data = ["line1", "line2", "line3"]

    for i in range(len(data)):
        data[i] = data[i] + "\n"

    filename = "output1.txt"   
    with open(filename , mode="w", encoding="utf-8") as file:
        file.writelines( data )

    data = ["line1", "line2", "line3"]
    for i in range(len(data)):
        data[i] = data[i] + "\n"
    filename = "output1.txt"   
    with open(filename , mode="a", encoding="utf-8") as file:
        file.writelines( data )

    
main()