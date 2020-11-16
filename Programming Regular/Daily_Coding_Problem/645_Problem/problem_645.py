#!/usr/bin/env python3

# --------------------------------------------------

# JLF  -  20201102 - 20201115

#  from Daily Coding Problem: Problem #645 [easy]

#  Good morning! Here's your coding interview problem for today.
#  
#  This problem was asked by Microsoft.
#  
#  Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in matrix in the matrix by going left-to-right, or up-to-down.
#  
#  For example, given the following matrix:
#  
#  [['F', 'A', 'C', 'I'],
#   ['O', 'B', 'Q', 'P'],
#   ['A', 'N', 'O', 'B'],
#   ['M', 'A', 'S', 'S']]
#  
#  and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
#  
#  

# --------------------------------------------------

def mL():
        print("")
        print("")
        print("------------------------------------------------------")
        print("")
        print("")

# --------------------------------------------------

def two_string_method():
      # First Try:  make a string out of matrix, and an other out of
      # a flipped matrix, then see if the words are in there:

      # make variables to hold the data given in the question:

      print("------------------------------------------------")      
      print("two_string_method")

      matrix = [['F', 'A', 'C', 'I'],['O', 'B', 'Q', 'P'],['A', 'N', 'O', 'B'],['M', 'A', 'S', 'S']]
      target_word_1 = 'FOAM'
      target_word_2 = 'MASS'


      # --------------------------------------------------

      # make one big string from horizontal matrix letters:

      damn_list = []
      for x in range(4):
            for i in range(4):
                  damn_list.extend(matrix[i][x])

      horizontal_letter_string = ''
      horizontal_letter_string = horizontal_letter_string.join(damn_list)


      # --------------------------------------------------

      # make one big string from vertical matrix letters:

      new_list = []
      for i in range(4):
            new_list = new_list + matrix[i]

      vertical_letter_string = ''
      vertical_letter_string = vertical_letter_string.join(new_list)

      # --------------------------------------------------


      # see if the target words are in the matrix, via the 
      # created strings, and if yes show that info on the screen:

      print("")
      print("target word 1 => ", target_word_1)
      if target_word_1 in vertical_letter_string:
            print("found horizontally in matrix")
      if target_word_1 in horizontal_letter_string:
            print("found vertically in matrix")

      print("")
      print("target word 2 => ", target_word_2)
      if target_word_2 in vertical_letter_string:
            print("found horizontally in matrix")
      if target_word_2 in horizontal_letter_string:
            print("found vertically in matrix")

# --------------------------------------------------


def one_big_string_method():

      # make variables to hold the data given in the question:

      matrix = [['F', 'A', 'C', 'I'],['O', 'B', 'Q', 'P'],['A', 'N', 'O', 'B'],['M', 'A', 'S', 'S']]
      target_word_1 = 'FOAM'
      target_word_2 = 'MASS'

      # make one big list from matrix letters:

      print("------------------------------------------------")      
      print("one_big_string_method")

      damn_list = []
      for x in range(4):
            for i in range(4):
                  damn_list.extend(matrix[i][x])
      for i in range(4):
            for x in range(4):
                  damn_list.extend(matrix[i][x])


      # turn damn_list into one big_string

      big_string = ''
      big_string = big_string.join(damn_list)

      print("big_string => ", big_string)

      if target_word_1 in big_string:
            print("found ", target_word_1)
      if target_word_2 in big_string:
            print("found ", target_word_2)
      # --------------------------------------------------


# --------------------------------------------------------

def find_words_as_lists():

      matrix = [['F', 'A', 'C', 'I'],['O', 'B', 'Q', 'P'],['A', 'N', 'O', 'B'],['M', 'A', 'S', 'S']]
      target_word_1 = 'FOAM'
      target_word_2 = 'MASS'

      list1 = [] 
      list2 = [] 
      list1[:0] = (target_word_1)
      list2[:0] = (target_word_2)

      print("------------------------------------------------")      
      print("find_words_as_lists")

      print("We are looking for:")
      print("list1 => ", list1)
      print("list2 => ", list2)
      print("")

      for x in range(4): 
            print("matrix[", x, "] => ", matrix[x])
            if list1 == matrix[x]:
                  print("Found ", list1, "!")
            if list2 == matrix[x]:
                  print("Found ", list2, "!")

      flipped_matrix = []
      temp_list = []

      for y in range(4):
            for x in range(4):
                  temp_list.extend(matrix[x][y])
            flipped_matrix.append(temp_list)
            temp_list = []

      for x in range(4): 
            print("flipped_matrix[", x, "] => ", flipped_matrix[x])
            if list1 == flipped_matrix[x]:
                  print("Found ", list1, "!")
            if list2 == flipped_matrix[x]:
                  print("Found ", list2, "!")

# --------------------------------------------------------

def main():
      mL()
      
      # show the matrix on the screen:

      print("matrix => ")
      print("")
      print(['F', 'A', 'C', 'I'])
      print(['O', 'B', 'Q', 'P'])
      print(['A', 'N', 'O', 'B'])
      print(['M', 'A', 'S', 'S'])

      one_big_string_method()
      two_string_method()
      find_words_as_lists()
      mL()

      
if __name__ == '__main__':
      main()


