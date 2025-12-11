def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    mx = arr[0]
    cnt = 0
    ans = 0
    for i in range(1, n):

        if arr[i] < mx:
            cnt += 1
        else:
            mx = arr[i]
            ans += cnt 
            cnt = 0
    if cnt > 0:
        ans += cnt
    return ans
        

t = int(input())
for _ in range(t):
	print(solve())
