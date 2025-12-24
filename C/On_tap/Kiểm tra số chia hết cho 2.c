// Ki?m tra s? chia h?t cho 2
int divisibleBy2(const char *num) {
    int last_digit = num[strlen(num) - 1] - '0';
    return (last_digit % 2 == 0);
}