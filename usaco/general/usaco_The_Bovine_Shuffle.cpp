#include <bits/stdc++.h>
#include <iterator>
#include <algorithm>

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

// https://usaco.org/index.php?page=viewproblem2&cpid=760
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    freopen("shuffle.in", "r", stdin);
    freopen("shuffle.out", "w", stdout);

    int n; cin >> n;
    vector<int> shuffle(n);
    for (int &i : shuffle) {
        cin >> i;
    }

    vector<int> ids(n);
    for (int &i : ids) {
        cin >> i;
    }

    for (int i=0; i<3; ++i) {
        vector<int> past_order(n);
        for (int j=0; j<n; j++) {
            past_order[j] = ids[shuffle[j] - 1];
        }

        ids = past_order;
    }

    for (const int &i : ids) { cout << i << '\n'; }    

    return 0;
}