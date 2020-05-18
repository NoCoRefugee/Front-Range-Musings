#include <iostream>
using namespace std;

// fucking variables

// this is a little test of variable passing in functions, cause our
// big_number program is not changing variables like we expect, WTF?

// jlf  -  20200517

void testFunction(int &someInt) {

	someInt++;

}

// ---------------------------------------------------------------

int main() {

	int someInt = 0;

	cout << "\n---------------------------------------------------------------\n";

	cout << "\nsomeInt => " << someInt;

	testFunction(someInt);

	cout << "\nsomeInt => " << someInt;
	
	cout << "\n---------------------------------------------------------------\n";

}  // end of main



