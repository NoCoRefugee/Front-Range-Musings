#! /usr/bin/env python3
from decimal import *


# JLF  -  20200502

# 	This program plays with decimal precision while working on a numberphile division
# 	problem that they showed with James Grimes.  1 / 998001 is supposed to produce all 3 digit
# 	numbers in order up to 997, skip 998, then do 999 000 001 and start the whole thing over again.
# 	We are seeing if we can reproduce that here.

#	The video goes on to say that this works with the powers of 9.  998001 is 999^2.  99^2 is 9801, etc.
#	Maybe later try it with those also, and check on whether it actually repeats.



def makeLine():
	''' This function makes a nice line of asterix on the screen when called '''

	print()
	print()
	print("******************************************")
	print()
	print()



def makeOtherNumber():
	''' This function makes a big decimal number with excessive precision. '''

	# this part sets the precision used.  We used 3020 so it would be bigger than
	# needed and not cause an error when we convert this to a string.	
	getcontext().prec = 3020 
	
	# this is our decimal division as stated in problem description at top of this file
	return (Decimal(1) / Decimal(998001))



def convertToStringAndShow(bigNum):

	# make a big number and convert it to a string to make the output
	# more easily formated
	bigNumConvertedToString = str(bigNum)

	# This outputs the number as a string with formating
	for i in range(2,3002):
		print(bigNumConvertedToString[i], end = '')
		if ( (i-1)%3 == 0 ):
			print(' ', end = '')



def main():

	makeLine()

	print("Here is the number (1 / 998001) =>  ( '0.' removed for symetry. )")
	print()

	bigNum = makeOtherNumber()

	convertToStringAndShow(bigNum)

	print()
	print()
	print("Apparently this number repeats indefinitely.")

	makeLine()


main()
