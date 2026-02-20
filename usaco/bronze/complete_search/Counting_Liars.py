n = int(input())
cows = []
MAX = 10**10

for i in range(n):
    pos, p = input().split()
    p = int(p)
    if pos == 'G':
        rng = [p, MAX]
    else:
        rng = [0, p]
    cows.append(rng)

ans = 1000
for i in range(n):
    left, right = cows[i][0], cows[i][1]
    
    cnt = 0
    for j in range(n):
        c_left, c_right = cows[j][0], cows[j][1]
        
        r_left = max(left, c_left)
        r_right = min(right, c_right)
        
        if r_left > r_right:
            cnt += 1
        else:
            left = r_left
            right = r_right

    ans = min(ans, cnt)

print(ans)