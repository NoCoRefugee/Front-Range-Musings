#!/usr/bin/env python3
import math
from decimal import *
"""
      This doesn't seem to work past 18281828459045, next digit should be 2 according to the
      internet, but we are getting 5.  Don't know what is up.
"""
# ---------------------------------------------------------------------------------------------------

def makeLine(someWord):
      print("\n----------- ", someWord, " --------------------------------------------------------------\n")

# ---------------------------------------------------------------------------------------------------

def part_of_the_way_to_e():

      getcontext().prec = 30

      fact_sum = 1.0
      print("Factorialize => ")
      for x in range(1, 30):
            fact_sum = fact_sum + ( 1 / math.factorial(x))
#           print(Decimal.from_float(fact_sum))
            print(fact_sum)

      str_num = str(fact_sum)
      print("as a string => ", str_num)
      print("decimal ??? => ", Decimal.from_float(fact_sum))

     
# ---------------------------------------------------------------------------------------------------

def show_some_factorials():

      for x in range(1, 100):
            print(math.factorial(x))

 
# ---------------------------------------------------------------------------------------------------

def main():

      makeLine("Start") 
      
      getcontext().prec = 25

      part_of_the_way_to_e()

#     show_some_factorials()


      makeLine("End  ") 
# ---------------------------------------------------------------------------------------------------
             
if __name__ == "__main__":
      main()
     

 
