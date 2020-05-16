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

void showArray(int* arrayOne) {
	
	int i;

	cout << "\nWe are in show array\n";
	
	cout << endl;	

	for ( i=arraySize; i--; i>=0 ) {
		cout << arrayOne[i] << ".";
	}	

	cout << endl;	


} // end of showArray

// -------------------------------------------------------------------

void multiplyArrayByTwo(int* arrayOne, int arrayCurrentSize) {

	int i = 0;

	while ( arrayCurrentSize >= i ) {

		cout << "\narrayCurrentSize => " << arrayCurrentSize;
		arrayOne[i] = arrayOne[i]*2;	
		if ( arrayOne[i] > 9 ) {
			arrayOne[i+1]++;
			arrayOne[i] = arrayOne[i]%10;
			if ( i >= arrayCurrentSize ) { arrayCurrentSize++; }
		} // end of if...	
		i++;
		cout << "\ni => " << i;

	} // end of while...

	showArray(arrayOne);

}  // end of multiplyArrayByTwo 

// -------------------------------------------------------------------
// -------------------------------------------------------------------



int main() {
	
	int mersenneN = theNumber;  // this will be the n of 2^n-1
	int arrayCurrentSize = 1;
	int numberholder[arraySize] = {0};

	cout << "\n----------------------------------------------------\n";
	
	initializeArray(numberholder);

	for ( int i=0; i<theNumber; i++ ) {
		multiplyArrayByTwo(numberholder, arrayCurrentSize);
	} // end of for...

	
	cout << "\n----------------------------------------------------\n";


} // end of main



