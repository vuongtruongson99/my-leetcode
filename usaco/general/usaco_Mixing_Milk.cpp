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

    freopen("mixmilk.in", "r", stdin);
    freopen("mixmilk.out", "w", stdout);

    int a1,b1,a2,b2,a3,b3;
    cin >>a1>>b1>>a2>>b2>>a3>>b3;
    int arr[3] = {a1, a2, a3};
    int brr[3] = {b1, b2, b3};

    for (int i=0;i<100;i++) {
        int curr = i % 3;
        int next = ((i%3) + 1)%3;
        int mn = min({brr[curr], arr[next] - brr[next]});
        brr[curr] -= mn;
        brr[next] += mn;
    }

    for (int i=0;i<3;++i) {
        cout << brr[i] << '\n';
    }

    return 0;
}