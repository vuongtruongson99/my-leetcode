#include <bits/stdc++.h>
#include <cstdio>

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

    freopen("paint.in", "r", stdin);
    freopen("paint.out", "w", stdout);
    
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    vector<bool> cover(100);
    for (int i = a; i < b; ++i) {
        cover[i] = true;
    }

    for (int i = c; i < d; ++i) {
        cover[i] = true;
    }

    int ans = 0;
    for (int i = 0; i < cover.size(); ++i) {
        if (cover[i]) {
            ++ans;
        }
    }

    cout << ans;

    return 0;
}