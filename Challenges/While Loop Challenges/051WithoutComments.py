
def main():
    num = 10
    answer = -1    # setting answer to a default value 
    while( answer != num and num != 0):
        poem = "There are " + str(num) + " green bottles\nhanging on the wall,\n" + str(num) + " green bottles hanging on the wall,\nand if 1 green bottle\nshould accidentally fall"
        print(poem)
        answer = int(input("How many green bottles will be hanging on the wall? "))
        num = num - 1 
        if( answer != num and num != 0 ):
            print("No, try again.")

    if  (num == 0):
            print("There are no more green bottles hanging on the wall")
    else:
        print("There will be " + str(num) + "green bottles hanging on the wall")
main()
