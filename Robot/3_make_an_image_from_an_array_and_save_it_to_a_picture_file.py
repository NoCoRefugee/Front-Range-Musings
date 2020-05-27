#!/usr/bin/env python3
from PIL import Image

# -----------------------------------------------------------------------
# todo List:
#


# -----------------------------------------------------------------------

def go_get_the_image_and_load_it_into_the_array(the_name_of_the_picture_file):

# 	This function loads an image from a file and returns the size of that
#	image and an array with that image's pixel data.

#	This function needs these external variables to exist:
#		thePictureArray = [list]
#		pictureSize = [list] 
#		the_name_of_the_picture_file = "file name string"

#	jlf  -  20200525


	# open file and create image object:, and then do the stuff with it
	with Image.open(the_name_of_the_picture_file) as img1:
		
		# get the width and height of the image in the image object
		width, height = img1.size
				
		theArray = [[0 for i in range(height)] for j in range(width)]


		# get the image size in this variable to make 
		# it easier to return out of the function
		pictureSize = img1.size

		# This double loop gets the pixel info from the picture and
		# puts it in the array	
		for x in range(width-1):
			for y in range(height-1):
				theArray[x][y] = img1.getpixel((x,y)) 


	return pictureSize, theArray

# -----------------------------------------------------------------------

def make_image_object_from_array_and_save_it_to_file(thePictureArray, pictureSize):
	
	imageOutgoing = Image.new(mode = "RGB", size = pictureSize)

	width, height = pictureSize

	for x in range(width-1):
		for y in range(height-1):
			imageOutgoing.putpixel((x,y), (thePictureArray[x][y]))

	imageOutgoing.save('picSaved.png')

	imageOutgoing.show()

# -----------------------------------------------------------------------

def change_image_arbitrarily(thePictureArray, pictureSize):


	width, height = pictureSize

	# this loop swaps the r and b colors of the pixels
	# in the image, using RGB format
#	for x in range(width-1):
#		for y in range(height-1):
#			a, b, c = thePictureArray[x][y] 
#			thePictureArray[x][y] = c, b, a
	
	# this loop makes the left half of image a copy
	# of the right half of the image		
	halfThing = int((width-1)/2)	
	for x in range(halfThing):
		for y in range(height-1):
			thePictureArray[x][y] = thePictureArray[halfThing+x][y]
			
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


