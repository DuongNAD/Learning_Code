#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    // Khởi tạo seed cho số ngẫu nhiên
    srand(static_cast<unsigned int>(time(0)));

    // Chọn một số ngẫu nhiên từ 1 đến 100
    int targetNumber = rand() % 100 + 1;
    int guess;
    int attempts = 0;

    cout << "Chào mừng bạn đến với trò chơi đoán số!" << endl;
    cout << "Tôi đã chọn một số từ 1 đến 100, hãy thử đoán xem đó là số nào!" << endl;

    // Vòng lặp để người chơi đoán số
    while (true) {
        cout << "Nhập số bạn đoán: ";
        cin >> guess;
        attempts++;

        if (guess < targetNumber) {
            cout << "Số bạn đoán nhỏ hơn số bí mật. Thử lại!" << endl;
        }
        else if (guess > targetNumber) {
            cout << "Số bạn đoán lớn hơn số bí mật. Thử lại!" << endl;
        }
        else {
            cout << "Chúc mừng! Bạn đã đoán đúng số sau " << attempts << " lần thử." << endl;
            break;
        }
    }

    return 0;
}