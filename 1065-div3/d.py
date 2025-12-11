def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    min_curr = float('inf')
    can = True
    for i in range(n-1):
        min_curr = min(arr[i], min_curr)
        if min_curr == n - i:
            can = False
            break
        
    print("Yes") if can else print("No")

    
 
t = int(input())
for _ in range(t):
	solve()
