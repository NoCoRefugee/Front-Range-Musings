# or not... this has been modified to just put out the mersenne number that
# goes with the "n" of "num1"

# This PYTHON program should ask you for a number 'n', and then give you
# the result of (2^n) - 1.  It should store this number in a file
# for you, if you want it to.

# jlf  -  20200507

num1 = 50 

print("\n-------------------------------------------------------------------")

# ask the user for an 'n' to use in computing the mersenne number
# inp1 = input("give me an exponent to work with and I will make you a mersenne number from it: ")

# convert that input to an integer
# num1 = int(inp1)

print()
print("from a Python3 program")
print(f"Mersenne ( 2^{num1} ) - 1 is => ")
#print("you gave me => ", num1 )
#print("type for variable num1 is: ", type(num1))
print()


num2 = (2**num1) - 1
#print(f"(2^n) - 1 for that number is: \n{num2:,}")
print(f"\n{num2:,}")

#print()
# inp2 = input("Shall I store that number in a file for you? (y/n)")
#print()

# if inp2 == "y":
#	print(f"you said Yes")
# else:
#	print(f"you said No")


# fileName = "Mersenne_number_data/mersenne_number_2^" + inp1 + "-1"

# print("filename is => ", fileName)

# if inp2 == "y":
#	f = open(fileName, "w+" )
##	f.write(str(num2))
#	f.close()

print("\nLength of this mess is => ", len(str(num2)))

print("\n-------------------------------------------------------------------\n")


