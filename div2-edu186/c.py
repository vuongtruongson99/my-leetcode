def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    crr = list(map(int, input().split()))
    
    ab = 0
    bc = 0
    for i in range(n):
        check_ab = True
        for j in range(n):
            if arr[j] >= brr[(j + i) % n]:
                check_ab = False
                break
        if check_ab:
            ab += 1
            
        check_bc = True
        for j in range(n):
            if brr[j] >= crr[(j + i) % n]:
                check_bc = False
                break
        if check_bc:
            bc += 1

    return ab * bc * n
    
t = int(input())
for _ in range(t):
	print(solve())
