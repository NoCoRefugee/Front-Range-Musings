#include <iostream>
#include <math.h>
using namespace std;


// -------------------------------------------------------------------

float powerize( float powerThing ) {
	
	float pT = powerThing;
	pT = pow( powerThing, powerThing );

	return pT;

} // end of powerize


// -------------------------------------------------------------------
// -------------------------------------------------------------------

int main() {

	float f1 = 0.1;
	int ct1 = 0;

	cout << "\n\n*******************************\n\n";

	cout << "\nPowers headed toward 0^0\n";

	for ( ct1 = 0; ct1 < 15; ct1 ++ ) {
	
		cout << "\n" << f1 << "^" << f1 << " => " << powerize(f1);
		f1 = f1 / 10;
	} 
	
	cout << "\n\n*******************************\n\n";

} // end of main


// -------------------------------------------------------------------

