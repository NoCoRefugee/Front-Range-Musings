#! /usr/bin/env python3
from PIL import Image



def makeLine(someWord):
      print("\n------- ", someWord, "-----------------------------------------\n")

def do_image():

      img = Image.open("pdog.jpg")
      width, height = img.size
      print("image size => ", img.size)
      img_data = img.getexif()
      print("-------------")
      print("Data => ")
      print(img_data)
      print("-------------")
def main():

      makeLine("Start")

      do_image()

      makeLine("End  ")


if __name__ == "__main__":
      main()




