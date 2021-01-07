#!/usr/bin/env python3

import numpy as np

#------------------------------------------------------------------------------

def makeLine():
      print("\n----------------------------------------------------------------\n")

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def main():

      makeLine()

      # make 1 dimensional array
      a = np.array([1,2,3])
      print("a => ", a)
      print("\n")

      # make 2 dimensional array
      b = np.array([[9.0, 8.0, 7.0],[6.0,5.0,4.0]])
      print("b => \n", b)
      print("\n")
      
      # get dimension of array
      print("dimension of array a => ", a.ndim)
      print("dimension of array b => ", b.ndim)
      print("\n")

      # get shape of array
      print("shape of array a => ", a.shape)
      print("shape of array b => ", b.shape)
      print("\n")





      makeLine()


if __name__ == "__main__":
      main()
