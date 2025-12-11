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

// https://usaco.org/index.php?page=viewproblem2&cpid=591
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    freopen("promote.in", "r", stdin);
    freopen("promote.out", "w", stdout);
    
    int bi, bo, si, so, gi, go, pi, po;
    cin >> bi >> bo >> si >> so >> gi >> go >> pi >> po;

    int db = bo - bi;
    int ds = so - si;
    int dg = go - gi;
    int dp = po - pi;

    cout << ds + dg + dp << "\n" << dg + dp << "\n" << dp;

    return 0;
}