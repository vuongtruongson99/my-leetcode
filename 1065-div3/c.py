def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    
    a_xor, b_xor = 0, 0
    for i in range(n):
        a_xor ^= arr[i]
        b_xor ^= brr[i]
        
    if a_xor == b_xor:
        print("Tie")
        return
    
    swap_idx = -1
    for i in range(n-1, -1, -1):
        if arr[i] != brr[i]:
            swap_idx = i
            break            
            
    if swap_idx & 1:
        print("Mai")
    else:
        print("Ajisai")

    
 
t = int(input())
for _ in range(t):
	solve()
