def solve():
    n, k = map(int, input().split())
    q_arr = list(map(int, input().split()))
    r_arr = list(map(int, input().split()))
    
    z = []
    for i in range(n):
        z.append((k - r_arr[i]) // (r_arr[i] + 1))
    z.sort()
    q_arr.sort()
    
    ans = 0
    cnt = 0
    for i in range(n):
        if cnt < n and z[i] >= q_arr[cnt]:
            ans += 1
            cnt += 1
    return ans
    
    
    

t = int(input())
for _ in range(t):
	print(solve())
