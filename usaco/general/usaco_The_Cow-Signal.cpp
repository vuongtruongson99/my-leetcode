#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = a; i <= b; i++)
#define SQ(a) (a)*(a)


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    freopen("cowsignal.in", "r", stdin);
    freopen("cowsignal.out", "w", stdout);

    int m, n, k;
    cin >> m >> n >> k;

    vector<string>output;
    vector<string>arr(m);
    for (int i=0; i<m;++i) {
        string a;
        cin >> a;
        string out;
        for (char c : a) {
            for (int j=0; j<k; ++j) {
                out.push_back(c);
            }
        }

        for (int j=0; j<k; ++j) {
            output.push_back(out);
        }
    }

    for (size_t i = 0; i < output.size(); i++) {
        cout << output[i];
        if (i + 1 < output.size()) cout << '\n';
    }


    return 0;
}