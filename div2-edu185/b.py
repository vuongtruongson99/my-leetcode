def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    new_arr = []
    for i in range(n):
        if arr[i] != 0:
            new_arr.append(arr[i])
    s = sum(new_arr)

    return min(len(new_arr), s - n + 1)

t = int(input())
for _ in range(t):
	print(solve())
