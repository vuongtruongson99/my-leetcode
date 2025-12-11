def solve():
    n = int(input())
    if n & 1:
        return 0

    return (n // 4) + 1
 
t = int(input())
for _ in range(t):
	print(solve())
