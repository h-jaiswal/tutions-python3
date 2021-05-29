#include <iostream>

using namespace std;

int main() {

    void * p;
    cout<< sizeof(p) << endl;

    int * q = nullptr;
    (*q)++;
    cout << &q << endl;
    return 0;
}