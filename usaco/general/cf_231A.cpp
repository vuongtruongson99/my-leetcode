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

    int n; cin >> n;
    int ans = 0;
    REP(i, 1, n) {
        int x, y, z;
        cin >> x >> y >> z;
        if (x + y + z >= 2) {
            ++ans;
        }
    }

    cout << ans;

    return 0;
}