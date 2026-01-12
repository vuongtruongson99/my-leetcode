# https://codeforces.com/contest/2001/problem/A
from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    cnt = defaultdict(int)
    for a in arr:
        cnt[a] += 1
    
    cnt_arr = sorted(cnt.items(), key=lambda item: item[1], reverse=True)
    return n - cnt_arr[0][1]
    

t = int(input())
for _ in range(t):
	print(solve())