#include <iostream>
#include <math.h>
using namespace std;

// -------------------------------------------------------------------

int theNumber = 5;
int arraySize = 20;

// -------------------------------------------------------------------

void initializeArray(int* arrayOne) {

	arrayOne[0] = 2;

} // end of initializeArray
// -------------------------------------------------------------------

int getArraySize(int* arrayOne) {

	int i;
	int sizeA = 0;
	

	return sizeA;

} // end of getArraySize

// -------------------------------------------------------------------

void showArray(int* arrayOne) {
	
	int i;

	cout << "\nWe are in show array\n";
	
	cout << endl;	

	for ( i=arraySize; i--; i>=0 ) {
		cout << arrayOne[i];
	}	

	cout << endl;	


} // end of showArray

// -------------------------------------------------------------------

void multiplyArrayByTwo(int* arrayOne, int counter) {

	int howManyIterations = counter + 2;	

	arrayOne[1] = 5;
	cout << "\ncounter => " << counter;
	cout << "\nhowManyIterations => " << howManyIterations;

}  // end of multiplyArrayByTwo 
// -------------------------------------------------------------------
// -------------------------------------------------------------------



int main() {
	
	int mersenneN = theNumber;  // this will be the n of 2^n-1
	int numberSize = 0;
	int numberholder[20] = {0};

	cout << "\n----------------------------------------------------\n";
	
	initializeArray(numberholder);

	cout << "\nThe array is => \n";

	showArray(numberholder);

	multiplyArrayByTwo(numberholder, numberSize);


	cout << "\nThe array is => \n";

	showArray(numberholder);

	
	cout << "\n----------------------------------------------------\n";


} // end of main



