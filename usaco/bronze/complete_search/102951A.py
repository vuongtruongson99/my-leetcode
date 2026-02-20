n = int(input())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        x = (xs[j] - xs[i])**2
        y = (ys[j] - ys[i])**2
        ans = max(ans, x+y)

print(ans)