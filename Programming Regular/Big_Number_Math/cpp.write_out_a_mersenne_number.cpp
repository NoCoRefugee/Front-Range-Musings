#include <iostream>
using namespace std;

int testNumber = 50;
int arraySize  = 10000;

// -------------------------------------------------------------------------------

void showArray(int* array, int currentSize) {

	// all the "counter1" stuff is here to put commas in the output
	int counter1 = 1;

	// all the "counter1" stuff is here to put commas in the output
	if (( (currentSize+1)%3) == 1 ) counter1 = 0;
	if (( (currentSize+1)%3) == 2 ) counter1 = 2;

	cout << "\n";

	for ( int i=currentSize; i>=0; i-- ) {
		cout << array[i];
		// all the "counter1" stuff is here to put commas in the output
		if (( counter1 == 0 ) && ( i>1 )) { cout << ","; }
		// all the "counter1" stuff is here to put commas in the output
		counter1++;
		if ( counter1 == 3 ) counter1 = 0;
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


	int array[arraySize];
	int currentSize = 0;
	int numberN = testNumber;

	cout << "\n----------------------------------------\n";
	cout << "\nfrom a C++ program:";

	// initialize array to zero's, cause apparently you can't do that
	// in the variable declaration if the array size is set to a variable
	for ( int i=arraySize; i>0; i-- ) {
		array[i-1] = 0;
	}	
	
	array[0] = 2;

	for ( int i=0; i<numberN-1; i++ ) {
		multiplyArrayByTwo(array, currentSize);
	}

	cout << "\nMersenne ( 2^" << numberN << " - 1 ) makes => \n";
	array[0]--;
	showArray(array, currentSize);

	cout << "\nThe size of this mess is => " << currentSize+1;

	cout << "\n----------------------------------------\n";

} // end of main





