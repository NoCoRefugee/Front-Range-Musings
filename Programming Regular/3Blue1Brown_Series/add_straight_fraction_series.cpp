#include <iostream>
using namespace std;

/*
	This program is going to add series' together as I follow along on the
 	3Blue1Brown natural logarithm video on youTube
*/


int simplest_series() {
/*
	This function runs the 1/x + 1/(x+1), 1/(x+2)... 1/(+n) series.  Instead of printing out the
        running sum of this series we are counting the number of terms that start with each digit.
       	So, there are three terms that start with a 1 ( 1, 1 1/2, 1 5/6... ) then seven that start with 
        a 2, and so on.       
*/
	int double_checking = 1;
	int sub_total_sum_so_far = 0;
	int counter1 = 2;
	int upper_limit_1 = 20;
	int i;

	float series_sum = 0;
	int track_for_each_digit[20] = {0};


	cout << "This function runs the 1/x + 1/(x+1), 1/(x+2)... 1/(x+n) series.  Instead of printing out the";
	cout << "running sum of this series we are counting the number of terms that start with each digit.";
	cout << "So, there are three terms that start with a 1 ( 1, 1 1/2, 1 5/6... ) then seven that start with ";
	cout << "a 2, and so on.";
	cout << "The computer is currently running that series out to " << upper_limit_1 << " terms.";

	for ( i=1; i<=upper_limit_1; i++ ) {

		series_sum = series_sum + 1/i;
		sub_total_sum_so_far++;

		if ( series_sum + ( 1 / (i+1) ) > counter1 ) {
			track_for_each_digit[i] = sub_total_sum_so_far;
			sub_total_sum_so_far = 0;
			counter1++;
		}  // end of if 

	} // end of for ( i=1...

	track_for_each_digit[i] = sub_total_sum_so_far;

	cout << "\n" << track_for_each_digit[0];
	cout << "\n" << track_for_each_digit[1];
	cout << "\n" << track_for_each_digit[2];
	cout << "\nsub_total_sum_so_far => " << sub_total_sum_so_far;
/*
	i = 1;
	for ( i=1; i<counter1; i++ ) {
		cout << "\ni => " << i << "\t" <<  track_for_each_digit[i];
		double_checking++;
	} // end of for
*/
} // end of simplest_series




int main() {

	cout << "\n------------------------------------------------------------\n";

	cout << "\nDid something happen?\n";

	simplest_series();

	cout << "\n------------------------------------------------------------\n";



} // end of main
