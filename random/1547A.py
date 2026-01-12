# https://codeforces.com/contest/1547/problem/A
def solve():
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())
    dirs = [(-1, 0), (1, 0), (0, 1), (0, 1)]
    
    # visisted = [[0 for _ in range(1001)] for _ in range(1001)]
    q = [(xa, ya)]
    ans = 0
    while len(q):
        for _ in range(len(q)):
            x, y = q.pop(0)
            print(x, y)
            
            if x == xb and y == yb:
                return ans
            
            for dx, dy in dirs:
                n_x, n_y = x + dx, y + dy
                if n_x == xf and n_y == yf:
                    continue
                if n_x > 0 and n_y > 0:
                    q.append((n_x, n_y))
        
        ans += 1
    return ans

t = int(input())
for _ in range(t):
	print(solve())