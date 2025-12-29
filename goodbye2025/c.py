def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    curr, best = -arr[n-1], arr[n-1]
    ans = 0
    
    for i in range(n-2, -1, -1):
        tmp = curr + max(0, arr[i] + best)
        curr -= arr[i]
        best = max(best, tmp - curr)
        
        if i == 0:
            ans = tmp
    return ans
        
t = int(input())
for _ in range(t):
	print(solve())
