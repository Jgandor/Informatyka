#include <iostream>
using namespace std;


bool sprawdz_bok(int x, int y, int z)
{
    if (x+y <= z)
    {
        cout << x << "+" << y << "=" << x+y << " <= " << z << endl;
        return false;
    }
    return true;
}

bool sprawdz5(int a, int b, int c)
{  
    return sprawdz_bok(a, b, c) && sprawdz_bok(b, c, a) && sprawdz_bok(a, c, b);
}

/*

bool sprawdz4(int a, int b, int c)
{
    if (!sprawdz_bok(a, b, c))
        return false;
    if (!sprawdz_bok(b, c, a))
        return false;
    if (!sprawdz_bok(a, c, b))
        return false;
   
    return true;
}

bool sprawdz3(int a, int b, int c)
{
    if (a+b < c)
    {
        cout << a << "+" << b << "=" << a+b << " < " << c << endl;
        return false;
    }
    if (b+c > a)
        return false;
    if (a+c > b)
        return false;
   
    return true;
}

bool sprawdz2(int a, int b, int c)
{
    if (a+b < c)
        return false;
    if (b+c > a)
        return false;
    if (a+c > b)
        return false;
   
    return true;
}


bool sprawdz(int a, int b, int c)
{
    return a+b > c && b+c > a && a+c > b;
}
*/

int main()
{
    int a, b, c;
    cout << "Podaj bok a: ";
    cin >> a;
    cout << "Podaj bok b: ";
    cin >> b;
    cout << "Podaj bok c: ";
    cin >> c;
    if (sprawdz5(a, b, c))
        cout << "To jest trojkat" << endl;
    else
        cout << "To NIE jest trojkat" << endl;
   
    return 0;
}
