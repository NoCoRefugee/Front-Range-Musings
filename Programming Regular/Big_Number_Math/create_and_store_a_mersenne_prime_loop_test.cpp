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
	int i = 0;

	for ( i=0; i<6; i++ ) {
		array[i] = array[i] * 2;
		array[i] = array[i] + carryOver;
		if ( array[i] > 9 ) {
			carryOver = 1;
			array[i] = array[i]%10;
		} 
		else { carryOver = 0; }

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
		multiplyArrayByTwo(array, currentSize);
		showArray(array, currentSize);
	}
	cout << "\n------------------------";

	cout << "\n----------------------------------------\n";

} // end of main





