double calculateS(int x, int n) {
    double s = 0;
    double power = 1;
    for (int i = 1; i <= n; i++) {
        power *= x;
        s += power;   
    }
    return s;
}