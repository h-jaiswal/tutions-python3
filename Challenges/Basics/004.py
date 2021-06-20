# 004 
# Ask the user to enter 
# two numbers. Add 
# them together and 
# display the answer as 
# The total is 
# [answer].

def main():
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	answer = num1 + num2

	print("The total is " + str(answer))

main()