from math import gcd

def solve():
	n = int(input())
	p = list(map(int, input().split()))
	ans = []
	for i in range(n):
		ans.append(n + 1 - p[i])
	return ans

t = int(input())
for _ in range(t):
	result = solve()
	print(*result)
