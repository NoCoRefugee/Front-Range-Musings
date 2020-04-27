#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

/*
	JLF  -  April 27, 2020

	We were watching Eddie Woo talk about zero^zero = 1 and the 
	limit and we decided to write this little program to test that
	idea for outselves.  What happens as lim x->0 x^x?
*/

// -------------------------------------------------------------------

float powerize( float powerThing ) {
	
	float pT = powerThing;
	pT = pow( powerThing, powerThing );

	return pT;

} // end of powerize


// -------------------------------------------------------------------
// -------------------------------------------------------------------

int main() {

	float f1 = 1.0;
	int ct1 = 0;

	cout << "\n\n*******************************\n\n";

	cout << "\nPowers headed toward 0^0\n";

	for ( ct1 = 0; ct1 < 15; ct1 ++ ) {
	
		cout << setprecision(4) << setw(10) << "\n" << f1 << "^" << f1 << " => ";
		cout << setprecision(10) << setw(10) << powerize(f1);
		f1 = f1 / 10;
	} 
	
	cout << "\n\n*******************************\n\n";

} // end of main


// -------------------------------------------------------------------

