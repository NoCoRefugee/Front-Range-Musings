#!/usr/bin/env python3
from PIL import Image

# -----------------------------------------------------------------------

def get_the_picture_size( pictureSize ):

	print("inside pictureSize")
	return pictureSize

# -----------------------------------------------------------------------

def go_get_the_image_and_load_it_into_the_array( theArray = [], *args):

	show_progress_on_screen = False

	with Image.open('pic1.jpg') as img1:

		width, height = img1.size

		randomSize = img1.size
		get_the_picture_size( randomSize )	

		if ( show_progress_on_screen ):	
			print("height => ", height)
			print("width => ", width)

			print("1st pixel => ", img1.getpixel((0,0)))

			print("last pixel => ", img1.getpixel((width-1, height-1)))

		
		for x in range(width-1):
			for y in range(height-1):
				if ( x<4 and y<4 ) or ( x>width-5 and y>height-5 ):
					if ( show_progress_on_screen ):	
						if ( x==0 ) and ( y==0 ):
							print()
						if ( x==width-4 ) and ( y==height-4 ):
							print()
				holder = img1.getpixel((x,y)) 
				theArray.append(holder)
				if ( show_progress_on_screen ):	
					print(holder),

	img1.save('and_other_one.png')
	
	return pictureSize

# -----------------------------------------------------------------------

def main():

	thePicture = []
	PictureSize = (0, 0)

	print("\n-------------------\n")

	print(f"thePicture size at the start => {len(thePicture)}")
	print(f"PictureSize => {PictureSize}")
	
	go_get_the_image_and_load_it_into_the_array(thePicture) 
	

	print(f"thePicture size at the end   => {len(thePicture)}")
	print(f"PictureSize => {PictureSize}")

	print("\n-------------------\n")

# -----------------------------------------------------------------------

if __name__ == "__main__":
	main()


