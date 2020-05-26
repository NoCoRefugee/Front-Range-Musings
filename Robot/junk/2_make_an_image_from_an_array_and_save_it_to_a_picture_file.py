#!/usr/bin/env python3
from PIL import Image

# -----------------------------------------------------------------------
# todo List:
#	make the array 2 dimensional


# -----------------------------------------------------------------------

def go_get_the_image_and_load_it_into_the_array(the_name_of_the_picture_file):

# 	This function loads an image from a file and returns the size of that
#	image and an array with that image's pixel data.

#	This function needs these external variables to exist:
#		thePictureArray = [list]
#		pictureSize = [list] 
#		the_name_of_the_picture_file = "file name string"

#	jlf  -  20200525


	theArray = []

	# show_progress_on_screen is just for trouble shooting, remove later
	show_progress_on_screen = False

	# open file and create image object:, and then do the stuff with it
	with Image.open(the_name_of_the_picture_file) as img1:
		
		# get the width and height of the image in the image object
		width, height = img1.size
		
		# get the image size in this variable to make it easier to return out of the function
		pictureSize = img1.size

		# show_progress_on_screen is just for trouble shooting, remove later
		if ( show_progress_on_screen ):	
			print("height => ", height)
			print("width => ", width)
			print("1st pixel => ", img1.getpixel((0,0)))
			print("last pixel => ", img1.getpixel((width-1, height-1)))


		# This double loop gets the pixel info from the picture and
		# puts it in the array	
		for x in range(width-1):
			for y in range(height-1):
				theArray.append(img1.getpixel((x,y))) 

				# show_progress_on_screen is just for trouble shooting, remove later.
				# These "if" statements print out first and last part of theArray
				# for trouble shooting.
				if ( x<4 and y<4 ) or ( x>width-5 and y>height-5 ):
					if ( show_progress_on_screen ):	
						if ( x==0 ) and ( y==0 ):
							print()
						if ( x==width-4 ) and ( y==height-4 ):
							print()

	return pictureSize, theArray

# -----------------------------------------------------------------------

def make_image_object_from_array_and_save_it_to_file(thePictureArray, pictureSize):
	
	imageOutgoing = Image.new(mode = "RGB", size = pictureSize)

	width, height = pictureSize

	counter = 0;
	for x in range(width-1):
		for y in range(height-1):
			imageOutgoing.putpixel((x,y), (thePictureArray[counter]))
			counter = counter + 1

	imageOutgoing.save('picSaved.png')

	imageOutgoing.show()

# -----------------------------------------------------------------------

def change_image_arbitrarily(thePictureArray, pictureSize):


	width, height = pictureSize

	counter = 0	
	for x in range(width-1):
		for y in range(height-1):
			a, b, c = thePictureArray[counter] 
			b = 255 - b
			thePictureArray[counter] = c, b, a
			counter = counter + 1 
			
	return thePictureArray			

# -----------------------------------------------------------------------

def main():

	thePictureArray = []
	pictureSize = [] 
	the_name_of_the_picture_file = "pic2.png"

	print("\n-------------------\n")

	print(f"thePictureArray size at the start => {len(thePictureArray)} array objects")
	print(f"pictureSize => {pictureSize} pixels")
	
	pictureSize, thePictureArray = go_get_the_image_and_load_it_into_the_array(the_name_of_the_picture_file)
	

	print(f"thePictureArray size at the end   => {len(thePictureArray)} array objects")
	print(f"pictureSize => {pictureSize} pixels")
	print()

	
	thePictureArray = change_image_arbitrarily(thePictureArray, pictureSize)

	make_image_object_from_array_and_save_it_to_file(thePictureArray, pictureSize)

	

	print("\n-------------------\n")

# -----------------------------------------------------------------------

if __name__ == "__main__":
	main()


