#include<iostream>
using namespace std;
int main() {
	int n=10;
	while (n>=1 && n<=50) {
		if (n % 3 == 0) {
			cout << n << endl;
		}
		n++;
	}
	return 0;
}