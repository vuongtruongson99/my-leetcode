def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    
    mx, mn = 0, 0

    for i in range(n):
        nmx = max(mx - arr[i], brr[i] - mn)
        nmn = min(mn - arr[i], brr[i] - mx)
        
        mx = nmx
        mn = nmn
    return mx
        

t = int(input())
for _ in range(t):
	print(solve())
