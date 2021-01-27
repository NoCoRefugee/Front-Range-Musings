#! /usr/bin/env python3

"""
      jlf  -  20201227

      just goofing around with dicts
"""

def makeline(word1):

      if word1 == "":
            print("\n------------------------------------------\n")
      else:
            print("\n----", word1, "-------------------------------\n")


def show_cat(dict_in):

      for thing in dict_in:
            print( "cat is => ", thing, " named => ", dict_in[thing] )


def list_comp_thing():

      some_var = 8
      some_list = [ n*n for n in range(1, some_var+1) ]
      print(some_list)


def make_cat_list():
      
      return { "cat1": "sumo", "cat2": "rosie", "cat3": "pete" }


def make_vert_list():
"""
      the point of this fuction is to see if the indent matters
      when creating a list, cause vertically would be much nicer.
      looks like indent doesn't matter inside the brackets
"""

      return {
"dog1": "snoopy", 
"dog2": "spot",
"dog3": "fido",
"dog4": "rin tin tin",
"dog5": "lassie"
            }


def main():

      makeline("start")

      some_dict = make_cat_list()

      print("the dictionary is now => ", some_dict)
      print("the dictionary type is now => ", type(some_dict))
      print("the dictionary length is now => ", len(some_dict))

      print()

      # display dictionary key value pair
      show_cat(some_dict)

      print()

      # how to combine dicts, one way:
      big_dict = make_cat_list()
      big_dict.update(make_vert_list())

      print("big_dict => ", big_dict)

      print() 

      show_cat(big_dict)

      makeline("stop")

if __name__ == "__main__":
      main()




