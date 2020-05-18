#include <iostream>
using namespace std;

int testNumber = 110503;
int arraySize  = 100000;

// -------------------------------------------------------------------------------

void showArray(int* array, int currentSize) {

	int counter1 = 0;

	cout << "\n";

	for ( int i=currentSize; i>=0; i-- ) {
		cout << array[i];
		counter1++;
	} // end of for

} // end of showArray

// -------------------------------------------------------------------------------

void multiplyArrayByTwo(int* array, int& currentSize) {

	
	int carryOver = 0;
	int i = 0;

//	for ( i=0; i<=10; i++ ) {
	for ( i=0; i<=currentSize; i++ ) {
		array[i] = array[i] * 2;
		array[i] = array[i] + carryOver;
		if ( array[i] > 9 ) {
			carryOver = 1;
			array[i] = array[i]%10;
			if ( i >= currentSize ) { currentSize++; }
		} 
		else { carryOver = 0; }

	} // end of for 

} // end of multiplyArrayByTwo

// -------------------------------------------------------------------------------

int main() {


	int array[arraySize] = {0};
	int currentSize = 0;
	int numberN = testNumber;

	cout << "\n----------------------------------------\n";

	array[0] = 2;

	for ( int i=0; i<numberN-1; i++ ) {
		multiplyArrayByTwo(array, currentSize);
	}

	cout << "\nMersenne ( 2^" << numberN << " - 1 ) makes => \n";
	array[0]--;
	showArray(array, currentSize);

	cout << "\n----------------------------------------\n";

} // end of main





