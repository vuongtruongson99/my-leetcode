def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(1, n-1):
        if arr[i] == -1:
            arr[i] = 0
    
    if arr[0] == -1 and arr[n-1] == -1:
        arr[0] = 0
        arr[n-1] = 0
    
    elif arr[0] == -1 and arr[n-1] != -1:
        arr[0] = arr[n-1]
    
    elif arr[0] != -1 and arr[n-1] == -1:
        arr[n-1] = arr[0]
    
    print(abs(arr[n-1] - arr[0]))
    print(*arr)
        
    
    
 
t = int(input())
for _ in range(t):
	solve()
