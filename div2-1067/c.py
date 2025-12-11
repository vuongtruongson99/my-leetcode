from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    
    prefix_sum = []
    temp = 0
    for a in arr:
        temp = max(a, temp + a)
        prefix_sum.append(temp)
        
    if not (k & 1):
        return max(prefix_sum)
    
    suffix_sum = []
    temp = 0
    for i in range(n-1, -1, -1):
        temp = max(arr[i], temp + arr[i])
        suffix_sum.append(temp)
    
    ans = -float("inf")
    for i in range(n):
        s = prefix_sum[i] + suffix_sum[n-i-1] - arr[i] + brr[i]
        ans = max(ans, s)

    return ans
    

t = int(input())
for _ in range(t):
	print(solve())
