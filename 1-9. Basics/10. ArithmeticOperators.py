def main():
	a = float( input("Enter a number: ") )
	b = float( input("Enter a number: ") )

	sum = a + b
	print("Sum: " + str(sum))

	difference = a - b
	print("difference: " + str(difference))

	division = a / b
	print("division: " + str(division))
	
	multiply = a * b
	print("multiply: " + str(multiply))

	quotient = a // b
	print("quotient only or integer division result: " + str(quotient)) 

	remainder = a % b
	print("remainder or modulos: " + str(remainder))

main()
