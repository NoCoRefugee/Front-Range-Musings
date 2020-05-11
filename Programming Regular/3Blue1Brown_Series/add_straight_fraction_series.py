#! /usr/bin/env python3
from os import system as screenThing


# This program is going to add series' together as I follow along on the
# 3Blue1Brown natural logarithm video on youTube

def mL():
	print("\n-------------------------------------------------------------\n")

def simplest_series():
#	This function runs the 1/x + 1/(x+1), 1/(x+2)... 1/(+n) series.  Instead of printing out the
#	running sum of this series we are counting the number of terms that start with each digit.
#	So, there are three terms that start with a 1 ( 1, 1 1/2, 1 5/6... ) then seven that start with 
#	a 2, and so on.  	

	double_checking = 1
	track_for_each_digit = []
	series_sum = 0
	sub_total_sum_so_far = 0	
	counter1 = 2
	upper_limit_1 = 5000	

	print("This function runs the 1/x + 1/(x+1), 1/(x+2)... 1/(+n) series.  Instead of printing out the")
	print("running sum of this series we are counting the number of terms that start with each digit.")
	print("So, there are three terms that start with a 1 ( 1, 1 1/2, 1 5/6... ) then seven that start with ")
	print("a 2, and so on.")
	print()
	print(f"The computer is currently running that series out to {upper_limit_1:,} terms.")
	print()

	for i in range(1, upper_limit_1):
		series_sum = series_sum + 1/i
		sub_total_sum_so_far = sub_total_sum_so_far + 1				

		if ( series_sum + 1/(i+1) > counter1 ):
			track_for_each_digit.append(sub_total_sum_so_far)
			sub_total_sum_so_far = 0
			counter1 = counter1 + 1

	track_for_each_digit.append(sub_total_sum_so_far)

	i = 1
	for x in track_for_each_digit:
		print(f"{i:,}s =>\t{x:,}")
		double_checking = double_checking + x
		i = i + 1

	print()
	print("*The last number is almost certainly incomplete.")
	print()
	print("The series sum at the end was => ", series_sum) 
	print(f"and that is after {upper_limit_1:,} additions.")
	print("This series grows infinitely, and slowely.")
#	print(f"double_checking => {double_checking:,}")

	# later, have this thing return the something, so it can run through different
	# size searches and maybe compare them to guess where the thing will flatten out

def main():

	# see line 2 of this program => from os import system as screenThing
	screenThing("clear")

	mL()
	
	simplest_series()

	mL()


main()











