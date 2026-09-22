#include<iostream>
using namespace std;
int main() {
	for (int i = 4; i >=1; i--) {
		for (int j = 1; j <= i; j++) {
			if (i == j || i == 1 || j == 1) {
				cout << "*" << " ";
			}
			else {
				cout << " " << " ";
			}
	    }
		cout << endl;
	}
	return 0;
}