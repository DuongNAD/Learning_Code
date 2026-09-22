#include<iostream>
#include<cmath>
using namespace std;

bool nt(int n) {
	if (n < 2)
		return false;
	for (int i = 2; i <= sqrt(n); i++)
	{
		if (n % i == 0) return false;
	}
	return true;
}

int main() {
	int n;
	cin >> n;
	int arr[n];
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	for (int i = 0; i < n; i++)
	{
		if (nt(arr[i]))
		{
			cout << arr[i] << " ";
		}
	}
	return 0;
}