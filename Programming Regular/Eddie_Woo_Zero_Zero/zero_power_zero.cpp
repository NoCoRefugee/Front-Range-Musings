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
	float holder = 1.0;
	int ct1 = 0;

	cout << "\n\n*******************************\n\n";

	cout << "\nPowers headed toward 0^0\n";

	while ( f1 > 0 ) {
		cout << fixed << "\n";

		cout << setprecision(6) << f1 << "^" << f1 << " => ";
		holder = powerize(f1);
		cout << setprecision(10) << setw(20) << holder;
		f1 = f1 - .05;
	} 

	cout << "\n------------------------------------------------\n";

	f1 = .01;	
	while ( f1 > 0.000000001 ) {
		cout << fixed << "\n";

		cout << setprecision(6) << f1 << "^" << f1 << " => ";
		holder = powerize(f1);
		cout << setprecision(10) << setw(20) << holder;
		f1 = f1 / 10;
	} 
	
	cout << "\n\n*******************************\n\n";

} // end of main


// -------------------------------------------------------------------

