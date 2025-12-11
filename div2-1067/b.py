from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = defaultdict(int)
    
    for i in range(2 * n):
        cnt[arr[i]] += 1
    
    odd, even = 0, 0
    for k, v in cnt.items():
        if v & 1:
            odd += 1
        else:
            even += 1
    
    ans = odd + 2 * even
    if not odd:
        if even % 2 != n % 2:
            ans -= 2
    return ans

t = int(input())
for _ in range(t):
	print(solve())
