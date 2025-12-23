def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    s = 0
    for i in range(n-1):
        s += abs(arr[i] - arr[i+1])
        
    ans = s
    if n > 1:
        ans = min(ans, s - abs(arr[0] - arr[1]))
        ans = min(ans, s - abs(arr[n-2] - arr[n-1]))
    
    for i in range(1, n-1):
        curr = s
        curr -= abs(arr[i-1] - arr[i])
        curr -= abs(arr[i] - arr[i+1])
        curr += abs(arr[i-1] - arr[i+1])
        ans = min(ans, curr)
    
    return ans

t = int(input())
for _ in range(t):
	print(solve())
