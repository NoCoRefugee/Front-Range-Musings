#include <iostream>
using namespace std;

// -------------------------------------------------------------------------------

void showArray(int* array, int currentSize) {

	cout << "\narray => ";
	for ( int i=19; i>=0; i-- ) {
		cout << array[i] << ".";
	} // end of for
/*
	cout << "\narray => ";
	for ( int i=currentSize; i>=0; i-- ) {
		cout << array[i] << ".";
	} // end of for
*/
} // end of showArray

// -------------------------------------------------------------------------------

void multiplyArrayByTwo(int* array, int currentSize) {

	
	int carryOver = 0;
	int numberN = 5;
	int i = 0;

	for ( i=0; i<=currentSize; i++ ) {
		array[i] = array[i] + carryOver;
		array[i] = array[i] * 2;
		cout << "\ncarryOver => " << carryOver;
		if ( array[i] > 9 ) {
			cout << "\ngreater than 9";
			carryOver = 1;
			array[i+1] = array[i+1] + carryOver;
			array[i+5] = 8;
			array[i] = array[i]%10;
			if ( i > currentSize ) { currentSize++; } 
		} // end of if
		i++;

		cout << "\ncurrentSize => " << currentSize;
		cout << "\ncarryOver => " << carryOver << endl;
		
	} // end of for 

} // end of multiplyArrayByTwo

// -------------------------------------------------------------------------------

int main() {


	int array[20] = {0};
	int currentSize = 1;

	cout << "\n----------------------------------------\n";

	showArray(array, currentSize);

	array[0] = 2;

	cout << "\n------------------------";
	for ( int i=0; i<9; i++ ) {
		showArray(array, currentSize);
		multiplyArrayByTwo(array, currentSize);
	}
	cout << "\n------------------------";


	cout << "\n----------------------------------------\n";

} // end of main





