def solve():
    n = int(input())
    s = list(input())
    
    pos_1, pos_0 = [], []
    for i, c in enumerate(s):
        if c == '1':
            pos_1.append(i+1)
        else:
            pos_0.append(i+1)
    
    if len(pos_1) % 2 == 0:
        print(len(pos_1))
        print(*pos_1)
    elif len(pos_0) % 2 == 1:
        print(len(pos_0))
        print(*pos_0)
    else:
        print(-1)
    

t = int(input())
for _ in range(t):
	solve()
