read = open("pails.in")

x, y, m = map(int, read.readline().split())

ans = 0
for i in range(m // x + 1):
    remain = m - i * x
    total_y = remain // y
    ans = max(ans, i * x + total_y * y)

print(ans, file=open("pails.out", "w"))