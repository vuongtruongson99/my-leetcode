def solve():
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    
    cnt = 1
    for i in range(n):
        for j in range(n):
            arr[i][j] = cnt
            cnt += 1
            
    ans = 0
    directions = [(-1, 0), (1,0),(0,1),(0,-1)]
    for i in range(n):
        for j in range(n):
            local = arr[i][j]
            for dx, dy in directions:
                nx,ny = i+dx, j+dy
                if 0<=nx<n and 0<=ny<n:
                    local += arr[nx][ny]
            ans = max(ans, local)
    return ans

t = int(input())
for _ in range(t):
	print(solve())
