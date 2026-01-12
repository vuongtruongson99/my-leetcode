import math

def solve():
    MOD = 998244353
    n = int(input())
    arr = list(map(int, input().split()))
    
    src, remains = arr[0], arr[1:]
    total = sum(arr)
    
    base_val = total // n
    num_p = total % n
    num_remain = n - num_p
    
    cost_base = 0
    cnt_sml = 0
    for i in range(len(remains)):
        if remains[i] < base_val:
            cost_base += (base_val - remains[i])
        if remains[i] <= base_val:
            cnt_sml += 1

    cnt_lg = n - cnt_sml
    remain_a = src - cost_base
    if remain_a < 0:
        return 0
    
    ans = 0
    for i in range(num_p + 1):
        if i > remain_a:
            break
        
        need = num_p - i
        if i <= cnt_sml and need <= cnt_lg:
            w = math.comb(cnt_sml, i) % MOD * math.comb(cnt_lg, need) % MOD
            ans = (ans + w) % MOD
    
    factor = math.factorial(num_p) % MOD * math.factorial(num_remain) % MOD
    return (ans * factor) % MOD


t = int(input())
for _ in range(t):
    print(solve())
