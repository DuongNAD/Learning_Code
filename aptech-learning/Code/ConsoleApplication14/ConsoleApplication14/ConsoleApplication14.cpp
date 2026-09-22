#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n]; // array declaration

    // Input the array elements
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Output the array elements
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " "; // printing elements with space in between
    }
    cout << endl; // print a new line after all elements

    return 0; // return 0 at the end of main function
}