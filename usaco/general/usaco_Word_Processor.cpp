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

    freopen("word.in", "r", stdin);
    freopen("word.out", "w", stdout);

    int n, k; cin >> n >> k;
    string arr[n];
    int cnt_arr[n];

    REP(i, 0, n-1) {
        string a;
        cin >> a;
        arr[i] = a;
        cnt_arr[i] = a.size();
    }

    int i=0;
    int cnt = 0;
    while (i < n) {
        cnt += cnt_arr[i];
        if (cnt > k) {
            cnt = 0;
            cnt += cnt_arr[i];
            cout << '\n' << arr[i];
        } else {
            if (i == 0) {
                cout << arr[i];
            } else {
                cout << ' ' << arr[i];
            }
            
        }
        i++;
    }

    return 0;
}