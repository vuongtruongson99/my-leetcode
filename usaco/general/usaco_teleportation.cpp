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

// https://usaco.org/index.php?page=viewproblem2&cpid=807
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    freopen("teleport.in", "r", stdin);
    freopen("teleport.out", "w", stdout);
    
    int a, b, x, y;
    cin >> a >> b >> x >> y;

    if (a > b) { swap(a, b); }
    if (x > y) { swap(x, y); }

    int ans = min(b-a, abs(a-x) + abs(b-y));
    cout << ans << "\n";

    return 0;
}