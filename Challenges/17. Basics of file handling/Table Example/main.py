def main():

    numbers = []

    # we will take input from a text file named input.txt which is already present in the same folder as our main.py file

    # file.read() # gives whole content of the file as a string

    # file.readlines()  gives a list of each line in the file, where each line is in the form of a string

    with open("input.txt", mode="r", ) as file:
        numbers = file.readlines()

    for number in numbers:
        number = int(number)

        output = []

        # calculate table for the number
        for i in range(1, 11):
            result = number * i
            finalResult = str(number) + " X " + str(i) + " = " + str(result)
            output.append(finalResult + "\n")

        output.append("\n")
        filename = "output" + str(number) + ".txt"
        with open(filename , mode="w", encoding="utf-8") as file:
            file.writelines( output )
    
main()