#include <iostream>
using std::cout;
using std::ostream;

struct Vector {
    double x, y;
};

ostream& operator<<(ostream& out, const Vector& v) {
    out << '(' << v.x << ", " << v.y << ')';
    return out;
}

bool BinSearch(int* beg, int* end, int val) {
    if(end - beg == 1)
        return *beg == val;
    int* mid = beg + (end - beg)/2;

    if(*mid > val)
        return BinSearch(beg, mid, val);
    else
        return BinSearch(mid, end, val);
}

int main() {
    if(false) {
        int a = 5;
        int& b = a;

        cout << a << ' ' << b << '\n';

        a = 7;

        cout << a << ' ' << b << '\n';

        b++;

        cout << a << ' ' << b << '\n';

        int c = 5;
        int* d = &c;

        cout << c << ' ' << d << ' ' << *d << '\n';
        cout << d + 1 << ' ' << *(d + 1) << '\n';
        cout << *(d + 1) << ' ' << d[1] << ' ' << 1[d] << '\n';
        int* e = d + 1;

        int mas[7] = {1, 3, 4, 5, 7, 9, 11};
        cout << BinSearch(mas, mas + 7, 3) << '\n';
    }
    volatile int a, b, c;
    a = b = c = 0;
    *(&a + (&c - &a)/2) = 1;
    cout << a << b << c << '\n';


    int* mas = new int[21];
    mas += 10;
    delete[] (mas-10);
}