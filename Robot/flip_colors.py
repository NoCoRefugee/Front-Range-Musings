#!/usr/bin/env Python3
from PIL import Image

# -------------------------------------------------------------------------------------------------
# todo list:
# 
#	1. I think you have to save the width/height, or just one, as a variable to pass around 
#	2. Write a function that turns the array back into a picture and saves it 
#	3. Write a function that makes some noticable change to the array before it gets re-pictured 
#	4. do a time check to see if it wouldn't be easier to just use image objects the whole time 
#	5. set vim to use spaces instead of tabs, just in case 
# 


# -------------------------------------------------------------------------------------------------

def go_get_the_image_and_load_it_in_the_array( theArray = [], *args ):

	with Image.open('pic1.jpg') as img1:

		width, height = img1.size

		for x in range(width-1):
			for y in range(height-1):
				theArray.append(img1.getpixel((x,y)))

# -------------------------------------------------------------------------------------------------

def print_out_part_of_array( theArray = [], *args ):

	arraySizeVariable = len(theArray)

	print(f"theArray.size => {arraySizeVariable}")
	print(f"last value @{arraySizeVariable-1} => {theArray[arraySizeVariable-1]}")
	print("\nHere are the first and last 10 values in the image array:\n")	

	for i in range(10):
		print(f"theArray[{i}] => {theArray[i]}")

	print("")
	for i in range(arraySizeVariable-10, arraySizeVariable):
		print(f"theArray[{i}] => {theArray[i]}")
	
	print()

# -------------------------------------------------------------------------------------------------

def change_image_around( theArray = [], *args ):
		
		for x in range(width-1):
			for y in range(height-1):
				a, b, c = img1.getpixel((x,y))
				b = 255-b
				img1.putpixel((x,y), ( c, b, a))

# -------------------------------------------------------------------------------------------------

def save_image( image ):
	img1.save('an_other_one.png')




# -------------------------------------------------------------------------------------------------

def main():

	thePicture = []

	print("\n-------------------\n")

	go_get_the_image_and_load_it_in_the_array(thePicture)

	print_out_part_of_array(thePicture)

	print("\n-------------------\n")

# -------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	main()


