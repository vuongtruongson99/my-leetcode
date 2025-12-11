def solve():
	k, x = map(int, input().split())
	for i in range(k):
		x *= 2
	return x
 
n = int(input())
for _ in range(n):
	print(solve())
