#include <iostream>
using namespace std;

// -------------------------------------------------------------------------------

void showArray(int* array, int currentSize) {

	cout << "\narray => ";
	for ( int i=currentSize; i>=0; i-- ) {
		cout << array[i] << ".";
	} // end of for

	cout << "\nsizeof returned => " << sizeof(array) << endl;
	for ( int i=19; i>=0; i-- ) {
		cout << array[i] << ".";
	} // end of for

} // end of showArray

// -------------------------------------------------------------------------------

// -------------------------------------------------------------------------------

int main() {

	int carryOver = 0;
	int array[20] = {0};
	int currentSize = 1;
	int numberN = 5;
	int i = 0;

	cout << "\n----------------------------------------\n";

	array[0] = 2;
	showArray(array, currentSize);
// you need to make a seperate "multiply once by 2" function
	while ( i<=numberN ) {
		cout << "\nIn the loop";
		array[i] = array[i] + carryOver;
		array[i] = array[i] * 2;
		cout << "\n=> " << array[0];
		if ( array[i] > 9 ) {
			carryOver = 1;
			array[i] = array[i]%10;
			i++;
		} // end of if
		if ( i > currentSize-1 ) {
			currentSize++;
		} // end of other if
	} // end of while 

	showArray(array, currentSize);
	

	cout << "\n----------------------------------------\n";

} // end of main





