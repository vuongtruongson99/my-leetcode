def solve():
    k, x = map(int, input().split())
    
    return k * x + 1

t = int(input())
for _ in range(t):
	print(solve())
