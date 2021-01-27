#include <iostream>
#include <string>
using namespace std;



void makeLine(string someWord) {
/*
      This function makes a line.  It's only purpose is 
      to make the output more readable in the terminal.
*/

      cout << "\n\n-- "
            << someWord
            << " -------------------"
            << "-------------------------------\n\n";

} // end of makeLine


int main() {

      string word1[10];

      makeLine("start");

      cout << "\nProbably should have had some content to this program...\n";

      makeLine("end  ");


} // end of main
/*
total 120
drwxr-xr-x  10 jlf  staff    320 Jan  1 16:46 .
drwxr-xr-x  11 jlf  staff    352 Dec 18 01:45 ..
-rw-r--r--   1 jlf  staff  12288 Jan  1 16:46 .junk.cpp.swp
-rwxr-xr-x   1 jlf  staff  24500 Jan  1 16:45 a.out
-rw-r--r--   1 jlf  staff    760 May  7  2020 big_numbers_python_practice.py
-rw-r--r--   1 jlf  staff    886 May 17  2020 can_you_mess_with_for_loop_variables.cpp
-rw-r--r--   1 jlf  staff    488 Jan  1 16:45 junk.cpp
-rwxr-xr-x   1 jlf  staff   1593 Dec 27 04:27 list_comp.py
-rw-r--r--   1 jlf  staff    661 May 17  2020 pass_variables_with_changes_check.cpp
-rwxr-xr-x   1 jlf  staff   1595 May  7  2020 python_tips.py


a.out
big_numbers_python_practice.py
can_you_mess_with_for_loop_variables.cpp
junk.cpp
list_comp.py
pass_variables_with_changes_check.cpp
python_tips.py


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

*/







