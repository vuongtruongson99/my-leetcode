def solve():
    s = input()
    cnt = 0
    
    if s[0] == 'u':
        cnt += 1
    if s[-1] == 'u':
        cnt += 1
    
    cnt_u = 0
    for i in range(1, len(s) - 1):
        if s[i] == 'u':
            cnt_u += 1
        else:
            if cnt_u > 1:
                cnt += (cnt_u // 2)
            cnt_u = 0
    if cnt_u > 1:
        cnt += (cnt_u // 2)
    return cnt
    
        

t = int(input())
for _ in range(t):
	print(solve())
