def solve():
    n, k = map(int, input().split())
    s = input()
    
    w = [0] * n
    for i in range(n):
        if s[i] == '1':
            for j in range(0, k+1):
                if i + j < n:
                    w[i+j] = True
    ans = 0
    for i in range(n):
        if not w[i]:
            ans += 1
            
    return ans
        

t = int(input())
for _ in range(t):
	print(solve())
