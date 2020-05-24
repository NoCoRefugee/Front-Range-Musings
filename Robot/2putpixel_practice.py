#!/usr/bin/env Python3
from PIL import Image


print("\n-------------------\n")


img1 = Image.open("pic1.jpg")

print("img1.size => ", img1.size)

print("getpixel => ", img1.getpixel((0, 0)))

img2 = img1
width, height = img1.size 

for x in range(width - ( int(width/2) )):
	for y in range(height - ( int(height/2) )):
		img2.putpixel((x,y), (0, 0, 0, 0))

img1.save('changed_pic.png')


print("getpixel => ", img1.getpixel((0, 0)))


print("\n-------------------\n")

