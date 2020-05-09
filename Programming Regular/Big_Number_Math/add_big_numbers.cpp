#include <iostream>
using namespace std;
/*

	jlf  -  20200508

	This is big_number_math.  We are starting with adding big numbers
	together.  We are using arrays to hold individual 0-9 numbers and
	the array index as 1s, 10ths, 100ths, etc.  Once we get that working
	we will move to making each index half of maxInt, or some fraction
	of that that keeps us from going over on the math operations.] 

	Then subtraction, etc.  Probably make sqrt also.  

	notes:  
	1) the first index of array, [0] will be used only to show sign
	2) the info is stored in the arrays backwards, sort of.  Array[1]
		is the one's place, Array[3] is the hundredths place, etc.

*/

int arraySize = 31;
int intSize = 9;

// ------------------------------------------------------------------------
// This function makes a line on the screen soley for clarifying output.
void makeLine(){

	cout << "\n*******************************************************************\n";


}  // end makeLine


// ------------------------------------------------------------------------
// This function seeds an array with ints.  This is for testing only.
void seedArray( int* passedArray ) {

	int i;

	passedArray[0] = 0;

	for ( i=4; i>0; i-- ) {
		
		passedArray[i] = i;
	} 

/*
	for ( i=arraySize-1; i>0; i-- ) {
		
		passedArray[i] = 3;
	} 
*/

} // end of seedArray

// ------------------------------------------------------------------------
// This function adds two arrays together
void addArrays( int* a1, int* a2, int* a3 ) {
// 1. make a carry over part
// 2. count the leading zeros so you don't have to add that part
// 3. track if you are getting to array size limit, make error if last
//	addition is going to roll over too far.

	int i;

	for ( i=arraySize-1; i>0; i-- ) {
		a3[i] = a2[i] + a1[i];
	}


} // end of addArrays



// ------------------------------------------------------------------------
// This function prints out the array.  This is for testing only.
void showArray( int* passedArray ) {

	int i;

	// show the sign character
	cout << "\narray[0] => " << passedArray[0];

	// show what the arraySize constant is at the moment
	cout << "\narray size => " << arraySize;

	// this prints numbers on screen to make it easier to 
	// see what the array print out is doing, it's a ruler.
	cout << "\n123456789012345678901234567890\n";

	// This shows the current contents of the array:
	for ( i=arraySize-1; i>0; i-- ) {
		
		cout << passedArray[i];

	} 

}  // end of showArray

// ------------------------------------------------------------------------

// ------------------------------------------------------------------------

// ------------------------------------------------------------------------

int main() {

	int arr1[arraySize] = {0};
	int arr2[arraySize] = {0};
	int arr3[arraySize] = {0};


	makeLine();

	seedArray( arr1 );
	seedArray( arr2 );
	addArrays(arr1, arr2, arr3);

	showArray( arr1 );
	showArray( arr2 );
	showArray( arr3 );

	cout << "\narr2[0] => " << arr2[0];
	cout << "\narr2[30] => " << arr2[30];
	makeLine();

}  // end of main

// ------------------------------------------------------------------------

