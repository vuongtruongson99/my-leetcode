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

// https://usaco.org/index.php?page=viewproblem2&cpid=856

struct Cow {
    int start, end;
    int buckets;
};


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    freopen("blist.in", "r", stdin);
    freopen("blist.out", "w", stdout);

    int n; cin >> n;
    vector<Cow> cows(n);
    for (auto &cow : cows) {
        cin >> cow.start >> cow.end >> cow.buckets;
    }

    int ans = 0;

    for (int i=1; i <= 1000; ++i) {
        int curr_bucket = 0;
        for (auto cow : cows) {
            if (cow.start <= i and cow.end >= i) {
                curr_bucket += cow.buckets;
            }
        }

        ans = max({ans, curr_bucket});
    }

    cout << ans;

    return 0;
}