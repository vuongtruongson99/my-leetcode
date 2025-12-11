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

    int arr[7];
    REP(i, 0, 6) {
        cin >> arr[i];
    }
    sort(arr, arr + 7);

    cout << arr[0] << ' ' << arr[1] << ' ' << arr[6] - arr[0] - arr[1];

    return 0;
}