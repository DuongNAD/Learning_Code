#include<iostream >
using namespace std;
int main() {
	for (int i = 1; i <= 7; i++) {
		for (int j = 1; j <= 7; j++) {
			cout << i << j << " ";
		}
		cout << endl;
	}
	cout << endl;
	cout << endl;
	cout << endl;
	for (int i = 1; i <= 7; i++) {
		for (int j = 1; j <= 7; j++) {
			if (j == i || j == 1 || j == 7) {
				cout << "*" << " ";
			}
			else {
				cout << " " << " ";
			}
		}
		cout << endl;
	}
	cout << endl;
	cout << endl;
	cout << endl;
	for (int i = 1; i <= 7; i++) {
		for (int j = 1; j <= i; j++) {
			cout << " " << "*";
		}
		cout << endl;
	}
	return 0;
}