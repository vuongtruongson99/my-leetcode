def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    return max(arr[0], arr[1] - arr[0])

t = int(input())
for _ in range(t):
	print(solve())
