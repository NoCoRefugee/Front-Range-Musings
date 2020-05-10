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

def doIt(int1):

	decimal.getcontext().prec = 100

	return decimal.Decimal(int1)*decimal.Decimal(int1)

# ------------------------------------------------------------------------------------------

def main():
	makeLine()

	print("what is the Limit as x -> 0 of x^x?")

	decimal.Decimal(num) = decimal.Decimal(0.1)
	for x in range(20):
		print(doIt(decimal.Decimal(num)))
		print("decimal.Decimal(num) => ", decimal.Decimal(num))
		decimal.Decimal(num) = decimal.Decimal(num) / 10

	makeLine()

# ------------------------------------------------------------------------------------------

main()

# ------------------------------------------------------------------------------------------

