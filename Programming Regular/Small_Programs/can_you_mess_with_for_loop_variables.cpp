#include <iostream>
using namespace std;

// the point of this program is to test if we can manipulate the 
// control variable in a for loop.  And it turns out we can.

// jlf  -  20200517

int main() {


	cout << "\n--------------------------------------------------------------------\n";


	cout << "\nThis is a for loop writen to loop 20 times,";
	cout << "\nexcept that we sabotaged it by changing the ";
	cout << "\nloop variable mid stream just to see what would ";
	cout << "\nhappen.\n";

	// and now for a run of the mill for loop:
	for ( int i=0; i<20; i++ ) {

		cout << "\ni => " << i;

		// change i and see if that is picked up:
		if ( i == 6 ) { i = 9; } 

		// do it again in a way that ends the loop:
		if ( i == 15 ) { i = 21; } 

	} // end of for loop


	cout << "\n\n--------------------------------------------------------------------\n";


} // end of main






