def solve():
    l, a, b = map(int, input().split())
    ans = 0
    for i in range(5000):
        ans = max(ans, (a + i*b) % l)
    return ans
        

t = int(input())
for _ in range(t):
	print(solve())