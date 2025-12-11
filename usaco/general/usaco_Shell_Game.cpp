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

// https://usaco.org/index.php?page=viewproblem2&cpid=891
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    freopen("shell.in", "r", stdin);
    freopen("shell.out", "w", stdout);

    int n; cin >> n;
    vector<int>shell(3);
    for (int i = 0; i < n; ++i) {
        shell[i] = i;
    }

    vector<int>counter(3);
    for (int i=0;i<n;++i) {
        int a, b, g;
        cin >> a >> b >> g;
        a--,b--,g--;

        swap(shell[a], shell[b]);
        counter[shell[g]]++;
    }

    cout << max({counter[0], counter[1], counter[2]});


    return 0;
}