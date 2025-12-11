import bisect

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(list(set(arr)))
    
    check = [0] * len(arr)
    ans = []
    for i in range(0, len(arr)):
        if check[i]:
            continue
        b = arr[i]
        c = True
        
        for j in range(b * 2, k + 1, b):
            idx = bisect.bisect_left(arr, j)
            if idx == len(arr) or (idx < len(arr) and arr[idx] != j):
                c = False
                break
            
            check[idx] = True
            j += b
        
        if not c:
            print(-1)
            return
        
        ans.append(b)
    
    print(len(ans))
    print(*ans)
        

t = int(input())
for _ in range(t):
	solve()
