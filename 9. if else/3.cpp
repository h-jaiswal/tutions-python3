#include <bits/stdc++.h>

using namespace std;

int main() {
    long long T;
    cin >> T;

    while (T > 0)
    {
        long long n, r;
        cin>>n>>r;

        vector<long long> a;
        vector<long long> b;

        long long tension = 0;
        for (long long i = 0; i < n; i++)
        {
            long long temp;
            cin >> temp;
            a.push_back(temp);
        }
        for (long long i = 0; i < n; i++)
        {
            long long temp;
            cin >> temp;
            b.push_back(temp);
        }

        long long maxTension = 0;

        for (long long i = 0; i < n; i++)
        {
            if (i != 0) 
            {
                tension -= (a[i] - a[i-1]) * r;
                if (tension < 0) {
                    tension = 0;
                }
                if (tension > maxTension) {
                    maxTension = tension;
                }
            }

            tension += b[i];

            if (tension > maxTension) {
                maxTension = tension;
            }
        }

        cout << tension<< endl;

        T--;
    }
    
    return 0;
}