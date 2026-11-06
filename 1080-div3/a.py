def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    for a in arr:
        if a == 67:
            return "yes"
            
    return "no"
        
 
t = int(input())
for _ in range(t):
	print(solve())
