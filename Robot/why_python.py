#!/usr/bin/env Python3
from PIL import Image


print("\n-------------------\n")

print("\nWhat the fuck?!, python?")

img1 = Image.open("pic1.jpg")

print("img1.size => ", img1.size)
croppedIm = img1.crop((50, 260, 340, 650))
croppedIm.save('cropped.png')

print("getpixel => ", img1.getpixel((0, 0)))


for x in range(100):
	for y in range(100):
		croppedIm.putpixel((x, y), (0, 0, 0))

croppedIm.save('putpixeled.png')




print("\n-------------------\n")

