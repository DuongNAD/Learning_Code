#include <stdio.h>
 #include <math.h>
#include <stdio.h>
#include <math.h>

/* 
Danh sach cac ham:
1. tinhTongTu1DenN(n) - Tinh tong cac so tu 1 den n.
// Vi du: neu n = 4 thi S = 1 + 2 + 3 + 4 = 10
2. tinhTongChanDenN(n) - Tinh tong cac so chan tu 1 den n.
// Vi du: neu n = 6 thi S = 2 + 4 + 6 = 12
3. tinhTongLeDenN(n) - Tinh tong cac so le tu 1 den n.
// Vi du: neu n = 5 thi S = 1 + 3 + 5 = 9
4. tinhTongMDenN(m, n) - Tinh tong cac so tu m den n.
// Vi du: neu m = 2, n = 5 thi S = 2 + 3 + 4 + 5 = 14
5. tinhTongChanMDenN(m, n) - Tinh tong cac so chan trong khoanh m den n.
// Vi du: neu m = 3, n = 8 thi S = 4 + 6 + 8 = 18
6. tinhTongTuMdenNDivisibleByX(m, n, x) - Tinh tong cac so chia het cho x trong khoanh m den n.
// Vi du: neu m = 1, n = 10, x = 3 thi S = 3 + 6 + 9 = 18
7. tinhTongBoiCuaX(n, x) - Tinh tong cac so tu 1 den n la boi cua x.
// Vi du: neu n = 10, x = 4 thi S = 4 + 8 = 12
8. tinhTongChiaHetChoXHoacY(n, x, y) - Tinh tong cac so chia het cho x hoac y tu 1 den n.
// Vi du: neu n = 10, x = 2, y = 3 thi S = 2 + 3 + 4 + 6 + 8 + 9 = 32
9. tinhTongChiaHetCho3(n) - Tinh tong cac so chia het cho 3 tu 1 den n.
// Vi du: neu n = 10 thi S = 3 + 6 + 9 = 18
10. tinhTongCanBacHai(n) - Tinh tong cac can bac hai tu 1 den n.
Tinh tong cac can bac hai (S = sqrt(1) + sqrt(2) + sqrt(3) + ... + sqrt(n))
11. tinhTongGiaiThua(n) - Tinh tong cac giai thua tu 1 den n.
Tinh tong cac giai thua (S = 1! + 2! + 3! + ... + n!)
12. tinhTongBinhPhuong(n) - Tinh tong cac binh phuong tu 1 den n.
Tinh tong cac binh phuong (S = 1^2 + 2^2 + 3^2 + ... + n^2)
13. tinhTongPhanSo(n) - Tinh tong cac phan so 1 + 1/2 + 1/3 + ... + 1/n.
14. tinhTongSoMu(n) - Tinh tong cac so mu tu 1 den n.
Tinh tong cac so mu (S = 1^1 + 2^2 + 3^3 + ... + n^n)
15. tinhTongCanBacHaiGiaiThua(n) - Tinh tong cac can bac hai va giai thua tu 1 den n.
S = sqrt(1) + 1! + sqrt(2) + 2! + sqrt(3) + 3! + ... + sqrt(n) + n!
16. tinhTongBinhPhuongPhanSo(n) - Tinh tong cac binh phuong va phan so tu 1 den n.
S = 1^2 + 1/1 + 2^2 + 1/2 + 3^2 + 1/3 + ... + n^2 + 1/n
17. tinhTongSoMuCanBacHai(n) - Tinh tong cac so mu va can bac hai tu 1 den n.
S = 1^1 + sqrt(1) + 2^2 + sqrt(2) + 3^3 + sqrt(3) + ... + n^n + sqrt(n)
18. tinhTongPhanSoTuChanMauBinhPhuong(n) - Tinh tong cac phan so voi mau la binh phuong va tu la so chan.
// S = 2/(1^2) + 4/(2^2) + 6/(3^2) + ... + 2n/(n^2)
19. tinhTongPhanSoGiaiThuaCanBacHai(n) - Tinh tong cac phan so voi mau la can bac hai cua giai thua.
S = 1/sqrt(1!) + 2/sqrt(2!) + 3/sqrt(3!) + ... + n/sqrt(n!)
20. tinhTongBinhPhuongGiaiThua(n) - Tinh tong cac binh phuong chia cho giai thua.
S = 1^2/1! + 2^2/2! + 3^2/3! + ... + n^2/n!
21. tinhTongCanBacHaiBinhPhuong(n) - Tinh tong cac can bac hai chia cho binh phuong.
S = sqrt(1)/1^2 + sqrt(2)/2^2 +sqrt(3)/3^2 + ... + sqrt(n)/n^2
22. tinhTongBinhPhuongGiaiThuaBí_nT?_Ýng(n) - Tinh tong cac binh phuong chia cho giai thua.
S = (1^2 / 1!) + (2^2 / 2!) + (3^2 / 3!) + ... + (n^2 / n!)
23. tinhTongBinhPhuongCanBacHaiGiaiThua(n) - Tinh tong cac binh phuong va can bac hai chia cho giai thua.
S = 1/sqrt(1!) + 4/sqrt(2!) + 9/sqrt(3!) + ... + n^2/sqrt(n!)
24. tinhTongBinhPhuongPhanSoCanBacHai(n) - Tinh tong cac binh phuong va phan so voi can bac hai.
S = 1^2/2 + 2^2/3 + 3^2/4 + ... + n^2/(n+1) + sqrt(1) + sqrt(2) + ... + sqrt(n)
25. tinhTich1_CongThuc1(n) - Tinh tich theo cong thuc (1 + 1/1) * (1 + 1/2) * ... * (1 + 1/n).
26. tinhTich2_CongThuc2(n) - Tinh tich theo cong thuc (1 + 1/1^2) * (1 + 1/2^2) * ... * (1 + 1/n^2).
27. tinhTich3_CongThuc3(n) - Tinh tich theo cong thuc (1 + sqrt(k)/(k+1)) * ... * (1 + sqrt(k)/(k+1)).
28. tinhTich4_GiaiThua(n) - Tinh tich voi cac giai thua (1 + 1!/1+1) * (1 + 2!/2+1) * .... * (1 + n!/n+1)
29. tinhTich5_CongThucGiaiThua(n) - Tinh tich ket hop voi giai thua: (1 + cbrt(1)/1+1) * (1 + cbrt(2)/2+1) * .... * (1 + cbrt(k)/k+1)
30. tinhTich6_CongThucCbrt(n) - Tinh tich voi can bac ba (1 + 1/(sqrt(1)+1^2)) * (1 + 2/(sqrt(2)+2^2)) * .... * (1 + n/(sqrt(n)+n^2))
*/

// Cac ham thuc thi tuong ung...


// 1.Tinh tong cac so tu nhien tu 1 den n
// Vi du: neu n = 4 thi S = 1 + 2 + 3 + 4 = 10
int tinhTongTu1DenN(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

// 2.Tinh tong cac so chan tu 1 den n
// Vi du: neu n = 6 thi S = 2 + 4 + 6 = 12
int tinhTongChanDenN(int n) {
    int sum = 0;
    for (int i = 2; i <= n; i += 2) {
        sum += i;
    }
    return sum;
}

// 3.Tinh tong cac so le tu 1 den n
// Vi du: neu n = 5 thi S = 1 + 3 + 5 = 9
int tinhTongLeDenN(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i += 2) {
        sum += i;
    }
    return sum;
}

// 4.Tinh tong cac so tu m den n
// Vi du: neu m = 2, n = 5 thi S = 2 + 3 + 4 + 5 = 14
int tinhTongMDenN(int m, int n) {
    int sum = 0;
    for (int i = m; i <= n; i++) {
        sum += i;
    }
    return sum;
}

// 5.Tinh tong cac so chan trong khoang m den n
// Vi du: neu m = 3, n = 8 thi S = 4 + 6 + 8 = 18
int tinhTongChanMDenN(int m, int n) {
    int sum = 0;
    for (int i = m; i <= n; i++) {
        if (i % 2 == 0) {
            sum += i;
        }
    }
    return sum;
}
// 6.Tinh tong cac so tu nhien trong khoang m den n voi dieu kien chia het cho x
// Vi du: neu m = 1, n = 10, x = 3 thi S = 3 + 6 + 9 = 18
int tinhTongTuMdenNDivisibleByX(int m, int n, int x) {
    int sum = 0;
    for (int i = m; i <= n; i++) {
        if (i % x == 0) {
            sum += i;
        }
    }
    return sum;
}

// 7.Tinh tong cac so tu 1 den n la boi cua x
// Vi du: neu n = 10, x = 4 thi S = 4 + 8 = 12
int tinhTongBoiCuaX(int n, int x) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        if (i % x == 0) {
            sum += i;
        }
    }
    return sum;
}

// 8.Tinh tong cac so tu 1 den n la các s? chia h?t cho x hoac y
// Vi du: neu n = 10, x = 2, y = 3 thi S = 2 + 3 + 4 + 6 + 8 + 9 = 32
int tinhTongChiaHetChoXHoacY(int n, int x, int y) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        if (i % x == 0 || i % y == 0) {
            sum += i;
        }
    }
    return sum;
}

// 9.Tinh tong cac so chia het cho 3
// Vi du: neu n = 10 thi S = 3 + 6 + 9 = 18
int tinhTongChiaHetCho3(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0) {
            sum += i;
        }
    }
    return sum;
}
// 10. Tinh tong cac can bac hai (S = sqrt(1) + sqrt(2) + sqrt(3) + ... + sqrt(n))
double tinhTongCanBacHai(int n) {
    double sum = 0.0;
    for (int i = 1; i <= n; i++) {
        sum += sqrt(i);  // Tinh can bac hai cua tung so i
    }
    return sum;
}

// 11. Tinh tong cac giai thua (S = 1! + 2! + 3! + ... + n!)
unsigned long long giaiThua(int n) {
    unsigned long long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;  // Tinh giai thua cua n
    }
    return result;
}

unsigned long long tinhTongGiaiThua(int n) {
    unsigned long long sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += giaiThua(i);  // Cong giai thua cua i vao tong
    }
    return sum;
}

// 12. Tinh tong cac binh phuong (S = 1^2 + 2^2 + 3^2 + ... + n^2)
int tinhTongBinhPhuong(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i * i;  // Tinh binh phuong cua i va cong vao tong
    }
    return sum;
}

// 13. Tinh tong cac phan so (S = 1 + 1/2 + 1/3 + ... + 1/n)
double tinhTongPhanSo(int n) {
    double sum = 0.0;
    for (int i = 1; i <= n; i++) {
        sum += 1.0 / i;  // C?ng phân s? vào t?ng
    }
    return sum;
}

// 14. Tinh tong cac so mu (S = 1^1 + 2^2 + 3^3 + ... + n^n)
unsigned long long tinhTongSoMu(int n) {
    unsigned long long sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += pow(i, i);  // Tinh so mu cua i va cong vao tong
    }
    return sum;
}
// 15.Ham tinh tong cac can bac hai va giai thua
// S = sqrt(1) + 1! + sqrt(2) + 2! + sqrt(3) + 3! + ... + sqrt(n) + n!
double tinhTongCanBacHaiGiaiThua(int n) {
    double sum = 0.0;

    for (int i = 1; i <= n; i++) {
        sum += sqrt(i);               // Cong can bac hai cua i
        sum += tgamma(i + 1);          // Cong giai thua cua i (tgamma(i+1) tuong duong voi i!)
    }
    
    return sum;
}

// 16.Ham tinh tong cac binh phuong va phan so
// S = 1^2 + 1/1 + 2^2 + 1/2 + 3^2 + 1/3 + ... + n^2 + 1/n
double tinhTongBinhPhuongPhanSo(int n) {
    double sum = 0.0;

    for (int i = 1; i <= n; i++) {
        sum += i * i;             // Cong binh phuong cua i
        sum += 1.0 / i;           // Cong phan so 1/i
    }
    
    return sum;
}

// 17.Ham tinh tong cac so mu va can bac hai
// S = 1^1 + sqrt(1) + 2^2 + sqrt(2) + 3^3 + sqrt(3) + ... + n^n + sqrt(n)
double tinhTongSoMuCanBacHai(int n) {
    double sum = 0.0;

    for (int i = 1; i <= n; i++) {
        sum += pow(i, i);          // Cong so mu i^i
        sum += sqrt(i);            // Cong can bac hai cua i
    }
    
    return sum;
}
// 18.Ham tinh tong phan so tu la so chan, mau la binh phuong
// S = 2/(1^2) + 4/(2^2) + 6/(3^2) + ... + 2n/(n^2)
double tinhTongPhanSoTuChanMauBinhPhuong(int n) {
    int i;
    double sum = 0.0;
    
    for (i = 1; i <= n; i++) {
        sum += (2 * i) / (pow(i, 2));   // Tinh 2i / i^2
    }

    return sum;
}

// 19.Ham tinh tong phan so tu giai thua, mau la can bac hai
// S = 1/sqrt(1!) + 2/sqrt(2!) + 3/sqrt(3!) + ... + n/sqrt(n!)
double tinhTongPhanSoGiaiThuaCanBacHai(int n) {
    int i, j;
    double sum = 0.0;

    for (i = 1; i <= n; i++) {
        double fact = 1;
        for (j = 1; j <= i; j++) {
            fact *= j;
        }
        sum += i / sqrt(fact);    // Tinh i/sqrt(i!)
    }

    return sum;
}

// 20.Ham tinh tong binh phuong va giai thua
// S = 1^2/1! + 2^2/2! + 3^2/3! + ... + n^2/n!
double tinhTongBinhPhuongGiaiThua(int n) {
    int i, j;
    double sum = 0.0;

    for (i = 1; i <= n; i++) {
        double fact = 1;
        for (j = 1; j <= i; j++) {
            fact *= j;
        }
        sum += pow(i, 2) / fact;    // Tinh i^2/i!
    }

    return sum;
}

// 21.Ham tinh tong can bac hai va binh phuong
// S = sqrt(1)/1^2 + sqrt(2)/2^2 +sqrt(3)/3^2 + ... + sqrt(n)/n^2
double tinhTongCanBacHaiBinhPhuong(int n) {
    int i;
    double sum = 0.0;

    for (i = 1; i <= n; i++) {
        sum += sqrt(i) / pow(i, 2);   // Tinh sqrt(i)/i^2
    }

    return sum;
}

// 22.Ham tinh tong binh phuong va giai thua
// S = (1^2 / 1!) + (2^2 / 2!) + (3^2 / 3!) + ...
double tinhTongBinhPhuongGiaiThuaBi?nTý?ng(int n) {
    int i, j;
    double sum = 0.0;

    for (i = 1; i <= n; i++) {
        double fact = 1;
        for (j = 1; j <= i; j++) {
            fact *= j;
        }
        sum += (pow(i, 2)) / fact;    // Tinh i^2/i!
    }

    return sum;
}

// 23.Ham tinh tong cac phan so
// S = 1/sqrt(1!) + 4/sqrt(2!) + 9/sqrt(3!) + ...
double tinhTongBinhPhuongCanBacHaiGiaiThua(int n) {
    int i, j;
    double sum = 0.0;

    for (i = 1; i <= n; i++) {
        double fact = 1;
        for (j = 1; j <= i; j++) {
            fact *= j;
        }
        sum += pow(i, 2) / sqrt(fact);  // Tinh i^2/sqrt(i!)
    }

    return sum;
}
// 24.Ham tinh tong cac so tu binh phuong va can bac hai cua phan so
// S = 1^2/2 + 2^2/3 + 3^2/4 + ... + n^2/(n+1) + sqrt(1) + sqrt(2) + ... + sqrt(n)
double tinhTongBinhPhuongPhanSoCanBacHai(int n) {
    int i;
    double sum = 0.0;

    for (i = 1; i <= n; i++) {
        sum += pow(i, 2) / (i + 1) + sqrt(i);  // Cong binh phuong va can bac hai trong phan so
    }

    return sum;
}
// 25.Ham tinh tich theo cong thuc:
// S(n) = (1 + 1/1) * (1 + 1/2) * (1 + 1/3) * .... * (1 + 1/n)
double tinhTich1_CongThuc1(int n) {
    double S = 1.0;
    int i;

    // Tinh tich cho tung phan tu cua cong thuc
    for (i = 1; i <= n; i++) {
        S *= (1 + 1.0 / i); // Tinh tich tu 1 + 1/i
    }

    return S;
}

// 26.Ham tinh tich theo cong thuc:
// S(n) = (1 + 1/1^2) * (1 + 1/2^2) * .... * (1 + 1/n^2)
double tinhTich2_CongThuc2(int n) {
    double S = 1.0;
    int i;

    // Tinh tich cho tung phan tu cua cong thuc
    for (i = 1; i <= n; i++) {
        S *= (1 + 1.0 / (i * i)); // Tinh tich tu 1 + 1/i^2
    }

    return S;
}

// 27.Ham tinh tich theo cong thuc:
// S(n) = (1 + sqrt(k)/k+1) * (1 + sqrt(2)/2+1) * .... * (1 + sqrt(k)/k+1)
double tinhTich3_CongThuc3(int n) {
    double S = 1.0;
    int i;

    // Tinh tich cho tung phan tu cua cong thuc
    for (i = 1; i <= n; i++) {
        S *= (1 + sqrt(i) / (i + 1)); // Tinh tich tu 1 + sqrt(i)/(i+1)
    }

    return S;
}

// 28.Ham tinh tich theo cong thuc:
// S(n) = (1 + 1!/1+1) * (1 + 2!/2+1) * .... * (1 + n!/n+1)
long long tinhTich4_GiaiThua(int n) {
    long long result = 1;
    int i;

    // Tinh giai thua cua tu so
    for (i = 1; i <= n; i++) {
        result *= i; // Tinh giai thua cua i
    }

    return result;
}

double tinhTich5_CongThucGiaiThua(int n) {
    double S = 1.0;
    int i;

    // Tinh tich ket hop giai thua
    for (i = 1; i <= n; i++) {
        S *= (1 + (double)tinhTich4_GiaiThua(i) / (i + 1)); // Tinh tich tu 1 + giai thua(i)/(i+1)
    }

    return S;
}

// 29.Ham tinh tich theo cong thuc:
// S(n) = (1 + cbrt(1)/1+1) * (1 + cbrt(2)/2+1) * .... * (1 + cbrt(k)/k+1)
double tinhTich6_CongThucCbrt(int n) {
    double S = 1.0;
    int i;

    // Tinh tich ket hop can bac ba (cbrt)
    for (i = 1; i <= n; i++) {
        S *= (1 + cbrt(i) / (i + 1)); // Tinh tich tu 1 + cbrt(i)/(i+1)
    }

    return S;
}

// 30.Ham tinh tich theo cong thuc:
// S(n) = (1 + 1/(sqrt(1)+1^2)) * (1 + 2/(sqrt(2)+2^2)) * .... * (1 + n/(sqrt(n)+n^2))
double tinhTich7_CongThucCanMau(int n) {
    double S = 1.0;
    int i;

    // Tinh tich ket hop sqrt va can bac hai, va ket hop mau
    for (i = 1; i <= n; i++) {
        S *= (1 + (double)i / (sqrt(i) + i * i)); // Tinh tich tu 1 + i/(sqrt(i) + i^2)
    }

    return S;
}

