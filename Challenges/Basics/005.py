# 005 
# Ask the user to enter three 
# numbers. Add together the first 
# two numbers and then multiply 
# this total by the third. Display the 
# answer as The answer is 
# [answer]. . 

def main():
	num1 = int( input("Enter number 1: ") )
	num2 = int( input("Enter number 2: ") )
	num3 = int( input("Enter number 3: ") )
	
	answer = (num1 + num2) * num3
	print("The answer is " + str(answer))

main()
