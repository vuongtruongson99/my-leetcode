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

    freopen("speeding.in", "r", stdin);
    freopen("speeding.out", "w", stdout);

    int n, m;
    cin >> n >> m;

    int speed[101];
    int idx = 1;
    REP(i, 0, n-1) {
        int a, b;
        cin >> a >> b;
        for (int j=0; j<a; ++j) {
            speed[idx + j] = b;
        }
        idx += a;
    }

    int ans = 0;
    idx = 1;
    REP(i, 0, m-1) {
        int a, b;
        cin >> a >> b;
        for (int j=0; j<a; ++j) {
            ans = max({ans, b - speed[idx + j]});
        }
        idx += a;
    }

    cout << ans;

    return 0;
}