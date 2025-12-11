def solve():
    n = int(input())
    y, r = map(int, input().split())
    
    return min(n, y // 2 + r)

t = int(input())
for _ in range(t):
	print(solve())
