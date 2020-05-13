#! /usr/bin/env python3
import decimal

#
# this doesn't work.  figure it out.
#



'''
	JLF  -  April 27, 2020

	We were watching Eddie Woo talk about zero^zero = 1 and the 
	limit and we decided to write this little program to test that
	idea for outselves.  What happens as lim x->0 x^x?
'''
# ------------------------------------------------------------------------------------------


def makeLine():
	print()
	print('*****************************************************************')
	print()

# ------------------------------------------------------------------------------------------

def main():
	makeLine()

	print("what is the Limit as x -> 0 of x^x?")

	decimal.getcontext().prec = 20 

	num1 = decimal.Decimal(0.0000001)

	print("num1 => ", num1)

	print("0.0000001 => ", 0.0000001)

	makeLine()

# ------------------------------------------------------------------------------------------

main()

# ------------------------------------------------------------------------------------------

