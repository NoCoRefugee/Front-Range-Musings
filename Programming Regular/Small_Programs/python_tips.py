#!/usr/bin/env python3




#---------------------------------------------------

def makeLine():
	print(); print(); 
	print("--------------------------------"); 
	print(); print();

#---------------------------------------------------

makeLine()

#---------------------------------------------------

# ternary conditional:

x = 9
y = 0

y = 1 if x == 1 else 2

#	y becomes 1 if x is 1, if x is not 1 then y becomes 2

print("ternary operator thing:")
print("x = ", x)
print("y = ", y)
print("y = 1 if x == 1 else 2")
print("makes y => ", y)


makeLine()


#---------------------------------------------------

# underscores as seperators in numbers
# python ignores the underscores and treats this as numbers
# the point of this is to make it more readable to you

num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print("Normal sort of number output => ")
print(total)
print()
# f string syntax for adding commas to output in numbers:
print("# f string syntax for adding commas to output in numbers:")
print()
print("this => print(f'{some_number:,}') cause this to happen =>")
print(f'{total:,}')


makeLine()

#---------------------------------------------------

# something about context managers
print("something about context managers.")

makeLine()

#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------





