#include <iostream>
#include <string>
using namespace std;

/*

jlf  -  20201115

#  from Daily Coding Problem: Problem #645 [easy]

Good morning! Here's your coding interview problem for today.
 
This problem was asked by Microsoft.
 
 Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in     matrix in the matrix by going left-to-right, or up-to-down.
 
 For example, given the following matrix:
 
 [['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
 
 and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target w    ord 'MASS', you should return true, since it's the last row.
*/ 

void showData() {

      cout << "\nHere is the matrix we are working with:\n";
      cout << "\n['F', 'A', 'C', 'I']";
      cout << "\n['O', 'B', 'Q', 'P']";
      cout << "\n['A', 'N', 'O', 'B']";
      cout << "\n['M', 'A', 'S', 'S']";
      cout << endl; 
      
      cout << "\ntargets words => 'FOAM' and 'MASS' \n";

} // end showData

// ------------------------------------------------------------------------------

void makeLine() {

      cout << "\n\n-----------------------------------------------------\n\n";

} // end of makeLine()

//---------------------------------------------------------------------------------

int main() {

      char matrix[4][4];
      string word3 = "";
      string word1 = "FOAM";
      string word2 = "MASS";
      
      makeLine();

      showData();

      // put the matrix in a data structure:      
      matrix[0][0] = 'F';
      matrix[0][1] = 'A';
      matrix[0][2] = 'C';
      matrix[0][3] = 'I';
      matrix[1][0] = 'O';
      matrix[1][1] = 'B';
      matrix[1][2] = 'Q';
      matrix[1][3] = 'P';
      matrix[2][0] = 'A';
      matrix[2][1] = 'N';
      matrix[2][2] = 'O';
      matrix[2][3] = 'B';
      matrix[3][0] = 'M';
      matrix[3][1] = 'A';
      matrix[3][2] = 'S';
      matrix[3][3] = 'S';

      // make a string from the vertical matrix letters:
      word3 = word3 + matrix[0][0];
      word3 = word3 + matrix[0][1];
      word3 = word3 + matrix[0][2];
      word3 = word3 + matrix[0][3];
      word3 = word3 + matrix[1][0];
      word3 = word3 + matrix[1][1];
      word3 = word3 + matrix[1][2];
      word3 = word3 + matrix[1][3];
      word3 = word3 + matrix[2][0];
      word3 = word3 + matrix[2][1];
      word3 = word3 + matrix[2][2];
      word3 = word3 + matrix[2][3];
      word3 = word3 + matrix[3][0];
      word3 = word3 + matrix[3][1];
      word3 = word3 + matrix[3][2];
      word3 = word3 + matrix[3][3];

      // add to string the horizontal matrix letters:
      word3 = word3 + matrix[0][0];
      word3 = word3 + matrix[1][0];
      word3 = word3 + matrix[2][0];
      word3 = word3 + matrix[3][0];
      word3 = word3 + matrix[0][1];
      word3 = word3 + matrix[1][1];
      word3 = word3 + matrix[2][1];
      word3 = word3 + matrix[3][1];
      word3 = word3 + matrix[0][2];
      word3 = word3 + matrix[1][2];
      word3 = word3 + matrix[2][2];
      word3 = word3 + matrix[3][2];
      word3 = word3 + matrix[0][3];
      word3 = word3 + matrix[1][3];
      word3 = word3 + matrix[2][3];
      word3 = word3 + matrix[3][3];

      cout << endl;
     
      // show string on screen: 
      cout << "Turn matrix into long string made from horizontal and";
      cout << "\nvertical readings of matrix. =>\n";      
      cout << word3;
      cout << "  length of string => " << word3.length() << endl;

      // check to see if word1 is in the string:
      for ( int i=0; i<word3.length()-3; i++ ) 
      {
            if (( word3[i] == word1[0] ) && 
               ( word3[i+1] == word1[1] ) &&
               ( word3[i+2] == word1[2] ) && 
               ( word3[i+3] == word1[3] ))
               {
                  cout << "\nfound a match for " << word1 << " at position [" << i << "]"; 
               }
      }

      // check to see if word2 is in the string:
      for ( int i=0; i<word3.length()-3; i++ ) 
      {
            if (( word3[i] == word2[0] ) && 
               ( word3[i+1] == word2[1] ) &&
               ( word3[i+2] == word2[2] ) && 
               ( word3[i+3] == word2[3] ))
               {
                  cout << "\nfound a match for " << word2 << " at position [" << i << "]"; 
               }
      }

      makeLine();


} // end of main
