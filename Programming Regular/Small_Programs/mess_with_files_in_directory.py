#!/usr/bin/env python3
import os
"""   
      This shows how to get the filenames for a directory and hints at 
      how to change those names, cause you can never remember the 'rename'
      command details

      20210124  -  JLF
"""

def get_directory_list():

      for name in os.listdir():
            print(name)
            # you can operate on those names here with os.rename(filename, new_filename) etc.


def main():

      print("\n---------------------------------------------------------------------------------\n")

      get_directory_list()

      print("\n---------------------------------------------------------------------------------\n")



if __name__ == "__main__":
      main()
