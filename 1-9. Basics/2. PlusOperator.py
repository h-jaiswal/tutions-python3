# operator 
# operand


# left and right both numbers

print(1 + 1)  # number addition

print(2 + 2)  # number addition

print(3 + 9)  # number addition



# left and right both strings

print("2" + "1")  # string addition OR fevicol horha OR string concatenation

print("Rishav" + "Nath") # string addition OR fevicol horha OR string concatenation



# one number and one string WILL GIVE ERROR

# print( 1 + "2" )

#print ( "Hi" + 5 )

#print( "89" + 11 )


# SOLUTION of above issue

# convert either string operand to int type IF POSSIBLE OR convert integer operand to str type IF POSSIBLE


print( str(1) + "2" )  # string addition

print( 1 + int("2") )  # number addition

print( "Hi" + str(5) )  

# print( int("Hi") + 5)

# Traceback (most recent call last):
#  File "IntegerInput.py", line 42, in <module>
#    print( int("Hi") + 5)
# ValueError: invalid literal for int() with base # 10: 'Hi'



print( int("89") + 11 )  # number addition

print(  "Hi" + str(11) )     # string addition




