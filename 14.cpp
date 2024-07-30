#include <bits/stdc++.h>
#include <iostream>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'queensAttack' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER r_q
 *  4. INTEGER c_q
 *  5. 2D_INTEGER_ARRAY obstacles
 */

bool rowObstacle(vector<vector<int>> oblist, int col) {
	for (vector<int> o : oblist) {
		if (o[1] == col)
			return true;
	}
	return false;
}

bool colObstacle(vector<vector<int>> oblist, int row) {
	for (vector<int> o : oblist) {
		if (o[0] == row)
			return true;
	}
	return false;
}

bool diagObstacle(vector<vector<int>> oblist, int r, int c) {
	for (vector<int> o : oblist) {
		if (o[0] == r && o[1] == c)
			return true;
	}
	return false;
}

int queensAttack(int n, int k, int r_q, int c_q, vector<vector<int>> obstacles) {
	cout << "Debug 1" << endl;
	vector<vector<int>> samerow;
	vector<vector<int>> samecol;
	vector<vector<int>> diag0;
	vector<vector<int>> diag1;

	cout << "Debug 2" << endl;

	int l = r_q + c_q;
	for (vector<int> o : obstacles) {
		if (o[0] == r_q)
			samerow.push_back(o);
		else if (o[1] == c_q)
			samecol.push_back(o);
		else if ((o[0] + o[1]) == l)
			diag1.push_back(o);
		else if (((o[0] + o[1]) - l) % 2 == 0)
			diag0.push_back(o);
	}

	cout << "Debug 3" << endl;

	int i = 0, j = 0;
	int res = 0;
	for (i = c_q - 1; i > 0; i--) {
		if (rowObstacle(samerow, i)) {
			break;
		}
		res += 1;
	}
	cout << "Debug 4, res: " << res << endl;

	for (i = c_q + 1; i < n + 1; i++) {
		if (rowObstacle(samerow, i)) {
			break;
		}
		res += 1;
	}

	cout << "Debug 5, res: " << res << endl;

	for (i = r_q - 1; i > 0; i--) {
		if (colObstacle(samecol, i)) {
			break;
		}
		res += 1;
	}

	cout << "Debug 6, res: " << res << endl;

	for (i = r_q + 1; i < n + 1; i++) {
		if (colObstacle(samecol, i)) {
			break;
		}
		res += 1;
	}

	cout << "1) res: " << res << endl;

	// Principal Diagonal
	i = r_q - 1;
	j = c_q - 1;
	while ((i != 0) && (j != 0)) {
		if (diagObstacle(diag0, i, j))
			break;
		res += 1;
		i -= 1;
		j -= 1;
	}
	cout << "2) res: " << res << endl;

	i = r_q + 1;
	j = c_q + 1;
	const int t = n + 1;
	while ((i != t) && (j != t)) {
		if (diagObstacle(diag0, i, j)) {
			break;
		}
		res += 1;
		i += 1;
		j += 1;
	}
	cout << "3) res: " << res << endl;

	// Other Diagonal
	i = r_q + 1;
	j = c_q - 1;
	while ((i != t) && (j != 0)) {
		if (diagObstacle(diag1, i, j))
			break;
		res += 1;
		i += 1;
		j -= 1;
	}
	cout << "4) res: " << res << endl;

	i = r_q - 1;
	j = c_q + 1;
	while ((i != 0) && (j != t)) {
		if (diagObstacle(diag1, i, j))
			break;
		res += 1;
		i -= 1;
		j += 1;
	}
	cout << "5) res: " << res << endl;
	return res;
}

int main()
{
	ofstream fout("output.txt");
	ifstream fin("input2.txt");

	string first_multiple_input_temp;
	getline(fin, first_multiple_input_temp);

	vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

	int n = stoi(first_multiple_input[0]);

	int k = stoi(first_multiple_input[1]);

	string second_multiple_input_temp;
	getline(fin, second_multiple_input_temp);

	vector<string> second_multiple_input = split(rtrim(second_multiple_input_temp));

	int r_q = stoi(second_multiple_input[0]);

	int c_q = stoi(second_multiple_input[1]);

	vector<vector<int>> obstacles(k);

	for (int i = 0; i < k; i++) {
		obstacles[i].resize(2);

		string obstacles_row_temp_temp;
		getline(fin, obstacles_row_temp_temp);

		vector<string> obstacles_row_temp = split(rtrim(obstacles_row_temp_temp));

		for (int j = 0; j < 2; j++) {
			int obstacles_row_item = stoi(obstacles_row_temp[j]);

			obstacles[i][j] = obstacles_row_item;
		}
	}

	int result = queensAttack(n, k, r_q, c_q, obstacles);

	fout << result << "\n";

	fin.close();
	fout.close();

	return 0;
}

string ltrim(const string &str) {
	string s(str);

	s.erase(
		s.begin(),
		find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
	);

	return s;
}

string rtrim(const string &str) {
	string s(str);

	s.erase(
		find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
		s.end()
	);

	return s;
}

vector<string> split(const string &str) {
	vector<string> tokens;

	string::size_type start = 0;
	string::size_type end = 0;

	while ((end = str.find(" ", start)) != string::npos) {
		tokens.push_back(str.substr(start, end - start));

		start = end + 1;
	}

	tokens.push_back(str.substr(start));

	return tokens;
}
