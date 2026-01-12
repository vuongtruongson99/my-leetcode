def solve():
    a, b = map(int, input().split())
    sum_odd, sum_even = 0, 0
    ans = 0
    
    while 1:
        tmp = 1 << ans
        tmp_odd, tmp_even = sum_odd, sum_even
        if (ans + 1) & 1:
            tmp_odd += tmp
        else:
            tmp_even += tmp
            
        if (tmp_odd <= a and tmp_even <= b) or (tmp_odd <= b and tmp_even <= a):
            sum_odd = tmp_odd
            sum_even = tmp_even
            ans += 1
        else:
            return ans
            
    

t = int(input())
for _ in range(t):
	print(solve())
