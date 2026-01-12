from collections import defaultdict

def solve():
    MOD = 998244353
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    g = defaultdict(list)
    edges = []

    for i in range(m):
        v, u = map(int, input().split())
        v -= 1
        u -= 1
        g[v].append((arr[u], i))
        edges.append((v, u))


    g2 = [defaultdict(list) for _ in range(n)]
    for u in range(n):
        for w, eid in g[u]:
            g2[u][w].append(eid)

    dp = [-1] * m

    def dfs(i, visited):
        nonlocal dp 
        
        if dp[i] != -1:
            return dp[i]
        
        visited[i] = 1

        v, u = edges[i]
        next = arr[v] + arr[u]
        res = 1

        if next in g2[u]:
            for nxt in g2[u][next]:
                if visited[nxt]:
                    continue
                res = (res + dfs(nxt, visited)) % MOD

        dp[i] = res
        return res

    ans = 0
    for i in range(m):
        visited = [0] * m
        ans = (ans + dfs(i, visited)) % MOD

    print(ans)


t = int(input())
for _ in range(t):
    solve()
