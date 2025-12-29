def solve():
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'Y':
            cnt += 1
    
    return "NO" if cnt > 1 else "YES"
    
    

t = int(input())
for _ in range(t):
	print(solve())
