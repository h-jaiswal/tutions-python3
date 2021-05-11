"""
Ask the user to enter a 
number and then enter 
another number. Add these 
two numbers together and 
then ask if they want to add 
another number. If they 
enter “y", ask them to enter 
another number and keep 
adding numbers until they 
do not answer “y”. Once the 
loop has stopped, display 
the total.
example

12
3
sum = 15
another no to add? y
num = 5
sum = sum + num = 15 + 5 = 20
another no to add? y
num = 7
sum = sum + num = 20 + 7 = 27
another no to add? n

total = 27
"""

def main():
    num1 = int(input("Enter a number: "))

    num2 = int(input("Enter another number: "))

    sum = num1 + num2

    toRepeat = input("Do you want to add another number? (y or n): ")

    while( toRepeat == "y" ):
        num3 = int(input("Enter another number: "))
        sum = sum + num3
        
        toRepeat = input("Do you want to add another number? (y or n): ")

    print("Total: " + sum)

main()





# def main():
#     num1 = int(input("Enter a number: "))

#     num2 = int(input("Enter another number: "))

#     sum = num1 + num2

#     toRepeat = "y"  # Assume, according to question, y means repeat and n means no repeat
#     while(toRepeat == "y"):
#         toRepeat = input("Do you want to add another number? (y or n): ")
#         if(toRepeat == "y"):
#             num3 = int(input("Enter another number: "))
#             sum = sum + num3