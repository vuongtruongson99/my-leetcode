# https://codeforces.com/contest/1374/problem/A
def solve():
    x, y, n = map(int, input().split())
    return ((n - y) // x) * x + y

t = int(input())
for _ in range(t):
	print(solve())
