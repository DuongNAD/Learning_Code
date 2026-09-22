#include<iostream>
using namespace std;
int main() {
	int so;
	cout << "1. Tim theo ten"<<endl;
	cout << "2. Tim theo tac gia"<<endl;
	cout << "3. Tim theo nha san xuat"<<endl;
	cout << "4. Tim theo tieu de"<<endl;
	cout << "Nhap so de chon ";
	cin >> so;
	switch (so) {
	case 1: cout << "Tim theo ten";
		break;
	case 2: cout << "Tim theo tac gia";
		break;
	case 3: cout << "Tim theo nha san xuat";
		break;
	case 4: cout << "Tim theo tieu de";
		break;
	default:
		cout << "Phim khong hop le";
		break;
	}
}