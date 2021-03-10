#! /usr/bin/env python3
import math

def makeLine(someWord):
      print("\n----- ", someWord, " ---------------------------------------------\n")


def makePrimesForReference():

      primeList = []

      for NumberToTest in range(3, 200000, 2):
            isPrime = True
            stopNumber = int(NumberToTest/2 + 1)
            for testNumber in range(3, stopNumber, 2):
                  if NumberToTest % testNumber == 0:
                        isPrime = False
                        break
            if isPrime:
                  primeList.append(NumberToTest)
                  
      return primeList

def main():


      makeLine("start")

      theNewList = makePrimesForReference()

      print("theNewList => ", theNewList) 

      
      makeLine("end  ")




if __name__ == "__main__":
      main()




