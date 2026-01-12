# https://codeforces.com/contest/1979/problem/A
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    mx = []
    for i in range(n-1):
        m = max(arr[i], arr[i+1])
        mx.append(m)
    
    return min(mx) - 1
    

t = int(input())
for _ in range(t):
	print(solve())
