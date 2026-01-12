// https://www.spoj.com/PTIT/problems/BCDAISY/
#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 250;

int n, m;
bool visited[MAX_N];
vector <int> g[MAX_N];

int main() {
    cin >> n >> m;
    while (m--) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    fill_n(visited, n+1, false);

    queue <int> q;
    q.push(1);
    visited[1] = true;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (auto v : g[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }

    return 0;
}