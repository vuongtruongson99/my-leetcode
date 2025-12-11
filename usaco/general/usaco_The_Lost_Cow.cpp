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

// https://usaco.org/index.php?page=viewproblem2&cpid=735
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    freopen("lostcow.in", "r", stdin);
    freopen("lostcow.out", "w", stdout);

    int x, y; cin >> x >> y;
    int step = 1;
    int curr = x;
    int ans = 0;

    while (1) {
        int temp = x + step;
        
        if ((x <= y && y <= temp) || (temp <= y && y <= x)) {
            ans += abs(curr - y);
            break;
        }

        ans += abs(curr - temp);
        curr = temp;
        step *= -2;
    }

    cout << ans;

    return 0;
}