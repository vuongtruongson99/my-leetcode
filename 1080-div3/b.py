def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(n+1):
        a = arr[i-1]
        while a:
            if a % 2 == 0:
                a //= 2
        idx = i
        while idx and idx % 2 == 0:
            idx //= 2
        
        if a != idx:
            return "No"
    return "Yes"
        
 
t = int(input())
for _ in range(t):
	print(solve())
