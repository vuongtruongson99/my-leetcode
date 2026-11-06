import math
def solve():
    n, h, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    ans = 0
    total = sum(arr)
    times = h // total
    mod = h % total
    remain = h - (times * total)
    
    if mod == 0:
        return times * n + (times - 1) * k
    
    ans = times * (n + k)
    
    for i in range(n):   
        remain -= arr[i]
        print(remain)
        if remain <= mx:
            ans += i + 1
            break
    return ans
        
        
    
    

t = int(input())
for _ in range(t):
	print(solve())
