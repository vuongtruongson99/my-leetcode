def solve():
    n = int(input())
    arr = list(map(str, input().split()))
    s = ""
    for i in range(n):
        s = min(s + arr[i], arr[i] + s)
    
    return s
        

t = int(input())
for _ in range(t):
	print(solve())