# https://codeforces.com/contest/279/problem/B
def solve():
    n, t = map(int, input().split())
    arr = list(map(int, input().split()))
    
    if len(arr) == 1:
        return 1 if arr[0] <= t else 0
    
    ans = 0
    i, j = 0, 0
    s = 0
    while j < n:
        if s > t:
            ans = max(ans, j - i - 1)
            s -= arr[i]
            i += 1

        s += arr[j]
        j += 1

    if s > t:
        ans = max(ans, j - i - 1)
    else:
        ans = max(ans, j - i)
    
    return ans

def solve2():
    n, t = map(int, input().split())
    arr = list(map(int, input().split()))
    
    r = 0
    s = 0
    ans = 0
    
    for i in range(n):
        while r < n and s + arr[r] <= t:
            s += arr[r]
            r += 1
        ans = max(ans, r - i)
        s -= arr[i]
    return ans
    

print(solve2())