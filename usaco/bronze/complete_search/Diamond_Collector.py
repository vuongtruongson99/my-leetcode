read = open("diamond.in")

n, k = map(int, read.readline().split())
arr = []
for i in range(n):
    a = int(read.readline())
    arr.append(a)

ans = 0
for i in range(n):
    check = 1
    for j in range(n):
        if i == j:
            continue
            
        if arr[i] <= arr[j] <= arr[i] + k:
            check += 1
    
    ans = max(ans, check)
    
print(ans, file=open("diamond.out", "w"))