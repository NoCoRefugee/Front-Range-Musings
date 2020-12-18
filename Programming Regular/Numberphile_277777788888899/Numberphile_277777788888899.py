#! /usr/bin/env python3

def mkline():
      print("\n------------------------\n")


def main():

      mkline()

      testNumber = 345
      iteration_tracker = 0 
      newNumber = 0

      testString = str(testNumber)

      print("testNumber => ", testNumber)
      print("testString => ", testString)
      print()

      while testNumber > 9:
            iteration_tracker += 1
            for x in testString:
                  newNumber *= int(x)
            print("newNumber => ", newNumber)
            print("testNumber => ", testNumber)
            print()
            testNumber = newNumber


      print("newNumber => ", newNumber)
      print("testNumber => ", testNumber)

      mkline()


main()
