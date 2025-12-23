def solve():
    n = int(input())
    ans = []
    
    x = (1 << n) - 1
    ans.append(x)
    
    for i in range(n-1, -1, -1):
        x &= ~(1 << i)
        ans.append(x)
        
        check = []
        for j in range(i+1, n):
            check.append(j)
        
        temp = 1 << len(check)
        for k in range(1, temp):
            new_x = x
            for m in range(len(check)):
                if (k >> m) & 1:
                    new_x |= (1 << check[m])
            ans.append(new_x)
    
    print(*ans)
                    

t = int(input())
for _ in range(t):
	solve()