def solve():
    n = int(input())
    s = input()
    
    cnt5 = 0    
    cnt6 = n
    for i in range(0, n-3):
        if s[i] == '2' and s[i+1] == '0' and s[i+2] == '2' and s[i+3] == '5':
            cnt5 += 1
        
        curr = 0
        if s[i] != '2':
            curr += 1
        if s[i+1] != '0':
            curr += 1
        if s[i+2] != '2':
            curr += 1
        if s[i+3] != '6':
            curr += 1
        if curr < cnt6:
            cnt6 = curr
            
    if cnt5 < cnt6:
        return cnt5
    else:
        return cnt6

t = int(input())
for _ in range(t):
	print(solve())
