# https://codeforces.com/contest/1607/problem/B
def solve():
    x, n = map(int, input().split())
    d = [0, n, -1, -n-1]
    
    return x + d[n % 4] if x & 1 else x - d[n % 4]

t = int(input())
for _ in range(t):
	print(solve())