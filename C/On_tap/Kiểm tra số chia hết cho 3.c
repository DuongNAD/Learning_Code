// Kiểm tra số chia hết cho 3
int divisibleBy3(const char *num) {
    int sum = 0;
    for (int i = 0; num[i] != '\0'; i++) {
        if (num[i] == '-') continue; // Bỏ qua dấu âm
        sum += num[i] - '0';
    }
    return (sum % 3 == 0);
}
