def solve():
    n, x, y = map(int, input().split())
    s = input()
    p = list(map(int, input().split()))
    
    if x + y < sum(p):
        print("NO")
        return
    
    a_w, b_w = 0, 0
    a_l, a_r = 0, 0
    even_p_a, even_p_b = 0, 0
    for i in range(n):
        if s[i] == '0':
            a_w += 1
            a_l += (p[i] // 2) + 1
            a_r += p[i]
            if not (p[i] & 1):
                even_p_a += 1
        else:
            b_w += 1
            a_r += (p[i] + 1) // 2 - 1
            if not (p[i] & 1):
                even_p_b += 1
    
    remain = (x + y) - sum(p)
    min_l = a_l
    if b_w == 0:
        tmp = remain
        if tmp > even_p_a:
            tmp -= even_p_a
            min_l += (tmp + 1) // 2
    
    max_r = a_r
    if a_w > 0:
        max_r += remain
    else:
        tmp = remain
        add = 0
        if tmp < even_p_b:
            add = tmp
        else:
            add = even_p_b
            tmp -= even_p_b
            add += tmp // 2
        max_r += add
        
    if x >= min_l and x <= max_r:
        print("YES")
    else:
        print("NO")
        
        

t = int(input())
for _ in range(t):
	solve()