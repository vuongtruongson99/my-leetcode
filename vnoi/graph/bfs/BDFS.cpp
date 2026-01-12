#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 1e5 + 7;

int n, m, components = 0;
bool visited[MAX_N];
vector <int> g[MAX_N];

void bfs(int s) {
    ++components;
    queue<int> q;
    q.push(s);
    visited[s] = true;

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
}

int main() {
    cin >> n >> m;
    while (m--) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    fill_n(visited, n+1, false);

    for (int i=0; i<n; i++) {
        if (!visited[i]) {
            bfs(i);
        }
    }

    cout << components;

    return 0;
}