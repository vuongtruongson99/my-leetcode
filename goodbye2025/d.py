def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    if m > 1 and 2 * m > n:
        print("-1")
        return
    
    elf = []
    for i, a in enumerate(arr):
        elf.append((a, i+1))
    elf.sort(key=lambda x: x[0])
    
    ans = []
    
    if m == 0:
        s = 0
        for i in range(n-1):
            s += elf[i][0]
        
        if s < elf[-1][0]:
            print("-1")
            return
        
        b_idx = elf[-1][1]
        for i in range(n-1):
            ans.append((elf[i][1], b_idx))
    elif m == 1:
        for i in range(n-1):
            ans.append((elf[i][1], elf[i+1][1]))
    else:
        k = n - 2 * m
        for i in range(m):
            l = (i * k) // m
            r = ((i + 1) * k) // m
            
            if r - l >= 2:
                for j in range(l, r-1):
                    ans.append((elf[j][1], elf[j+1][1]))
            if r -l >= 1:
                ans.append((elf[r-1][1], elf[k + i][1]))
        
        for i in range(m):
            ans.append((elf[k + m + i][1], elf[k+i][1]))
    
    print(len(ans))
    for i in range(len(ans)):
        print(f"{ans[i][0]} {ans[i][1]}")
                
        
        
        
t = int(input())
for _ in range(t):
	solve()
