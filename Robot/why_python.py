#!/usr/bin/env Python3
from PIL import Image

def go_get_the_image_and_load_it_in_the_array( theArray = [], *args ):

	with Image.open('pic1.jpg') as img1:
		img1.save('an_other_one.png')

	width, height = img1.size
	
	print("height => ", height)
	print("width => ", width)

	print("1st pixel => ", img1.getpixel((0,0)))

	print("last pixel => ", img1.getpixel((width-1, height-1)))

	
	for x in range(width-1):
		for y in range(height-1):
			if ( x<4 and y<4 ) or ( x>width-5 and y>height-5 ):
				holder = img1.getpixel((x,y)) 
				print(holder),
#			if ( holder == (242, 241, 249) ):
			if ( y<10 ):
				img1.putpixel((x,y), ( 153, 0, 153))

	img1.save('an_other_one.png')




def main():

	thePicture = []

	print("\n-------------------\n")

	go_get_the_image_and_load_it_in_the_array(thePicture)

	print("\n-------------------\n")

if __name__ == "__main__":
	main()


