def solve():
    _ = int(input())
    s = input()
    
    max_0 = 0
    cnt = 0
    new = s + s
    for i in range(len(new)):
        if new[i] == '0':
            cnt += 1
        else:
            max_0 = max(max_0, cnt)
            cnt = 0
    
    return max_0
    

t = int(input())
for _ in range(t):
	print(solve())
