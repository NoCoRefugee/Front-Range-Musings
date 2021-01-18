#!/usr/bin/env python3
import os
"""
      This program is an example of generator use in python.  As a
      by-product it also produces fibonacci numbers.  ( and small gererated
      numbers, and maybe some prime numbers... and what ever else we thing
      of...

      20200111  -  JLF
"""

# -----------------------------------------------------------------------------------------------------

def makeLine(someWord):
      """ 
      This function prints a line to the screen with a word in the line.
      The point of this is only to make the output easier
      to read in the terminal.
      """ 
      print("\n--- " + someWord + " ----------------------------------\n")


# -----------------------------------------------------------------------------------------------------

def simplest_generator_function():
      """ 
      I think this function is about the simplest generator function
      we can think of right now.  It just returns the next interger in
      in the list of whole numbers without an upper bound.
      """  
      x = 0
      while True:
            x = x + 1
            yield(x)


# -----------------------------------------------------------------------------------------------------

def simplest_generator_function_function():
      """
      This function makes an instance of the simplest_generator_function 
      and runs it through a loop or something
      """
#     this next line creates the generator from the function
      simplest_generator = simplest_generator_function()

#     this loop pulls numbers from the simplest_generator
      print("\n\nNow for the simplest generator output:\n")
      for i in range(10):
            print(next(simplest_generator))
      
# -----------------------------------------------------------------------------------------------------

def fibonacci_number_function():
      """
      This functions has two yield statements in it and returns a slightly more
      complitcated number set.  So it actually does something.
      """ 
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

# -----------------------------------------------------------------------------------------------------

def fibonacci_function_running_function():
      """
      don't understand why, but you can not directly call
      the generator.  You have to first assign it to a 
      variable, or object thing as show on next code line:           
      The form is "generator" = "function"... maybe
      fibonacci_generator = fibonacci_number_function()
      """

#     ask the user how many fibonacci numbers they want
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

# -----------------------------------------------------------------------------------------------------

def is_prime_function(someNumber):
      """ 
      This function tests to see if input number ( someNumber ) is prime
      """ 
      end_num = int(someNumber/2) + 1

      for divisor in range(3, end_num, 2):
            if someNumber%divisor == 0:
                  return False
            
      return True

# -----------------------------------------------------------------------------------------------------

def prime_number_generator_simple():
      """  
      This function defines a generator for producing Prime numbers one at a time,
      as generators do...
      """ 
      test_num = 3 
      end_num = 0
      is_prime = False
      stop = True
      
      while True:
            test_num += 2
            stop = False
            while stop == False: 
                  if is_prime_function(test_num) == False:
                        test_num += 2
                  else:
                        stop = True
                        yield test_num



# -----------------------------------------------------------------------------------------------------

def run_the_prime_number_generator_simple():
      """ 
      This function creates an instance of the prime number generator function and runs it 
      over some range, or something...
      """ 
      instance_of = prime_number_generator_simple()

      # print the first two primes to avoid having to make the loop more complicated
      print("1  => ", 2)
      print("2  => ", 3)
      
      number_of_primes_wanted = 20000
      for thing1 in range(number_of_primes_wanted-2):
            print(thing1+3, " => ", next(instance_of))

# -----------------------------------------------------------------------------------------------------

def show_some_prime_numbers_on_the_screen():
      """
      This function makes an instance of the run_the_prime_number_generator_simple function
      and uses the instance to put some prime number on the screen.  It might include a part
      about asking the user how many primes they want to see.
      """
      
      instance_of = prime_number_generator_simple()
      print("How many prime numbers you want?")
      x = int(input())
      x = x - 2
      print("1  => ", 2)
      print("2  => ", 3)
      for thing1 in range(x):
            if x > 1000:
                  if (thing1)%1000 == 0:
                        print(thing1 + 3, " => ", next(instance_of))
                  else:
                        next(instance_of)
            else:      
                  print(thing1 + 3, " => ", next(instance_of))

# -----------------------------------------------------------------------------------------------------

def main():

      # clear the screen before running other parts of program:        
      os.system("clear")

      makeLine("start")



#     fibonacci_function_running_function()
#     simplest_generator_function_function()

      run_the_prime_number_generator_simple()
      
      
#     show_some_prime_numbers_on_the_screen()


      makeLine("end  ")

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------

if __name__ == "__main__":
      main()

# -----------------------------------------------------------------------------------------------------
