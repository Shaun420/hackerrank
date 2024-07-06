#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 * https://www.hackerrank.com/challenges/time-conversion/problem
 */

string timeConversion(string s) {
	string output = "";
	int hrs = stoi(s.substr(0, 2));
	string remaining = s.substr(2, 6);
	char format = s[s.size() - 2];
	if(format == 'A' && hrs == 12) {
		hrs = 0;
	}
	if(format == 'P') {
		hrs += 12;
		if(hrs >= 24) {
			hrs -= 12;
		}
	}
	string hrs_str = to_string(hrs);
	if(hrs_str.size() == 1) {
		hrs_str = hrs_str.insert(0, "0");
	}
	output = hrs_str + remaining;
	return output;
}

int main()
{
	ofstream fout(getenv("OUTPUT_PATH"));

	string s;
	getline(cin, s);

	string result = timeConversion(s);

	fout << result << "\n";

	fout.close();

	return 0;
}
