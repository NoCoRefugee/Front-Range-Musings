#!/usr/bin/env python3
import os
"""
      This program is an example of generator use in python.  As a
      by-product it also produces fibonacci numbers.

      20200111  -  JLF
"""

def makeLine(someWord):
#
#      This function prints a line to the screen with a word in the line.
#      The point of this is only to make the output easier
#      to read in the terminal.
#
      print("\n--- " + someWord + " ----------------------------------\n")


def simplest_generator_function():
#
#     I think this function is about the simplest generator function
#     we can think of right now.  It just returns the next interger in
#     in the list of whole numbers without an upper bound.
#      
      x = 0
      while True:
            x = x + 1
            yield(x)


def fibonacci_number_function():
#
#      This functions has two yield statements in it and returns a slightly more
#      complitcated number set.  So it actually does something.
#
      num1 = 0
      num2 = 1
      new = 0

      # this "if" statement should only happen once, and at the very first iteration
      if new == 0:
            yield(1)

      # this while loop finds the fibonacci numbers and sends them to the program
      while True:
            new = num1 + num2
            yield( new )
            num1 = num2
            num2 = new

def main():

      makeLine("start")

#     don't understand why, but you can not directly call
#     the generator.  You have to first assign it to a 
#     variable, or object thing as show on next code line:           
#     The form is "generator" = "function"... maybe
      fibonacci_generator = fibonacci_number_function()

#     clear the screen before asking for user input:        
      os.system("clear")

#     ask the user how many fibonacci numerber they want
      print("How many fibonacci numbers do you want? => ", end = " ")
      user_input_number = int(input())
      print("")

#     This prints out x number of the fibs along with a 
#     bunch of helpful clarifying info.
      for x in range(user_input_number):
            print("fib(" + str(x+1) + ") => \t", next(fibonacci_generator))

      print("\n\n")
      print("type for fibonacci_number_function => ", type(fibonacci_number_function))
      print("type for fibonacci_generator => ", type(fibonacci_generator))
#     
#     The two print statements above this line produce the following 
#     output.  So I guess the 'function' is just a function and the
#     variable assigned to that 'function' is the generator.
#
#     type for fibonacci_number_function =>  <class 'function'>
#     type for fibonacci_generator =>  <class 'generator'>
#


#     this next line creates the generator from the function
      simplest_generator = simplest_generator_function()

#     this loop pulls numbers from the simplest_generator
      print("\n\nNow for the simplest generator output:\n")
      for i in range(10):
            print(next(simplest_generator))

      makeLine("end  ")


if __name__ == "__main__":
      main()
