#! /usr/bin/env python3
import math
""" 
      This program was prompted by James Grimes new favorite constant on Numberphile

      It shows a constant making primes in section main(),  far as I can tell it 
      doesn't work.

      JLF  -  20210302
"""

      

def makeLine(someWord):

      print("\n----- ", someWord, "----------------------------------------------------------\n")



def doTheFunction(someConstant):

      num1 = math.floor(someConstant)
      num2 = someConstant - num1 + 1

      return num1, num2

def makePrimesForReference():

      for NumberToTest in range(3, 100, 2):
            isPrime = True
            stopNumber = int(NumberToTest/2 + 1)
            for testNumber in range(3, stopNumber, 2):
                  if NumberToTest % testNumber == 0:
                        isPrime = False
                        break
            if isPrime:
                  print("NumberToTest => ", NumberToTest)

def main():

      someConstant = 2.920050977316

      makeLine("start")

      makePrimesForReference()


      for i in range(1, 30):
      
            num1, num2 = doTheFunction(someConstant)
            someConstant = num1 * num2
            print(i, "  The things => ", num1, ",",  num2)

      makeLine("end  ")




if __name__ == "__main__":
      main()




